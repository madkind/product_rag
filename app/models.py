from typing import List, Optional
from pydantic import BaseModel

class XenonLamp(BaseModel):
    # Allgemeine Produktinformationen - General Product Information
    product_name: str # Produktbezeichnung, z.B. "XBO 10000 W/HS OFR"
    
    # Produktfamilien-Eigenschaften - Common properties for the product family
    # Diese Werte stammen aus dem Abschnitt "Produktfamilien-Eigenschaften" der Dokumente.
    family_color_temperature_k: float # Farbtemperatur der Produktfamilie in Kelvin (z.B. 6000)
    family_power_min_w: float # Minimale Leistung der Produktfamilie in Watt (aus Bereichsangabe, z.B. 450)
    family_power_max_w: float # Maximale Leistung der Produktfamilie in Watt (aus Bereichsangabe, z.B. 10000)
    family_color_rendering_index_text: str # Textuelle Angabe zum Farbwiedergabeindex der Produktfamilie (z.B. ">" wenn nur "Ra >" angegeben ist)
    
    application_areas: List[str] # Anwendungsgebiete, z.B. ["Klassische 35-mm-Filmprojektion", ...]
    product_family_benefits: List[str] # Produktfamilien-Vorteile, z.B. ["Kurzbogen mit sehr hoher Leuchtdichte...", ...]

    # Elektrische Daten - Electrical Data
    nominal_current_a: float # Nennstrom in Ampere
    current_control_range_min_a: float # Minimaler Stromsteuerbereich in Ampere
    current_control_range_max_a: float # Maximaler Stromsteuerbereich in Ampere
    nominal_power_w: float # Nennleistung in Watt
    nominal_voltage_v: float # Nennspannung in Volt

    # Abmessungen & Gewicht - Dimensions & Weight
    diameter_mm: float # Durchmesser in Millimeter
    length_mm: float # Gesamtlänge in Millimeter
    length_with_base_without_pin_mm: float # Länge mit Sockel jedoch ohne Sockelstift in Millimeter
    light_center_length_lcl_mm: float # Abstand Lichtschwerpunkt (LCL) in Millimeter
    electrode_gap_cold_mm: float # Elektrodenabstand (kalt) in Millimeter
    product_weight_g: float # Produktgewicht in Gramm
    cable_length_mm: float # Kabellänge in Millimeter (aus "Kabellänge" oder "Kabel-/Leitungslänge, Eingangsseite")

    # Temperaturen & Betriebsbedingungen - Temperatures & Operating Conditions
    max_permissible_pinch_temperature_celsius: float # Maximal zulässige Temperatur an der Quetschung in Grad Celsius

    # Lebensdauer - Lifespan
    lifespan_h: int # Lebensdauer in Stunden

    # Zusätzliche Produktdaten - Additional Product Data
    base_anode_standard_designation: str # Sockel Anode (Normbezeichnung)
    base_cathode_standard_designation: str # Sockel Kathode (Normbezeichnung)

    # Einsatzmöglichkeiten - Capabilities / Usage
    cooling: str # Art der Kühlung, z.B. "Forciert"
    burning_position: str # Zulässige Brennstellung, z.B. "s15/p15"

    # Umwelt Informationen (REACh) - Environmental Information (REACh)
    reach_declaration_date: str # Datum der REACh Deklaration (Format z.B. "18-08-2023")
    primary_product_eans: List[str] # Primäre Erzeugnisnummern (EANs), oft eine Liste von Strings
    reach_candidate_substance_name: str # Name des Stoffs der Kandidatenliste (z.B. "Lead")
    reach_candidate_substance_cas: str # CAS-Nummer des Stoffs der Kandidatenliste (z.B. "7439-92-1")
    scip_numbers: List[str] # SCIP Deklarationsnummern, oft eine Liste von Strings

    # Länderspezifische Informationen - Country Specific Information (Optional, da nicht in allen Dokumenten vorhanden)
    country_specific_ean: Optional[str] = None # Länderspezifische EAN (falls vorhanden)
    metel_code: Optional[str] = None # METEL-Code (falls vorhanden)
    seg_number: Optional[str] = None # SEG-Nummer (falls vorhanden, oft "-")
    stk_number: Optional[str] = None # STK-Nummer (falls vorhanden, oft "-")
    uk_org: Optional[str] = None # UK Org Kürzel (falls vorhanden, oft "-")

    # Verpackungsinformationen - Packaging Information
    packaging_product_code: str # Produkt-Code der Verpackung (oft eine EAN)
    packaging_product_description: str # Produkt-Bezeichnung auf der Verpackung
    packaging_unit_pieces: int # Verpackungseinheit (Stück pro Einheit)
    packaging_dimension_length_mm: float # Länge der Verpackung in Millimeter
    packaging_dimension_width_mm: float # Breite der Verpackung in Millimeter
    packaging_dimension_height_mm: float # Höhe der Verpackung in Millimeter
    packaging_volume_dm3: float # Volumen der Verpackung in Kubikdezimeter (dm³)
    packaging_gross_weight_g: float # Bruttogewicht der Verpackung in Gramm