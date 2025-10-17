# How to Get GPU and TPU Access in Kaggle Notebooks

Kaggle gives you free access to faster computers (GPUs and TPUs) to speed up your machine learning projects. This guide will show you how to use them.

## Table of Contents
1. [Understanding Kaggle's Accelerators](#understanding-kaggles-speed-boosters)
2. [Setting Up a Kaggle Account](#setting-up-a-kaggle-account)
3. [Creating a New Notebook](#creating-a-new-notebook)
4. [Turning On GPU/TPU](#turning-on-gputpu)
5. [Checking If It's Working](#checking-if-its-working)
6. [Time Limits and Tips](#time-limits-and-tips)
7. [Fixing Common Problems](#fixing-common-problems)
8. [Example Code](#example-code)

## Understanding Kaggle's Accelerators

Kaggle offers three types of computers:

- **Regular Computer (CPU)**: The basic option that works for simple tasks (no accelerator added).
- **Graphics Card (GPU)**: NVIDIA P100, much faster for machine learning.
- **Dual T4 GPUs**: Two NVIDIA T4 GPUs that work together, great for larger models or faster training.
- **Special Chip (TPU)**: Google's custom chip, extremely fast for certain tasks.

Think of it like this:
- **CPU**: A regular car
- **GPU (P100)**: A sports car (faster for most machine learning)
- **Dual T4 GPUs**: Two sports cars working together (more memory and computing power)
- **TPU**: A rocket ship (extremely fast but only for specific tasks)

### When to Choose Between Accelerators

**Use P100 GPU when:**
- Working with smaller models or datasets
- Using PyTorch as your main framework
- Running varied operations with different data sizes
- Needing more flexibility in your code
- Working on individual projects or experimentation

**Use Dual T4 GPUs when:**
- Your model needs more memory than a single P100 GPU provides
- You're training medium to large-sized models
- You want to run multiple experiments in parallel
- You need to process larger batches of data
- You're fine-tuning pre-trained models like BERT or ResNet

**Use TPU when:**
- Training very large neural networks
- Processing large batches of data at once
- Working with transformer models (like BERT, GPT)
- Running computer vision or NLP tasks at scale
- Using consistent data shapes throughout your model
- Your operations can use bfloat16 precision

## Setting Up a Kaggle Account

1. Go to [Kaggle's website](https://www.kaggle.com/).
2. Click "Register" to create a new account or "Sign In" if you already have one.
3. Complete the registration process if needed.
4. Verify your phone number (required for using the faster computers). See the detailed phone verification steps in the next section.

## Phone Number Verification

To use GPUs and TPUs on Kaggle, you must verify your phone number. Here's how:

1. Click on your profile picture in the top-right corner of the Kaggle website.
2. Select "Settings" from the dropdown menu.
3. Scroll down to the "Phone Verification" section.
4. Click "Verify Phone" button.
5. Enter your phone number with country code (e.g., +1 for USA).
6. Click "Send Code" button.
7. Check your phone for an SMS with a verification code.
8. Enter the code in the verification box on Kaggle.
9. Click "Verify" to complete the process.
10. You should see a confirmation message that your phone is verified.

Once your phone is verified, you can use GPUs and TPUs in your notebooks.

## Creating a New Notebook

1. Go to the "Code" tab on the Kaggle homepage.
2. Click the "New Notebook" button.
3. A new notebook will open in Kaggle.

## Turning On GPU/TPU

1. In your notebook, click on the "Settings" button on the right side.
2. Under "Accelerator," you'll see four options:
   - None (regular computer with no accelerator attached)
   - GPU P100 (faster graphics card)
   - GPU T4 x2 (two T4 graphics cards working together)
   - TPU (special chip)
3. Select either "GPU" or "TPU" depending on what you need.
4. Click "Save" to apply your changes.
5. The notebook will restart with your selected speed booster turned on.

## Checking If It's Working

### For GPU:

```python
# Check if GPU is available
import torch
print("GPU Available: ", torch.cuda.is_available())
print("GPU Type: ", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
```

### For TPU:

```python
# Check if TPU is available
import torch_xla.core.xla_model as xm
print("TPU Available: ", xm.is_available())
print("TPU Cores: ", xm.xrt_world_size() if xm.is_available() else "No TPU")
```

## Time Limits and Tips

Kaggle limits how much you can use these accelerators:

- **GPU**: 30 hours per week
- **TPU**: 20 hours per week

Tips to make the most of your time:

1. **Save your work often** so you don't lose progress.
2. **Turn off the speed boosters** when you're not using them by switching back to CPU.
3. **Test your code on small samples** before running big jobs.
4. **Save checkpoints** of your models so you can continue if you run out of time.
5. **Do simple tasks on the CPU** and only use GPU/TPU for the heavy lifting.

## Fixing Common Problems

### Common Issues:

1. **"No GPU/TPU available" error**:
   - Make sure your account has a verified phone number.
   - Check if you've used up your weekly time limit.
   - Try a different browser or clear your cache.

2. **Slow performance despite using GPU/TPU**:
   - Make sure your code actually uses the GPU/TPU (see example code).
   - Check if your data loading is slowing things down.

3. **Out of memory errors**:
   - Use smaller batches of data.
   - Simplify your model.
   - Try using lower precision numbers.

## Example Code

### GPU Example with PyTorch:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Check for GPU and use it if available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")

# Create a simple model
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
).to(device)  # This sends the model to the GPU

# Create some fake data for testing
x = torch.randn(64, 784).to(device)  # This sends the data to the GPU
y = torch.randint(0, 10, (64,)).to(device)

# Set up the training tools
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train for a few steps
for i in range(10):
    # Clear the gradients
    optimizer.zero_grad()
    
    # Forward pass
    outputs = model(x)
    loss = loss_function(outputs, y)
    
    # Backward pass
    loss.backward()
    optimizer.step()
    
    print(f"Step {i+1}, Loss: {loss.item():.4f}")
```

### TPU Example with PyTorch:

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch_xla.core.xla_model as xm
import torch_xla.distributed.parallel_loader as pl

# Check if TPU is available
device = xm.xla_device()
print(f"Using device: {device}")

# Create a simple model
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
).to(device)  # This sends the model to the TPU

# Create some fake data
x = torch.randn(64, 784).to(device)  # This sends the data to the TPU
y = torch.randint(0, 10, (64,)).to(device)

# Set up training tools
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train for a few steps
for i in range(10):
    # Clear the gradients
    optimizer.zero_grad()
    
    # Forward pass
    outputs = model(x)
    loss = loss_function(outputs, y)
    
    # Backward pass
    loss.backward()
    
    # This is important for TPU - it marks step completion
    xm.optimizer_step(optimizer)
    
    print(f"Step {i+1}, Loss: {loss.item():.4f}")
```

Remember: GPUs work well with PyTorch for most projects. TPUs require a special PyTorch library called `torch_xla` and are best for very large models or datasets.