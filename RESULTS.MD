
**Question:** How much does the XBO 4000 W/HS XL OFR weigh?

**Expert Advice:** To answer the customer's question about the weight of the "XBO 4000 W/HS XL OFR" lamp, filter by `product_name` = "XBO 4000 W/HS XL OFR" and retrieve the value of `product_weight_g`.

**SQL Query:**
```sql
SELECT "product_weight_g" FROM xenon_lamps WHERE "product_name" = 'XBO 4000 W/HS XL OFR'
```

**DB Results (concatenated without content):**
[(Decimal('1022.9'),)]

**Answer:**
The OSRAM XBO 4000 W/HS XL OFR lamp weighs approximately 1023 grams. This lamp is a Xenon short-arc lamp commonly used in cinema projectors and other high-intensity lighting applications.

---

**Question:** Which luminaire is best suited for my home theater?

**Expert Advice:** For a home theater, prioritize these factors:

1.  **Application Areas:** Filter for "Digitale Film- und Videoprojektion".
2.  **Power:** Consider `family_power_min_w` and `family_power_max_w`. Lower wattage lamps are generally suitable for home use.
3.  **Color Temperature:** `family_color_temperature_k` around 6000K is standard, but personal preference matters.
4.  **Product Family Benefits:** Look for "Hohe Lichtbogenstabilität" and "Breiter Dimmbereich".
5.  **Lifespan:** `lifespan_h` should be reasonably high for longevity.

**SQL Query:**
```sql
SELECT
  "product_name",
  "content",
  CASE
    WHEN 'Digitale Film- und Videoprojektion' = ANY ("application_areas")
    THEN 1
    ELSE 0
  END AS application_area_match,
  CASE
    WHEN "family_power_min_w" BETWEEN 100 AND 500
    THEN 1
    ELSE 0
  END AS power_preference_match,
  CASE
    WHEN ABS("family_color_temperature_k" - 6000) <= 500
    THEN 1
    ELSE 0
  END AS color_temperature_match,
  CASE
    WHEN 'Hohe Lichtbogenstabilität' = ANY ("product_family_benefits")
    THEN 1
    ELSE 0
  END AS stability_match,
  CASE
    WHEN 'Breiter Dimmbereich' = ANY ("product_family_benefits")
    THEN 1
    ELSE 0
  END AS dimming_match
FROM xenon_lamps
ORDER BY
  application_area_match DESC,
  power_preference_match DESC,
  color_temperature_match DESC,
  stability_match DESC,
  dimming_match DESC,
  "lifespan_h" DESC
LIMIT 5;
```

**DB Results (concatenated without content):**
[('XBO 1600 W XL OFR', 1, 1, 1, 1, 1), ('XBO 2000 W/HTP XL OFR', 1, 1, 1, 1, 1), ('XBO 2000 W/H XL OFR', 1, 1, 1, 1, 1), ('XBO 1600 W/HSC XL OFR', 1, 1, 1, 1, 1), ('XBO 1000 W/HTP OFR', 1, 1, 1, 1, 1)]

**Answer:**
Based on your need for a home theater, I recommend the **XBO 1000 W/HTP OFR**.

Here's why:

*   **Application:** These lamps are designed for digital film and video projection, making them ideal for home theaters.
*   **Product Family Benefits:** This lamp offers very high luminance for bright screen illumination, a constant color temperature of 6,000 K throughout its lifespan, ease of maintenance, high arc stability, instant light on the screen due to the hot restart function, and a wide dimming range.

---

**Question:** Give me all lamps with at least 1500W and a lifetime of more than 3000 hours.

**Expert Advice:** Here's how to select the appropriate lamps based on the customer's request:

1.  **Power:** Filter for lamps where `family_power_max_w` is greater than or equal to 1500.
2.  **Lifespan:** Filter for lamps where `lifespan_h` is greater than 3000.

**SQL Query:**
```sql
SELECT "product_name", "content"
FROM xenon_lamps
WHERE "family_power_max_w" >= 1500 AND "lifespan_h" > 3000
LIMIT 5;
```

**DB Results (concatenated without content):**
[('XBO 1600 W XL OFR',), ('XBO 2000 W/H XL OFR',), ('XBO 2000 W/HTP XL OFR',)]

**Answer:**
Based on your requirements for a Xenon short-arc discharge lamp with at least 1500W and a lifespan exceeding 3000 hours, I recommend the following OSRAM products:

*   **XBO 2000 W/H XL OFR:** This lamp offers a very high luminance short arc for brighter screen illumination and a constant color temperature of 6,000 K throughout its lifespan. It features high arc stability and a hot restart function for instant light on the screen.

*   **XBO 2000 W/HTP XL OFR:** This lamp offers a very high luminance short arc for brighter screen illumination and a constant color temperature of 6,000 K throughout its lifespan. It features high arc stability and a hot restart function for instant light on the screen.

*   **XBO 1600 W XL OFR:** This lamp offers a very high luminance short arc for brighter screen illumination and a constant color temperature of 6,000 K throughout its lifespan. It features high arc stability and a hot restart function for instant light on the screen.

---

**Question:** Which luminaire has the SCIP number dd2ddf15-037b-4473-8156-97498e721fb3?

**Expert Advice:** To find the luminaire with the SCIP number "dd2ddf15-037b-4473-8156-97498e721fb3", filter the data where `scip_numbers` contains "dd2ddf15-037b-4473-8156-97498e721fb3".

**SQL Query:**
```sql
SELECT
  "product_name",
  "content"
FROM
  xenon_lamps
WHERE
  'dd2ddf15-037b-4473-8156-97498e721fb3' = ANY("scip_numbers")
LIMIT 5;
```

**DB Results (concatenated without content):**
[('XBO 3000 W/HS XL OFR',)]

**Answer:**
The luminaire with the SCIP number dd2ddf15-037b-4473-8156-97498e721fb3 is the **XBO 3000 W/HS XL OFR**.

Here are some of its key benefits:

*   It features a short arc with very high luminance, resulting in brighter screen illumination.
*   It maintains a consistent color temperature of 6,000 K throughout its lifespan.
*   It offers easy maintenance.
*   It provides high arc stability.
*   It allows for instant light on the screen due to its hot restart capability.