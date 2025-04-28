# GlitchForge

**GlitchForge** is a lightweight Python library for building simple, responsive GUI applications in minutes. It is designed for rapid system development, testing, and prototyping, enabling you to easily expose parameters to the user and launch functions dynamically.

---

## Features

- 🔹 Automatically generate UI from class attributes
- 🔹 Supports basic types: `int`, `float`, `str`, `bool`
- 🔹 Launch any custom function via a button
- 🔹 System tray integration with Quick Actions
- 🔹 Built with **PyQt6** for modern UI experience

---

## Installation

```bash
pip install glitchforge
```
---

## Quick Start

Here's how easy it is to create a GUI with GlitchForge:

```python
from glitch_forge.glitcher import Glitcher
from glitch_forge.parameter import Param

class MyApp(Glitcher):
    param_a: Param = Param(10, int, "Parameter A")
    param_b: Param = Param(3.14, float, "Parameter B")
    param_c: Param = Param("Hello", str, "Parameter C")
    param_d: Param = Param(True, bool, "Parameter D")

    def __init__(self):
        super().__init__(
            launch_func=self.run,
            launch_button_label="Run",
            window_title="My Example App"
        )
        self.show_window()

    def run(self, base_class):
        print(base_class.param_a.val)
        print(base_class.param_b.val)
        print(base_class.param_c.val)
        print(base_class.param_d.val)

if __name__ == "__main__":
    import sys
    app = MyApp()
    sys.exit(app.app.exec())
```

---

## Documentation

### Core Classes

- **Glitcher**

  - Handles main window setup and system tray icon.
  - Parameters:
    - `launch_func` : Function called when the launch button is pressed.
    - `window_title` : Title of the window.
    - `window_icon` : Icon of the window and tray.
    - `launch_button_label` : Label for the launch button.

- **Param**

  - Represents a user-editable field.
  - Fields:
    - `val` : Default value.
    - `var_type` : Type of parameter (`int`, `float`, `str`, `bool`).
    - `label` : Label shown next to the input.
    - `min_val`, `max_val` : For numeric parameters.
    - `tooltip`, `placeholder` : Optional UI hints.

- **GuiWindow**

  - Internal class for constructing the UI.

### Supported Types

| Type  | Widget        |
| ----- | ------------- |
| int   | SpinBox       |
| float | DoubleSpinBox |
| str   | LineEdit      |
| bool  | CheckBox      |

### System Tray

- Tray icon supports:
  - "Show" : Focus application main window.
  - "Quit" : Exit the application.

---

## Project Structure

```
glitch_forge/
├── __init__.py
├── _version.py
├── glitcher.py
├── parameter.py
├── ui.py
├── icon.svg
├── example.py
```

---

## Requirements

- Python 3.10+
- PyQt6

---

## License

**MIT License**

Free to use, modify, and distribute.

---

## Screenshots

![image](https://github.com/user-attachments/assets/7e71103d-533d-410e-be04-03cc165c5f1d)

---

## Future Plans

- list[str], list[float] an list[int] type inputs
- Ability to perform launch function via tray icon

---

## Version

Current Version: `1.0.0`

*(See ****`_version.py`**** for details)*


