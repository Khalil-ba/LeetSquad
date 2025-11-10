import importlib.util
import os
import sys
from typing import *

test_cases_dir = os.path.abspath(os.path.join(os.getcwd(), "dataset/test_cases"))
if test_cases_dir not in sys.path:
    sys.path.insert(0, test_cases_dir)

# Aggregate helpers from dataset test utils and consolidated testcase_utils
_UTILS_DICT: dict = {}


def _safe_load_module(name: str, path: str) -> None:
    try:
        if not os.path.exists(path):
            return
        spec = importlib.util.spec_from_file_location(name, path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # type: ignore[attr-defined]
            for k, v in module.__dict__.items():
                if not k.startswith("__"):
                    _UTILS_DICT[k] = v
    except Exception:
        # Keep going; missing utils will surface during test run
        pass


_safe_load_module(
    "testcase_utils",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "testcase_utils.py")),
)

# Make helpers available to exec(code_str, globals(), ...)
globals().update(_UTILS_DICT)


def str_to_func(code_str):
    local_vars = {}
    exec(code_str, globals(), local_vars)
    Solution = local_vars.get("Solution") or globals().get("Solution")
    if Solution is None:
        raise ValueError("No class 'Solution' found in generated code")
    method_name = [
        name
        for name in dir(Solution)
        if callable(getattr(Solution, name)) and not name.startswith("__")
    ][0]
    soln_func = getattr(Solution(), method_name)
    return soln_func


def test_accuracy(task_id: str, soln_func):
    spec = importlib.util.spec_from_file_location(
        task_id, os.path.join(test_cases_dir, f"{task_id}.py")
    )
    if spec is None or spec.loader is None:
        raise FileNotFoundError(f"Test case not found for task_id: {task_id}")
    test_cases = importlib.util.module_from_spec(spec)
    # Inject helpers before executing the test module so missing imports don't break
    if _UTILS_DICT:
        test_cases.__dict__.update(_UTILS_DICT)
    spec.loader.exec_module(test_cases)  # type: ignore[attr-defined]
    if not hasattr(test_cases, "calculate_accuracy"):
        raise AttributeError(
            f"Test case module for '{task_id}' lacks 'calculate_accuracy'"
        )
    return test_cases.calculate_accuracy(soln_func)
