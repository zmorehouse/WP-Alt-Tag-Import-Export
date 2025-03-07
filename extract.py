import csv
import xml.etree.ElementTree as ET
import os

xml_file = "example.xml"  # Filename of the wordpress export xml - place it in the current directory
tree = ET.parse(xml_file)
root = tree.getroot()

namespace = {'wp': 'http://wordpress.org/export/1.2/'}

ignore_empty = True  # Set to false if you want to ignore empty tags

csv_filename = "image_alt_tags.csv" # Filename for the csv
csv_data = [("title", "alt_text")] 

for item in root.findall("channel/item", namespace):
    attachment_url = item.find("wp:attachment_url", namespace)
    alt_text = ""
    title = item.find("title", namespace).text.strip() 

    for meta in item.findall("wp:postmeta", namespace):
        meta_key = meta.find("wp:meta_key", namespace)
        meta_value = meta.find("wp:meta_value", namespace)

        if meta_key is not None and meta_value is not None:
            if meta_key.text == "_wp_attachment_image_alt":
                alt_text = meta_value.text.strip() if meta_value.text else ""
                break  

    if attachment_url is not None:
        image_url = attachment_url.text
        filename = os.path.basename(image_url) 

        if not ignore_empty or alt_text:
            csv_data.append((title, alt_text))

with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

print(f"CSV file '{csv_filename}' has been created successfully.")


