import time
from glitch_forge.glitcher import Glitcher
from glitch_forge.parameter import Param


class TestClass(Glitcher):
    param_a: Param = Param(None, int, "param_a")
    param_b: Param = Param(None, float, "param_b")
    param_c: Param = Param(None, str, "param_c")
    param_d: Param = Param(None, bool, "param_d")

    def __init__(self):
        super().__init__(
            launch_func=test_function,
            launch_button_label="Print values",
            window_title="Test Window",
        )
        self.show_window()


def test_function(base_class: TestClass):
    # This function will be called when the button is pressed
    iterations = 20
    for i in range(20):
        print(f"{base_class.param_a.val=}")
        print(f"{base_class.param_b.val=}")
        print(f"{base_class.param_c.val=}")
        print(f"{base_class.param_d.val=}")
        print("-" * 20)
        print("Trie to change values via GUI")
        print(f"({i + 1}/{iterations})Sleeping for 2 seconds...")
        time.sleep(2)
        print("-" * 20)


if __name__ == "__main__":
    TestClass()
