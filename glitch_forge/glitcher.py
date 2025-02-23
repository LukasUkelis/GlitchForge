from pathlib import Path
import sys
from typing import Callable
from glitch_forge import ui
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu


class Glitcher:
    window_title: str
    window: ui.GuiWindow
    app: QApplication
    window_icon: Path
    launch_func: Callable | None
    launch_button_label: str

    def __init__(
        self,
        window_title: str = ui.DEFAULT_WINDOW_TITLE,
        window_icon: Path = ui.DEFAULT_WINDOW_ICON,
        launch_func: Callable | None = None,
        launch_button_label: str = "Launch",
    ):
        self.window_title = window_title
        self.window_icon = window_icon
        self.launch_func = launch_func
        self.launch_button_label = launch_button_label

    def show_window(self) -> None:
        """
        Initializes and displays the main application window along with a system tray icon.
        This method sets up the QApplication, main window, and system tray icon. It also
        creates a context menu for the tray icon with options to show the main window and
        quit the application.
        """
        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon(str(self.window_icon)))
        self.window = ui.GuiWindow(
            window_title=self.window_title,
            window_icon=self.window_icon,
            param_class=self,
            launch_func=self.launch_func,
            launch_button_label=self.launch_button_label,
        )
        self.window.show()

        tray_icon = QSystemTrayIcon(QIcon(str(self.window_icon)), parent=self.app)
        menu = QMenu()
        quit_action = QAction("Quit", self.app)
        quit_action.triggered.connect(self.app.quit)

        show_action = QAction("Show", self.app)
        show_action.triggered.connect(self.window.activateWindow)
        menu.addAction(show_action)

        menu.addAction(quit_action)
        tray_icon.setContextMenu(menu)
        tray_icon.show()
        sys.exit(self.app.exec())
