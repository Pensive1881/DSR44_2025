import fiftyone as fo
from fiftyone.utils.huggingface import load_from_hub
from pathlib import Path


dataset_name = "wikiart_dataset_local"

# Delete the dataset if it already exists
if fo.dataset_exists(dataset_name):
    fo.delete_dataset(dataset_name)
    print(f"Dataset '{dataset_name}' deleted.")
else:
    print(f"Dataset '{dataset_name}' does not exist.")


# Load the dataset from Hugging Face Hub
# This dataset is a collection of artworks from WikiArt with more than 11k images
# The dataset is available in parquet format
# The dataset is classified by artist, style, and genre
# The dataset is downloaded to the local disk and can be used offline
dataset = load_from_hub(
    "huggan/wikiart",
    format="parquet",
    classification_fields=["artist", "style", "genre"],
    max_samples=500,
    name=dataset_name,
    persistent=True,
)

print("Dataset loaded from Hugging Face Hub")
# Print the dataset information
print("Dataset information:")
print(dataset)

session = fo.launch_app(dataset)

#If we ran this in code we would need to hold the session open to prevent the app server from exiting
session.wait()
