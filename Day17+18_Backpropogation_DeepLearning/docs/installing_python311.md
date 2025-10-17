
# Installing Python 3.11

This guide outlines the steps to install Python 3.11 on **macOS**, **Linux**, and **Windows**.

---

## macOS

### Using Homebrew (recommended)
```sh
brew install python@3.11
````

To make it your default:

```sh
echo 'export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
```

### Verify

```sh
python3.11 --version
```

---

## Linux

### Debian/Ubuntu (apt)

```sh
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev
```

### Red Hat/Fedora

```sh
sudo dnf install -y python3.11
```

### From Source (all distros)

```sh
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev \
xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

cd /usr/src
sudo wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
sudo tar xvf Python-3.11.0.tgz
cd Python-3.11.0
sudo ./configure --enable-optimizations
sudo make -j "$(nproc)"
sudo make altinstall
```

### Verify

```sh
python3.11 --version
```

---

## Windows

1. Download the installer:
   [https://www.python.org/downloads/release/python-3110/](https://www.python.org/downloads/release/python-3110/)

2. Run the installer:

   * Select **"Add Python 3.11 to PATH"**
   * Choose **"Customize installation"** if needed
   * Click **Install Now**

3. After installation, open PowerShell or CMD:

```cmd
python --version
```

To ensure Python 3.11 runs:

```cmd
py -3.11
```

---

## Create a Virtual Environment

```sh
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```


