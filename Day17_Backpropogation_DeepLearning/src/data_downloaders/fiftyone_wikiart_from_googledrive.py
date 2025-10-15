
import os
import requests
import zipfile
import io
import gdown
import fiftyone as fo

# Google Drive file ID
# This file ID is for a zip file containing images from the WikiArt dataset
file_id = "1rFGWJnvOpsj6OBq1iKeyIstLNz5gPy8R"

# Extract the zip file to a directory
extract_dir = "downloads/wikiart"

# Download the zip file from Google Drive
url = f"https://drive.google.com/uc?id={file_id}"
print(f"Downloading from {url}...")
download_dir = "downloads/test"
os.makedirs(download_dir, exist_ok=True)

file_id_shortened = file_id[:8]  # Shortened file ID for the output filename
output = os.path.join(download_dir, f"test1_{file_id_shortened}.zip")
try:
    gdown.download(url, output, quiet=False)
except Exception as e:
    print(f"Error downloading file: {e}")
    print("Please ensure the file is shared publicly on Google Drive.")
    exit()

os.makedirs(extract_dir, exist_ok=True)
try:
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
except FileNotFoundError:
    print(f"Error: The file {output} was not found. Check if the download was successful.")
    exit()

# Create a FiftyOne dataset from the extracted images
dataset = fo.Dataset.from_dir(
    dataset_dir=extract_dir,
    dataset_type=fo.types.ImageDirectory,
    name="downloaded-dataset"
)

# Launch the FiftyOne App
session = fo.launch_app(dataset)
session.wait()