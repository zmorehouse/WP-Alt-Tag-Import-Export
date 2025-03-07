Basic script to import Media Library Alt Tags from an old Wordpress site into a new one. 

You'll need to export a media XML file from the old site (Tools > Export > Media). Use the extract.py script to generate a csv. Then import the csv into the new site via functions.php

This script matches based on title but you can rejig as you see fit (filename, url, etc.) - just modify the python script to grab the relevant XML field and the functions to look it up. 