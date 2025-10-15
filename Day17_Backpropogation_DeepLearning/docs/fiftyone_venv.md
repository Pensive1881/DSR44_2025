# Installing FiftyOne with `venv`

[FiftyOne](https://voxel51.com/fiftyone/) is an open-source toolkit for building high-quality datasets and computer vision workflows.

I recommend [installing Python3.11](https://github.com/andandandand/practical-computer-vision/blob/main/docs/installing_python311.md) to run the examples on this repository. 

## Installation

Follow these steps to install FiftyOne using Python 3.11 in a dedicated virtual environment named `.venv`.

### 1. Create a Virtual Environment

```bash
python3.11 -m venv .venv
````

### 2. Activate the Environment

* On **Linux/macOS**:

  ```bash
  source .venv/bin/activate
  ```

* On **Windows**:

  ```bash
  .venv\Scripts\activate
  ```

### 3. Upgrade `pip`

```bash
pip install --upgrade pip
```

### 4. Install FiftyOne

```bash
pip install fiftyone
```

### 5. (Optional) Launch the App

The app is the portion of FiftyOne that shows our dataset alongside all its avaialable fields and metadata.

```bash
fiftyone app launch
```

## Installing Additional Requirements

If you have a `requirements.txt` with extra dependencies (e.g., for training, evaluation, or visualization), install them with:

```bash
pip install -r requirements.txt
```

## Deactivating the Environment

To exit the virtual environment when done:

```bash
deactivate
```

## Notes

* FiftyOne automatically manages a local MongoDB instance.
* To install with optional features like video, OpenCV, or point clouds:

  ```bash
  pip install 'fiftyone[all]'
  ```

For more documentation, visit the [FiftyOne Docs](https://docs.voxel51.com/).



