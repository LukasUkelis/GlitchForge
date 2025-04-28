import pytestqt.qtbot
import pytest

from glitch_forge.glitcher import Glitcher
from glitch_forge.parameter import Param
from glitch_forge.ui import Worker


class TestClass(Glitcher):
    # adding some parameters to our demo class(all parameters have different types)
    param_a: Param = Param(None, int, "param_a")
    param_b: Param = Param(None, float, "param_b")
    param_c: Param = Param(None, str, "param_c")
    param_d: Param = Param(None, bool, "param_d")

    param_a2: Param = Param(1, int, "param_a1")
    param_b2: Param = Param(2.0, float, "param_b1")
    param_c2: Param = Param("Test", str, "param_c1")
    param_d2: Param = Param(True, bool, "param_d1")

    param_a3: Param = Param(True, dict, "param_a3")

    def __init__(self, launch_func=None):
        super().__init__(launch_func=launch_func)


def function_test(base_class: TestClass):
    print("Test function called")
    print(f"param_a: {base_class.param_a.val}")
    print(f"param_b: {base_class.param_b.val}")
    print(f"param_c: {base_class.param_c.val}")
    print(f"param_d: {base_class.param_d.val}")


@pytest.fixture
def main_window(qtbot: pytestqt.qtbot.QtBot):
    window: TestClass = TestClass(function_test)
    window.show_window()
    qtbot.addWidget(window.window)
    assert window.window.isVisible()
    assert window.window.isEnabled()
    yield window


def test_main_window(qtbot: pytestqt.qtbot.QtBot, main_window: TestClass):
    main_window.window.btn_launch.click()
    main_window.window.close()
    qtbot.waitExposed(main_window.window)


def test_worker():
    params_class = TestClass()
    worker = Worker(function_test, params_class)
    worker.run()
