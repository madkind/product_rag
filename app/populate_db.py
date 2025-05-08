import os
import dotenv
import psycopg2
import json
from models import XenonLamp
from embedding import XenonLampEmbeddingSystem

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

    try:
        conn = psycopg2.connect(**db_conn_params)
        cur = conn.cursor()
        # Dynamically fetch columns from the table (excluding id)
        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'xenon_lamps' AND column_name != 'id' ORDER BY ordinal_position;")
        columns = [row[0] for row in cur.fetchall()]
        table_name = "xenon_lamps"
        column_names_sql = ", ".join(columns)
        value_placeholders = ", ".join(["%s"] * len(columns))
        insert_query = f"INSERT INTO {table_name} ({column_names_sql}) VALUES ({value_placeholders})"

        embedding_system = XenonLampEmbeddingSystem()
        data_to_insert = []
        for record_dict in lamp_data_array:
            row_values = []
            for col_name in columns:
                if col_name == 'embedding':
                    # Always generate embedding from content
                    content = record_dict.get('content', '')
                    row_values.append(embedding_system.generate_embedding(content).tolist())
                else:
                    row_values.append(record_dict.get(col_name, None))
            data_to_insert.append(tuple(row_values))
        cur.executemany(insert_query, data_to_insert)
        inserted_count = cur.rowcount
        conn.commit()
        print(f"Successfully inserted {inserted_count} records into '{table_name}'.")
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Database error during insertion into 'xenon_lamps': {e}")
        return 0
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"An unexpected error occurred: {e}")
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