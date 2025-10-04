# 📝 Macan Notes Pro

Macan Notes Pro is a modern note-taking app based on PySide6, designed for a fast, clean, flexible, and professional writing experience.
Now available with font customization and syntax highlighting for Python

> "Write smarter. Stay organized." ✨

---

## ✨ Key Features
- 📑 Multi-Tab Notes — write multiple notes simultaneously in one window.
- 💾 Autosave & Recovery — notes are automatically saved, preventing crashes.
- 🔍 Find & Replace — fast and accurate text search.
- 🖋️ Font Customization — choose your preferred font type and size.
- 🎨 Custom Themes — support for dark, light, neon blue, dark blue, and soft pink themes.
- 📂 **File Management** — supports `.txt`, `.md`, `.py`, `.html` with automatic filtering.
- 🧩 **Syntax Highlighting (Python)** — Python code is displayed in color, making it easier to read.
- 🧹 **Modern & Frameless UI** — clean design with custom drag-and-drop windows.

---

## 📸 Screenshot
<img width="862" height="707" alt="Screenshot 2025-10-05 011053" src="https://github.com/user-attachments/assets/a700bb1d-22b0-4d9c-82c0-de870b3a7bb8" />
<img width="882" height="699" alt="Screenshot 2025-10-05 014935" src="https://github.com/user-attachments/assets/329e9946-690b-4175-a56f-a445ed8d7937" />
<img width="883" height="702" alt="Screenshot 2025-10-05 015010" src="https://github.com/user-attachments/assets/5eb40f80-bbcc-4fe7-8fed-9bcd172d534d" />



---

## 🆕 Changelog v4.0.0
✨ Summary of New Features ✨
* Added a Run button to execute the currently opened .py script using the method

* Added dynamic aura:
- If the opened file is a .txt file, the theme is automatically light/dark
- If the opened file is a .md file, the theme is automatically soft pink
- If the opened file is a .py file, the theme is automatically neon blue
- If the opened file is a .html file, the theme is automatically dark blue

* Added a code snippet button next to the run button and brings up a QDockWidget/side panel with QListView/QListWidget
---

## 📦 Release Notes
- **Source Code (this repo):** contains the **initial version/baseline** of Macan Notes Pro.
- **Release (Binary):** contains the **latest version (2.0.0)** ready to use.

👉 So, to try the latest version of the application directly, please download the **binary release** from the [Releases](../../releases) page.

---

## 🛠️ Installation (from Source)
### Prerequisites
- Python 3.10+
- Python Dependencies:
```bash
pip install -r requirements.txt
