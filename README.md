# 📝 Macan Notes Pro

Macan Notes Pro is a modern, feature-rich text/code editor based on PySide6 & Scintilla Engine — built for a fast, clean, flexible, and professional writing and scripting experience.
Now with an embedded script runner + terminal, AI chat assistant, speech-to-text, live Markdown/HTML preview, and full multi-language syntax highlighting.

> "Write smarter. Stay organized." ✨

## 📸 Screenshot
<img width="922" height="705" alt="Screenshot 2026-08-27 234729" src="https://github.com/user-attachments/assets/95b612b1-8169-4459-b9f3-cf987586f0f2" />

---

## ✨ Key Features

### 📑 Editing & Tabs
- **Multi-Tab Editing** — work on multiple files simultaneously in one window, with movable tabs.
- **Vertical Tab Panel** — optional resizable, drag-to-reorder sidebar tab list as an alternative to the top tab bar.
- **New Window** — open additional independent editor windows.
- **Autosave & Recovery** — notes are saved automatically with configurable Auto-Save Settings, and unsaved-changes are flagged with a tab badge indicator.
- **Session Restore** — reopens your previous tabs/files on next launch.
- **Find & Replace** — fast, accurate search across the document.
- **Go to Line** — jump straight to any line number.
- **Duplicate Line / Delete Line** — quick line-level editing shortcuts.
- **Insert Date/Time** and **Insert Horizontal Rule** helpers.
- **Word Count** dialog, plus optional live word count in the status bar.
- **Paste as Plain Text** to strip formatting on paste.

### 🖋️ Formatting
- **Font Customization** — choose font family and size, applied across all tabs.
- **Word Wrap** toggle.
- **Auto-Capitalization** toggle.
- **Smart Auto-Indent** toggle.
- **Bold / Italic / Underline** text styling with toolbar buttons and shortcuts.
- **Text Alignment** — left, center, right.
- **Bulleted & Numbered Lists**, selectable from the toolbar list combo or Format menu.
- **Case Conversion** — UPPERCASE, lowercase, and Title Case selection.
- **Encoding Menu** — choose the file's text encoding.

### 🎨 Themes & Appearance
- **Custom Themes** — Light, Dark, Neon Blue, Dark Blue, and Soft Pink, each with matched Scintilla syntax colors.
- **Dynamic Aura** — accent color adapts dynamically across the UI.
- **Frameless, Modern UI** — custom drag-and-drop titlebar and window chrome.
- **Distraction-Free Mode** (F11) — hide UI chrome for focused writing, with an Esc shortcut to exit.
- **Zoom In / Zoom Out / Restore Default Zoom** for editor text size.
- **Show/Hide Toolbar** and **Show/Hide Status Bar**.
- **Show Row Numbers** in the editor gutter.

### 🧩 Code Editing & Syntax Highlighting
Full syntax highlighting support for a wide range of languages:
- **Web:** HTML, CSS, JavaScript, PHP, XML, JSON, Markdown
- **Scripting:** Python, Ruby, Shell, Batch, PowerShell
- **Systems:** C/C++, Java, Rust
- **Data / Config:** SQL, YAML, TOML, INI
- **Misc:** Log files, Plain Text

Additional code tools:
- **Code Folding** — Fold All / Unfold All (Alt+0 / Alt+Shift+0).
- **Code Snippets Panel** — dockable panel with reusable snippets (e.g. Python main guard, for-loops, HTML boilerplate, Markdown tables), inserted via double-click.
- **Line Ending Conversion** — convert between Windows (CRLF) and Unix (LF).
- **Tabs ↔ Spaces Conversion**.
- **Column/Ruler Info** display.

### ▶️ Run & Debug Python Scripts
- **Run/Stop Python Scripts** directly from the editor (F5) — no need to leave the app.
- **Embedded Terminal Panel** — script output (stdout/stderr) streams live into a dockable terminal panel at the bottom of the window; no separate console/cmd window ever pops up.
- **Reliable Stop** — stopping a running script terminates the actual Python process (and its full process tree), not just a launcher stub.
- Terminal panel includes its own **Stop** and **Clear** controls, and reports the process exit code when finished.

### 🧹 Text Tools
- **Sort Lines** (A→Z / Z→A).
- **Remove Trailing Whitespace**.
- **Remove Blank Lines**.
- **Remove Duplicate Lines**.

### 🔍 File Comparison & Backup
- **Compare with Other File** — diff view with progress bar, row numbers, a change summary, and synchronized scrolling.
- **Create Backup** of the current file on demand.
- **Cache Manager** for managing app cache data.

### 👁️ Live Preview
- **Markdown & HTML Preview Panel** — dockable live preview, toggleable from the toolbar or View menu.

### 🤖 AI & Productivity
- **AI Copilot Panel** — integrated AI chat assistant dockable panel for writing and coding help.
- **Speech-to-Text** — dictate directly into the editor via an external speech engine, toggled from the toolbar.

### 📂 File Management
- Broad file type support with smart filtering, including: `.txt`, `.py`/`.pyw`, `.md`, `.html`/`.htm`, `.css`, `.js`/`.jsx`/`.ts`/`.tsx`, `.json`, `.xml`, `.yaml`/`.yml`, `.toml`, `.ini`/`.cfg`/`.conf`, `.sql`, `.c`/`.cpp`/`.h`/`.hpp`/`.cs`, `.java`/`.kt`, `.sh`/`.bash`/`.zsh`, `.ps1`, `.bat`/`.cmd`, `.php`, `.rs`, `.rb`, `.docx`, `.log`, and more.
- **Recent Files** list with Clear option.
- **Print** and **Export to PDF**.
- **Single-Instance / "Open With" Support** — opening a file while the app is already running sends it to the existing window instead of launching a duplicate instance.

### 🔄 Updates
- **Check for Updates** from within the app.

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
```
