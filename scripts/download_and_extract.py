import requests
from PIL import Image
import os


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded to {save_path}")
    else:
        print("Failed to download image")


def extract_tiles(image_path, tile_width, tile_height, rows, cols, output_dir):
    image = Image.open(image_path)
    img_width, img_height = image.size

    if img_width != tile_width * cols or img_height != tile_height * rows:
        print("Warning: The image size does not match the expected tile grid size!")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    tile_count = 0
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height

            tile = image.crop((left, upper, right, lower))
            tile_path = os.path.join(output_dir, f"tile_{tile_count}.png")
            tile.save(tile_path)
            print(f"Tile {tile_count} saved as {tile_path}")
            tile_count += 1


def main():
    image_url = "https://discord.com/assets/55e1dff9b6a3ad363e9f.png"
    download_path = "tiled_image.png"

    download_image(image_url, download_path)

    tiles_dir = "tiles"

    tile_width = 48
    tile_height = 48
    rows = 4
    cols = 20

    extract_tiles(download_path, tile_width, tile_height, rows, cols, tiles_dir)

if __name__ == "__main__":
    main()
