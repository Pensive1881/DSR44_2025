# How to Add a Shortcut to a Google Drive Folder

Adding a shortcut from a shared Google Drive folder to your own account allows you fast access to the data without having to download it.

Follow these steps to add a shortcut to a shared Google Drive folder in your own Drive for quick access. 

---

## 1. Open Google Drive

- Go to [drive.google.com](https://drive.google.com) and sign in with your Google account if you are not already signed in.

## 2. Locate the Shared Folder

- Find the folder you want to add a shortcut to. If someone shared it with you, look under the **"Shared with me"** section on the left sidebar.

## 3. Add the Shortcut

- Right-click (or two-finger click on a touchpad) the folder.
- Select **Organize > Add shortcut to Drive** from the menu.

## 4. Choose Shortcut Location

- A dialog box will appear. Select **My Drive** or any other folder in your Drive where you want the shortcut to appear.
- Click **Add shortcut** to confirm.

## 5. Access Your Shortcut

- Go to the location you selected (e.g., "My Drive").
- You will see the shortcut there, marked with a small arrow icon.
- You will be able to refer to this folder using the path specified: 

```python
from pathlib import Path
import os
path = Path("/gdrive/MyDrive/<folder_name>")
# This should print the filenames inside the folder
os.listdir(path)
``` 

---

**Tip:**  
Shortcuts are just pointers to the original folder-they do not make a copy or use your storage quota. Any changes you make to files within the shortcut are reflected in the original folder.

