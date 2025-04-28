import sys
import time
from glitch_forge.glitcher import Glitcher
from glitch_forge.parameter import Param


class TestClass(Glitcher):
    # adding some parameters to our demo class(all parameters have different types)
    param_a: Param = Param(None, int, "param_a")
    param_b: Param = Param(None, float, "param_b")
    param_c: Param = Param(None, str, "param_c")
    param_d: Param = Param(None, bool, "param_d")

    def __init__(self):
        super().__init__(
            # assigning the function to be called when the button is pressed
            launch_func=test_function,
            # Setting custom launch button label
            launch_button_label="Print values",
            # Setting custom window title
            window_title="Test Window",
        )
        self.show_window()
        sys.exit(self.app.exec())


# This function will be called when the button is pressed
def test_function(base_class: TestClass):
    # This function will print the values of the parameters 20 times and then exits
    # It's useful to see ability to change values via GUI during runtime
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
    # creating demo class with a few parameters
    TestClass()
