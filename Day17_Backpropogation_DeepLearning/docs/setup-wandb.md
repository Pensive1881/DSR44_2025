# Setting Up Weights & Biases (W&B) API Token

This guide shows you how to set up a W&B (aka `wandb`) account and use your API token securely in Kaggle and Colab notebooks. 

We use `wandb` to save trained PyTorch models, FiftyOne datasets, and performance metrics obtained during training, validation, and testing. 

`wandb` is a [Python package](https://pypi.org/project/wandb/). It comes preinstalled on both Kaggle and Google Colab. If you want to run it on your local machine, you will need to run 

```
pip install wandb
```

## Create an Account on W&B

1. Go to https://wandb.ai/
2. Click "Sign up"
3. Create an account using:
   - Email + password
   - Google account
   - GitHub account

## Get Your API Key

1. Log in to your W&B account, and go to to https://wandb.ai/authorize, you can copy the key from there. Alternatively, you can follow the next steps 
2. Click your profile picture in the top-right corner
3. Select "Settings"
4. Click on "API keys" in the left sidebar
5. Copy your API key (it starts with something like "abc123def456...")

## Add API Key to Kaggle

1. Open your Kaggle notebook
2. Click "Add-ons" in the top navigation bar
3. Select "Secrets"
4. Click "Create new secret"
5. Name it `WANDB_API_KEY`
6. Paste your API key in the value field
7. Click "Create"
8. Make sure that the entry is set with a checkbox to its left so that the key is usable in the Kaggle notebook

## Add API Key to Colab

1. Open your Colab notebook
2. Click the "Secrets" icon in the left sidebar (looks like a key)
3. Click "Add new secret"
4. Set the name as `WANDB_API_KEY`
5. Paste your API key as the value
6. Grant notebook access to the Secret entry

## Using the API Key in Colab

```python
# Access the W&B API key from Colab secrets
import wandb
import os
from google.colab import userdata

# Get API key from secrets
api_key = userdata.get('WANDB_API_KEY')

# Set the environment variable
os.environ["WANDB_API_KEY"] = api_key

# Verify login
wandb.login()
```

## Using the API Key in Kaggle

```python
# Access the W&B API key from Kaggle secrets
import wandb
import os
from kaggle_secrets import UserSecretsClient

# Get API key from secrets
secret_label = "WANDB_API_KEY"
secret_value = UserSecretsClient().get_secret(secret_label)

# Set the environment variable
os.environ['WANDB_API_KEY'] = secret_value
wandb.login()
```



## Test your setup in any of the above configurations

Run this code to verify everything works:

```python
# Start a new run
wandb.init(project="test-project")

# Log a simple metric
wandb.log({"test_value": 123})

# Finish the run
wandb.finish()
```

If you see a link to your W&B dashboard, you're all set up!
