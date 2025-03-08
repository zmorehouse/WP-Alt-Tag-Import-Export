# WordPress Media Library Alt Tag Importer

## Overview
This repository contains scripts to help migrate image alt tags from an old WordPress site to a new one. The process involves exporting media data from the old site, extracting alt tags into a CSV file, and importing them into the new WordPress site.

## How It Works
1. **Export Media Data**:  
   - In the old WordPress site, go to `Tools > Export` and choose `Media`.  
   - Download the XML export file.

2. **Extract Alt Tags to CSV**:  
   - Use the `extract.py` script to process the XML file and generate a CSV file containing image titles and alt text.  
   - The CSV format should be:  
     ```
     Image Title,Alt Text
     example-image,This is an example alt text
     ```

3. **Import Alt Tags into the New WordPress Site**:  
   - Upload the generated CSV file to `wp-content/path/image_alt_tags.csv` on the new WordPress site.  
   - Append the `functions.php` script to your theme’s `functions.php` file.  
   - Visit the WordPress admin dashboard once to trigger the script (`admin_init` action).  
   - The script will search for media attachments by title and update their alt tags accordingly.

4. **Remove the Function**:  
   - Once the import is complete, **remove the function from `functions.php`** to prevent unnecessary execution.

## Customisation
- The default matching method is by **image title**.  
- If needed, modify `extract.py` to extract a different identifier (e.g., filename, URL).  
- Adjust the SQL query in `functions.php` if using a different matching field.

## Notes
- Ensure the CSV file is correctly formatted before running the import.  
- If image titles differ between the old and new sites, the script may not find matches.  
- Always back up your database before making bulk changes.

