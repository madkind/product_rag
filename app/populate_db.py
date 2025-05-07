import os
import dotenv
import psycopg2
import json
from models import XenonLamp

dotenv.load_dotenv()

def get_db_params_from_env():
    return {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
    }

def insert_xenon_lamps(db_conn_params: dict, lamp_data_array: list[dict]):
    if not lamp_data_array:
        print("No data provided to insert.")
        return 0

    conn = None
    cur = None
    inserted_count = 0

    # The order of columns here MUST match the order of values extracted from each JSON object.
    # These are derived from the JSON_SCHEMA properties and match the DB table columns
    # (excluding 'id', 'created_at', 'updated_at' which are auto-managed by the DB).
    columns = list(XenonLamp.model_json_schema()['properties'].keys())
    
    # Construct the SQL query
    # e.g., INSERT INTO xenon_lamps (col1, col2, ...) VALUES (%s, %s, ...)
    table_name = "xenon_lamps"
    column_names_sql = ", ".join(columns)
    value_placeholders = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({column_names_sql}) VALUES ({value_placeholders})"

    # Prepare data for executemany: a list of tuples
    data_to_insert = []
    for record_dict in lamp_data_array:
        row_values = []
        for col_name in columns:
            # Use .get(col_name, None) if you suspect some keys might be missing
            # even if defined in schema (e.g. optional fields not present in input).
            # Given the schema defines defaults for optional fields like 'country_specific_ean',
            # they should ideally be present in a well-formed JSON, even if with a null value.
            # If a required field is missing, this will raise a KeyError or insert None,
            # potentially causing a DB error if the column is NOT NULL.
            # For robustness, one might add jsonschema validation before this step.
            value = record_dict.get(col_name) 
            
            # psycopg2 handles Python lists to SQL arrays (e.g., TEXT[]) automatically.
            # psycopg2 handles Python None to SQL NULL automatically.
            # psycopg2 handles Python int/float to SQL INTEGER/NUMERIC automatically.
            # For DATE type (reach_declaration_date), if the string is in 'YYYY-MM-DD' format,
            # PostgreSQL usually casts it correctly. Otherwise, pre-processing might be needed.
            row_values.append(value)
        data_to_insert.append(tuple(row_values))

    try:
        conn = psycopg2.connect(**db_conn_params)
        cur = conn.cursor()

        cur.executemany(insert_query, data_to_insert)
        inserted_count = cur.rowcount  # Number of rows affected
        conn.commit()
        print(f"Successfully inserted {inserted_count} records into '{table_name}'.")

    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Database error during insertion into '{table_name}': {e}")
        # Depending on requirements, you might want to re-raise the exception
        # raise
        return 0 # Indicate failure or partial success by returning 0
    except KeyError as e:
        if conn:
            conn.rollback()
        print(f"Data error: Missing key {e} in one of the JSON objects. "
              f"Ensure all JSON objects conform to the schema.")
        # raise
        return 0
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"An unexpected error occurred: {e}")
        # raise
        return 0
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return inserted_count

def load_lamps_data_from_json_folder(json_folder_path):
    lamps_data = []
    for filename in os.listdir(json_folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    lamps_data.append(data)
                except Exception as e:
                    print(f"Failed to load {filename}: {e}")
    return lamps_data

if __name__ == '__main__':
    # --- Example Usage ---
    db_params = get_db_params_from_env()
    json_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'json')
    lamps_data = load_lamps_data_from_json_folder(json_folder)
    num_inserted = insert_xenon_lamps(db_params, lamps_data)