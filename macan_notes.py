# Nama file: macan_notes.py
# Jalankan dengan perintah: python macan_notes.py

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QStatusBar,
    QMenu,
    QMenuBar
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class MacanNotes(QMainWindow):
    """
    Kelas utama untuk aplikasi text editor 'Macan Notes'.
    """
    def __init__(self):
        super().__init__()

        # Inisialisasi properti jendela
        self.current_file = None
        self.setWindowTitle("Macan Notes")
        self.setGeometry(100, 100, 800, 600)

        # Membuat area teks utama
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Membuat menu bar dan status bar
        self.create_menu_bar()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def create_menu_bar(self):
        """
        Membuat menu bar dengan aksi-aksi file.
        """
        menu_bar = self.menuBar()

        # Membuat menu 'File'
        file_menu = menu_bar.addMenu("&File")

        # Membuat aksi 'New'
        new_action = QAction("&New", self)
        new_action.triggered.connect(self.new_file)
        new_action.setShortcut("Ctrl+N")
        file_menu.addAction(new_action)

        # Membuat aksi 'Open'
        open_action = QAction("&Open...", self)
        open_action.triggered.connect(self.open_file)
        open_action.setShortcut("Ctrl+O")
        file_menu.addAction(open_action)

        # Membuat aksi 'Save'
        save_action = QAction("&Save", self)
        save_action.triggered.connect(self.save_file)
        save_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_action)

        # Menambahkan pemisah
        file_menu.addSeparator()

        # Membuat aksi 'Exit'
        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut("Ctrl+Q")
        file_menu.addAction(exit_action)

    def new_file(self):
        """
        Membuat file baru.
        """
        # Memeriksa apakah ada perubahan yang belum disimpan
        if self.text_edit.document().isModified():
            response = QMessageBox.warning(
                self,
                "Unsaved Changes",
                "Do you want to save the current file?",
                QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
            )
            if response == QMessageBox.StandardButton.Save:
                self.save_file()
            elif response == QMessageBox.StandardButton.Cancel:
                return

        self.text_edit.clear()
        self.current_file = None
        self.setWindowTitle("Macan Notes - New File")
        self.status_bar.showMessage("New file created")

    def open_file(self):
        """
        Membuka file dari dialog.
        """
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    self.text_edit.setText(content)
                    self.current_file = file_name
                    self.setWindowTitle(f"Macan Notes - {self.current_file}")
                    self.status_bar.showMessage(f"File '{file_name}' opened")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {e}")
                self.status_bar.showMessage("Failed to open file")

    def save_file(self):
        """
        Menyimpan file ke lokasi yang dipilih.
        """
        # Jika file belum pernah disimpan, panggil 'Save As'
        if not self.current_file:
            self.save_as_file()
        else:
            try:
                with open(self.current_file, 'w') as file:
                    file.write(self.text_edit.toPlainText())
                self.text_edit.document().setModified(False)
                self.status_bar.showMessage(f"File '{self.current_file}' saved")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {e}")
                self.status_bar.showMessage("Failed to save file")

    def save_as_file(self):
        """
        Menyimpan file ke lokasi baru.
        """
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save File As",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            self.current_file = file_name
            self.save_file()


# Blok utama untuk menjalankan aplikasi
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = MacanNotes()
    editor.show()
    sys.exit(app.exec())
