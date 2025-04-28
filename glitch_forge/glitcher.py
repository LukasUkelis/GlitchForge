from pathlib import Path
import sys
from typing import Callable
from glitch_forge import ui
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu


class Glitcher:
    """Glitcher is a class responsible for managing the main application window and system tray icon
    for a GUI-based application. It provides functionality to initialize and display the main
    window, set up a system tray icon with a context menu, and handle application launch behavior.
    Attributes:
        window_title (str): The title of the main application window.
        window (ui.GuiWindow): The main application window instance.
        app (QApplication): The QApplication instance managing the GUI application.
        window_icon (Path): The path to the icon used for the window and system tray.
        launch_func (Callable | None): An optional function to be executed when the launch button is clicked.
        launch_button_label (str): The label text for the launch button.
    Methods:
        __init__(window_title, window_icon, launch_func, launch_button_label):
            Initializes the Glitcher instance with the specified parameters.
        show_window():
            Sets up the QApplication, main window, and system tray icon, and creates a context
            menu for the tray icon with options to show the main window and quit the application."""

    window_title: str
    """The title of the main application window"""
    window: ui.GuiWindow
    """The main application window instance"""
    app: QApplication
    """The QApplication instance managing the GUI application"""
    window_icon: Path
    """The path to the icon used for the window and system tray"""
    launch_func: Callable
    """An optional function to be executed when the launch button is clicked"""
    launch_button_label: str
    """The label text for the launch button"""

    def __init__(
        self,
        launch_func: Callable,
        launch_button_label: str = "Launch",
        window_title: str = ui.DEFAULT_WINDOW_TITLE,
        window_icon: Path = ui.DEFAULT_WINDOW_ICON,
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
