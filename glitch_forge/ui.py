from contextlib import suppress
from dataclasses import dataclass
from typing import Callable
from PyQt6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QCheckBox,
    QWidget,
    QPushButton,
)
from glitch_forge import parameter
from PyQt6.QtGui import QIcon
from pathlib import Path
from PyQt6.QtCore import QThread


THIS_DIR = Path(__file__).resolve().parent
DEFAULT_WINDOW_TITLE = "GlitchForge"
DEFAULT_WINDOW_ICON = THIS_DIR / "icon.svg"


class Worker(QThread):
    """
    A QThread-based worker class that executes a given function with a parameter object
    in a separate thread.
    Attributes:
        func (Callable): The function to be executed in the thread.
        param_class (object): The parameter object to be passed to the function.
    Methods:
        __init__(func: Callable, param_class: object):
            Initializes the Worker with the specified function and parameter object.
        run():
            Executes the function with the parameter object and emits the `finished` signal upon completion.
    """

    func: Callable
    """The function to be executed in the thread"""
    param_class: object
    """The parameter object to be passed to the function"""

    def __init__(self, func: Callable, param_class: object):
        super().__init__()

        self.func = func
        self.param_class = param_class

    def run(self):
        self.func(self.param_class)
        self.finished.emit()


@dataclass
class Input:
    label_widget: QLabel
    input_widget: QWidget


class GuiWindow(QMainWindow):
    lay: QVBoxLayout
    """Main layout of the window"""
    inputs: dict[str, Input] = {}
    """Dictionary to store parameter inputs"""
    param_class: object
    """Class containing parameters all parameters that needs to be displayed in a GUI"""
    launch_func: Callable | None
    """Function to be executed when the launch button is clicked"""
    launch_button_label: str
    """Label for the launch button"""
    btn_launch: QPushButton
    """Button to launch the function"""
    worker: Worker
    """Worker thread for executing the function"""

    def __init__(
        self,
        param_class: object,
        launch_func: Callable | None = None,
        launch_button_label: str = "Launch",
        window_title=DEFAULT_WINDOW_TITLE,
        window_icon=DEFAULT_WINDOW_ICON,
    ):
        super().__init__()
        self.param_class = param_class
        self.launch_func = launch_func
        self.launch_button_label = launch_button_label

        self.setWindowTitle(window_title)
        self.setWindowIcon(QIcon(str(window_icon)))

        # Create a central widget and set its layout
        central_widget = QWidget()
        self.lay = QVBoxLayout(central_widget)
        self.lay.addLayout(self.param_inputs())
        self.lay.addStretch()
        self.lay.addLayout(self.actions_layout())
        self.setCentralWidget(central_widget)

    def param_inputs(self) -> QVBoxLayout:
        """Layout for the parameter inputs"""
        layout = QVBoxLayout()
        for attr_name in self.param_class.__annotations__:
            with suppress(AttributeError):
                attr = getattr(self.param_class, attr_name)
                if isinstance(attr, parameter.Param):
                    try:
                        h_layout, label, widget = self.get_input_by_param(attr)
                        self.inputs[attr_name] = Input(label, widget)
                        layout.addLayout(h_layout)
                    except ValueError as e:
                        print(f"Error creating input for {attr_name}: {e}")
                        continue
        return layout

    def actions_layout(self) -> QHBoxLayout:
        """Layout for the action buttons (Launch)"""
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        self.btn_launch = QPushButton(self.launch_button_label)
        self.btn_launch.setMinimumHeight(20)
        self.btn_launch.setMinimumWidth(100)
        self.btn_launch.setStyleSheet(
            """
        QPushButton {
            background-color: green;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #32cd32; /* lighter green on hover */
        }
        """
        )
        self.btn_launch.clicked.connect(self.start_func)
        h_layout.addWidget(self.btn_launch)
        return h_layout

    def start_func(self) -> None:
        """Function to be called when the launch button is clicked."""
        self.btn_launch.setEnabled(False)
        self.worker = Worker(self.launch_func, self.param_class)
        self.worker.setObjectName("worker")
        self.worker.finished.connect(self.worker_finished)
        self.worker.start()

    def worker_finished(self):
        """Function to be called when the worker thread finishes."""
        self.worker.deleteLater()
        self.btn_launch.setEnabled(True)

    @staticmethod
    def get_input_by_param(
        param: parameter.Param,
    ) -> tuple[QHBoxLayout, QLabel, QWidget]:
        """Function to create the appropriate input widget based on the parameter type."""
        h_layout = QHBoxLayout()

        # Create a label for the parameter; use an empty string if label is None
        label = QLabel(param.label if param.label else "")
        h_layout.addWidget(label)

        # Create the appropriate input widget based on param.var_type
        if param.var_type is int:
            widget = QSpinBox()
            if param.val is not None:
                widget.setValue(param.val)
            widget.setMinimum(
                param.min_val if param.min_val is not None else -2147483648
            )
            widget.setMaximum(
                param.max_val if param.max_val is not None else 2147483647
            )
            widget.valueChanged.connect(lambda val: setattr(param, "val", val))
        elif param.var_type is float:
            widget = QDoubleSpinBox()
            if param.val is not None:
                widget.setValue(param.val)
            widget.setMinimum(
                param.min_val if param.min_val is not None else -2147483648
            )
            widget.setMaximum(
                param.max_val if param.max_val is not None else 2147483647
            )
            widget.valueChanged.connect(lambda val: setattr(param, "val", val))
        elif param.var_type is str:
            widget = QLineEdit()
            if param.val is not None:
                widget.setText(param.val)
            widget.textChanged.connect(lambda text: setattr(param, "val", text))
        elif param.var_type is bool:
            widget = QCheckBox()
            if param.val is not None:
                widget.setChecked(param.val)
            widget.toggled.connect(lambda state: setattr(param, "val", state))
        else:
            raise ValueError(f"Unsupported type {param.var_type}")

        h_layout.addWidget(widget)
        return h_layout, label, widget
