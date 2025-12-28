# Warning: This script default options download 2K-PNG textures and exclude a lot of things.
# If you want to customize, check the https://ambientCG.com/api/v2/downloads_csv file and change the code to your liking. The .csv file is very simple.

import csv
import os
import requests # Install with: pip install requests

## Options ##
resolution = "2K" # Valid options: "1K", "2K", "4K", "8K"
file_format = "PNG" # Valid options: "JPG", "PNG"
match_attr = f"{resolution}-{file_format}" # Exact matching, avoid unwanted matching behaviour (Like matching 2K also include 12K, 24K, 32K, etc.)

# Exclude rows with these values in "assetId" (it's the same as the name of the asset in the web version)
# My list
exclude_values = ["HDRI", "Substance", "Set", "3D", "Backdrop", "Brush", "Terrain", "Pathway", "Leaf", "Sticker",
                   "End", "Grate", "Payment", "Sign", "Facade", "Imperfections", "Painting", "Pizza", "Rails"]

# exclude_values = ["None"] # Use this and remove the line above if you want to exclude nothing

download_folder_name = "downloaded_textures" # If you change this, you should also update the .gitignore
## ======= ##

os.makedirs(download_folder_name, exist_ok=True)

api_url = "https://ambientCG.com/api/v2/downloads_csv" #Get lastest link from https://docs.ambientcg.com/api/
# Fetch CSV with basic safety checks
api_response = requests.get(api_url, timeout=30)
api_response.raise_for_status()

api_file = "downloads.csv" # If you change this, you should also update the .gitignore

# Write content to local .csv file
with open(api_file, "wb") as file:
    file.write(api_response.content)

# Open the file and start downloading
with open(api_file, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        asset_id = row.get("assetId", "")
        attr = row.get("downloadAttribute", "")
        link = row.get("downloadLink", "")

        # Skip if not sastisfied
        if not asset_id or not attr or not link:
            continue

        if any(excluded in asset_id for excluded in exclude_values):
            continue

        if match_attr != attr: # Exact matching, avoid unwanted matching behaviour
            continue

        output = os.path.join(download_folder_name, link.split("file=")[1])

        if os.path.exists(output):
            print(f"{output} already exists. Skipped.")
            continue

        link_response = requests.get(link, stream=True, timeout=60)
        link_response.raise_for_status()

        with open(output, "wb") as output_file:
            for chunk in link_response.iter_content(chunk_size=1024 * 1024): # Chunking, in case downloading huge files like 8K-PNG
                if chunk:
                    output_file.write(chunk)

        print(f"{output} is successfully downloaded.")

# Multithreaded download can be added, but it may not be good for the server, not really recommended.