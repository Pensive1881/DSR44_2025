# Setting Up the Practical Computer Vision Repository with a Dev Container

This guide explains how to set up the Practical Computer Vision repository using a [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers), both locally in VS Code, PyCharm, or Cursor, and in a [GitHub Codespace](https://github.com/features/codespaces). Dev containers provide a consistent and isolated environment for development, ensuring that everyone working on the project has the same tools and dependencies.

**Important:** This dev container image is designed for inference tasks and does not include support for GPUs or hardware accelerators. If want to run the code samples that train neural networks consider using a cloud-based environment like [Kaggle](https://www.kaggle.com/kernels) or [Google Colab](https://colab.research.google.com/), which provide free access to GPUs.

## Prerequisites

*   **VS Code/PyCharm/Cursor:**
    *   [VS Code](https://code.visualstudio.com/) with the [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    *   [PyCharm](https://www.jetbrains.com/pycharm/) with the [Remote Development](https://www.jetbrains.com/pycharm/features/remote-development/) feature.
    *   [Cursor](https://cursor.sh/) which supports dev containers natively.
*   **Docker:** [Install Docker](https://docs.docker.com/get-docker/) on your local machine.
*   **GitHub Account:** Required for using GitHub Codespaces.

## Local Setup (VS Code/PyCharm/Cursor)

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/andandandand/practical-computer-vision.git
    cd practical-computer-vision
    ```

2.  **Open in VS Code/PyCharm/Cursor:**

    *   **VS Code:** Open the cloned repository in VS Code. If you have the Remote - Containers extension installed, VS Code will detect the `.devcontainer/devcontainer.json` file and prompt you to reopen the project in a container. Click "Reopen in Container".
    *   **PyCharm:** Open the cloned repository in PyCharm. Configure the remote development environment to use the Dockerfile in the repository.
    *   **Cursor:** Open the cloned repository in Cursor. Cursor should automatically detect the `.devcontainer/devcontainer.json` file and offer to open the project in the dev container.



3.  **Build the Dev Container:**

    VS Code/PyCharm/Cursor will now build the dev container. This may take some time, as it needs to download the base image and install all the necessary dependencies.  The `postCreateCommand` in `.devcontainer/devcontainer.json` will run `pip install --no-cache-dir -r requirements.txt` after the container is created.

4.  **Access the Dev Container:**

    Once the dev container is built, VS Code/PyCharm/Cursor will automatically connect to it. You can now work on the project as if you were working on your local machine, but with all the dependencies and tools pre-configured.

## GitHub Codespaces Setup

1.  **Create a New Codespace:**

    *   Go to the repository on GitHub: <https://github.com/andandandand/practical-computer-vision>
    *   Click the "Code" button, then select the "Codespaces" tab.
    *   Click "Create codespace on main".

2.  **Codespace Configuration:**

    GitHub Codespaces will automatically detect the `.devcontainer/devcontainer.json` file in the repository and use it to configure the development environment.

3.  **Wait for Setup:**

    GitHub Codespaces will build the dev container, which may take a few minutes.

4.  **Access the Codespace:**

    Once the dev container is built, you will be automatically connected to the Codespace in your browser. You can also connect to the Codespace using VS Code for a richer development experience.

## Using the Dev Container

Whether you are using a local dev container or a GitHub Codespace, the development experience is the same.

*   **Python Interpreter:** The Python interpreter is pre-configured to use the virtual environment located at [python](http://_vscodecontentref_/0) as specified in `.devcontainer/devcontainer.json`.
*   **FiftyOne:** The [FiftyOne](https://voxel51.com/fiftyone/) library is pre-installed.
*   **Git:** Git is pre-installed and configured, as specified by the `"ghcr.io/devcontainers/features/git:1"` feature in `.devcontainer/devcontainer.json`. This dev container includes an up-to-date version of Git, built from source as needed, pre-installed and available on the `PATH`.
*   **VS Code Extensions:**  The recommended VS Code extensions are automatically installed, as listed in the `extensions` section of the `.devcontainer/devcontainer.json` file.  This includes `github.copilot` and `github.copilot-chat`.
*   **Linting and Formatting:**  The devcontainer is configured with linting and formatting tools such as `pylint`, `flake8`, `black`, and `autopep8`.

## Key Files

*   `.devcontainer/devcontainer.json`: This file defines the dev container configuration, including the Docker image to use, the extensions to install, and the settings to apply.
*   `requirements.txt`: This file lists the Python dependencies required for the project.

## Troubleshooting

*   **Container Build Errors:** If you encounter errors during the container build process, check the Docker logs for more information.  Common issues include network connectivity problems or missing dependencies.
*   **VS Code Connection Issues:** If VS Code fails to connect to the dev container, try restarting VS Code or rebuilding the container.
*   **GitHub Codespaces Issues:** If you encounter issues with GitHub Codespaces, check the GitHub status page for any known outages.

