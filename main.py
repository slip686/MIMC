from PySide6.QtWidgets import QApplication
from widgets import main_window
import widgets.main_window
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = widgets.main_window.MainWindow()
    window.show()
    sys.exit(app.exec())
