# AmbientCG Textures Downloader

A simple Python script to bulk download textures from ambientcg.com with some customization. 

By default, it downloads **2K PNG Materials** and excludes "HDRI", "Substance", "Set", "3D", "Backdrop", "Brush", "Terrain", "Pathway", "Leaf", "Sticker", "End", "Grate", "Payment", "Sign", "Facade", "Imperfections", "Painting", "Pizza", "Rails". **(You can customize this)**

## Setup & Usage

1.  Install the required lib:
    ```bash
    pip install requests
    ```
2.  Run the script:
    ```bash
    python main.py
    ```

## Configuration

Edit the variables at the top of `main.py` to customize your download.

You need to check the file: https://ambientCG.com/api/v2/downloads_csv to know what to change.

## Credits

This project uses ambientCG's API: [AmbientCG API](https://docs.ambientcg.com/api/)