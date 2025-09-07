# 📝 Macan Notes Pro

Macan Notes Pro is a modern note-taking app based on PyQt6, designed for a fast, clean, flexible, and professional writing experience.
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
<img width="799" height="598" alt="Screenshot 2025-09-07 201857" src="https://github.com/user-attachments/assets/1c6084a1-461e-4250-896b-d33dc174465f" />


---

## 🆕 Changelog v3.5.0
✨ Summary of New Features ✨

- Toolbar Underline: Added an Underline button to the toolbar, complete with a Ctrl+U shortcut and a status update as the cursor moves.

- Encoding Menu: Added an "Encoding" submenu within the "Format" menu. This feature allows you to reopen the active file with a different encoding scheme (for example, if the text appears messy). The active option will be adjusted to the current tab's encoding.

- Numbering/List: Added a ComboBox to the toolbar to select the list format (bulleted or numbered list). This functionality is also added as a "Numbering" submenu within the "Format" menu.

- Hyperlink Improvements: Improved the link detection logic when Ctrl+Clicking. The previous, less reliable method has been replaced with a new method that detects links based on the text formatting (color and underline) applied by the syntax highlighter, making it much more accurate and functional.

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
