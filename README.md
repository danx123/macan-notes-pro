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
<img width="745" height="681" alt="Screenshot 2025-10-29 225338" src="https://github.com/user-attachments/assets/0513d995-594d-45c0-8543-0c744b655096" />
<img width="742" height="544" alt="Screenshot 2025-10-29 225400" src="https://github.com/user-attachments/assets/b590bc2b-6117-413c-9106-a459a4f4c3a3" />

---

## 🆕 Changelog v5.0.0
🚀 New Features
Added "Paste as Plain Text" Action:

Introduced a new "Paste as Plain Text" feature, accessible from the Edit menu or via the Ctrl+Shift+V shortcut.

This allows users to paste content from the clipboard while stripping all external formatting.

This resolves an issue where content pasted from external sources (like web browsers) would retain its original styling (e.g., black text in a dark theme), ensuring pasted text always respects the application's current theme.

🛠️ Improvements & Fixes
Enabled Rich Text Formatting Persistence for HTML:

Modified the file I/O logic to provide support for saving and loading rich text formatting (e.g., bold, italics, lists, and text alignment).

Save Logic: The application now serializes the editor's content to HTML when the file extension is .html or .htm. All other formats are saved as plain text as before.

Load Logic: The application now correctly deserializes .html and .htm files, restoring all rich text formatting when a file is opened.

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
