CREATE EXTENSION vector;

CREATE TABLE xenon_lamps (
    id SERIAL PRIMARY KEY, -- Auto-incrementing primary key

    -- Product Information
    product_name TEXT NOT NULL,
    family_color_temperature_k NUMERIC, -- Using NUMERIC for flexibility, could be REAL or DOUBLE PRECISION
    family_power_min_w NUMERIC,
    family_power_max_w NUMERIC,
    family_color_rendering_index_text TEXT,
    application_areas TEXT[], -- Array of strings
    product_family_benefits TEXT[], -- Array of strings

    -- Electrical Characteristics
    nominal_current_a NUMERIC,
    current_control_range_min_a NUMERIC,
    current_control_range_max_a NUMERIC,
    nominal_power_w NUMERIC,
    nominal_voltage_v NUMERIC,

    -- Physical Dimensions & Weight
    diameter_mm NUMERIC,
    length_mm NUMERIC,
    length_with_base_without_pin_mm NUMERIC,
    light_center_length_lcl_mm NUMERIC,
    electrode_gap_cold_mm NUMERIC,
    product_weight_g NUMERIC,
    cable_length_mm NUMERIC,

    -- Operational Characteristics
    max_permissible_pinch_temperature_celsius NUMERIC,
    lifespan_h INTEGER,
    base_anode_standard_designation TEXT,
    base_cathode_standard_designation TEXT,
    cooling TEXT,
    burning_position TEXT,

    -- Regulatory & Identification
    reach_declaration_date DATE, -- Assuming this is a date
    primary_product_eans TEXT[], -- Array of strings
    reach_candidate_substance_name TEXT,
    reach_candidate_substance_cas TEXT,
    scip_numbers TEXT[], -- Array of strings

    -- Optional Identifiers
    country_specific_ean TEXT,
    metel_code TEXT,
    seg_number TEXT,
    stk_number TEXT,
    uk_org TEXT,

    -- Packaging Information
    packaging_product_code TEXT,
    packaging_product_description TEXT,
    packaging_unit_pieces INTEGER,
    packaging_dimension_length_mm NUMERIC,
    packaging_dimension_width_mm NUMERIC,
    packaging_dimension_height_mm NUMERIC,
    packaging_volume_dm3 NUMERIC,
    packaging_gross_weight_g NUMERIC,
    content TEXT,
    embedding vector(768) 
);
CREATE INDEX ON xenon_lamps USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);

-- Add comments to columns based on the 'title' from the JSON schema
COMMENT ON COLUMN xenon_lamps.product_name IS 'Product Name';
COMMENT ON COLUMN xenon_lamps.family_color_temperature_k IS 'Family Color Temperature K';
COMMENT ON COLUMN xenon_lamps.family_power_min_w IS 'Family Power Min W';
COMMENT ON COLUMN xenon_lamps.family_power_max_w IS 'Family Power Max W';
COMMENT ON COLUMN xenon_lamps.family_color_rendering_index_text IS 'Family Color Rendering Index Text';
COMMENT ON COLUMN xenon_lamps.application_areas IS 'Application Areas';
COMMENT ON COLUMN xenon_lamps.product_family_benefits IS 'Product Family Benefits';
COMMENT ON COLUMN xenon_lamps.nominal_current_a IS 'Nominal Current A';
COMMENT ON COLUMN xenon_lamps.current_control_range_min_a IS 'Current Control Range Min A';
COMMENT ON COLUMN xenon_lamps.current_control_range_max_a IS 'Current Control Range Max A';
COMMENT ON COLUMN xenon_lamps.nominal_power_w IS 'Nominal Power W';
COMMENT ON COLUMN xenon_lamps.nominal_voltage_v IS 'Nominal Voltage V';
COMMENT ON COLUMN xenon_lamps.diameter_mm IS 'Diameter Mm';
COMMENT ON COLUMN xenon_lamps.length_mm IS 'Length Mm';
COMMENT ON COLUMN xenon_lamps.length_with_base_without_pin_mm IS 'Length With Base Without Pin Mm';
COMMENT ON COLUMN xenon_lamps.light_center_length_lcl_mm IS 'Light Center Length Lcl Mm';
COMMENT ON COLUMN xenon_lamps.electrode_gap_cold_mm IS 'Electrode Gap Cold Mm';
COMMENT ON COLUMN xenon_lamps.product_weight_g IS 'Product Weight G';
COMMENT ON COLUMN xenon_lamps.cable_length_mm IS 'Cable Length Mm';
COMMENT ON COLUMN xenon_lamps.max_permissible_pinch_temperature_celsius IS 'Max Permissible Pinch Temperature Celsius';
COMMENT ON COLUMN xenon_lamps.lifespan_h IS 'Lifespan H';
COMMENT ON COLUMN xenon_lamps.base_anode_standard_designation IS 'Base Anode Standard Designation';
COMMENT ON COLUMN xenon_lamps.base_cathode_standard_designation IS 'Base Cathode Standard Designation';
COMMENT ON COLUMN xenon_lamps.cooling IS 'Cooling';
COMMENT ON COLUMN xenon_lamps.burning_position IS 'Burning Position';
COMMENT ON COLUMN xenon_lamps.reach_declaration_date IS 'Reach Declaration Date';
COMMENT ON COLUMN xenon_lamps.primary_product_eans IS 'Primary Product Eans';
COMMENT ON COLUMN xenon_lamps.reach_candidate_substance_name IS 'Reach Candidate Substance Name';
COMMENT ON COLUMN xenon_lamps.reach_candidate_substance_cas IS 'Reach Candidate Substance Cas';
COMMENT ON COLUMN xenon_lamps.scip_numbers IS 'Scip Numbers';
COMMENT ON COLUMN xenon_lamps.country_specific_ean IS 'Country Specific Ean';
COMMENT ON COLUMN xenon_lamps.metel_code IS 'Metel Code';
COMMENT ON COLUMN xenon_lamps.seg_number IS 'Seg Number';
COMMENT ON COLUMN xenon_lamps.stk_number IS 'Stk Number';
COMMENT ON COLUMN xenon_lamps.uk_org IS 'Uk Org';
COMMENT ON COLUMN xenon_lamps.packaging_product_code IS 'Packaging Product Code';
COMMENT ON COLUMN xenon_lamps.packaging_product_description IS 'Packaging Product Description';
COMMENT ON COLUMN xenon_lamps.packaging_unit_pieces IS 'Packaging Unit Pieces';
COMMENT ON COLUMN xenon_lamps.packaging_dimension_length_mm IS 'Packaging Dimension Length Mm';
COMMENT ON COLUMN xenon_lamps.packaging_dimension_width_mm IS 'Packaging Dimension Width Mm';
COMMENT ON COLUMN xenon_lamps.packaging_dimension_height_mm IS 'Packaging Dimension Height Mm';
COMMENT ON COLUMN xenon_lamps.packaging_volume_dm3 IS 'Packaging Volume Dm3';
COMMENT ON COLUMN xenon_lamps.packaging_gross_weight_g IS 'Packaging Gross Weight G';