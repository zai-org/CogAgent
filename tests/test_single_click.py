import importlib.util
import sys
import types
import unittest


def load_register():
    calls = []
    pag = types.ModuleType("pyautogui")
    pag.FAILSAFE = False
    pag.PAUSE = 0
    pag.click = lambda box: calls.append(("click", box))
    pag.doubleClick = lambda box: calls.append(("double", box))
    sys.modules["pyautogui"] = pag
    sys.modules["pyperclip"] = types.ModuleType("pyperclip")
    spec = importlib.util.spec_from_file_location("register", "app/register.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, calls


class SingleClickTest(unittest.TestCase):
    def test_a_click_is_a_single_click(self):
        module, calls = load_register()
        module.click({"box": (10, 20)})
        self.assertEqual(calls, [("click", (10, 20))])

    def test_a_double_click_stays_a_double_click(self):
        module, calls = load_register()
        module.double_click({"box": (10, 20)})
        self.assertEqual(calls, [("double", (10, 20))])


if __name__ == "__main__":
    unittest.main()
