import importlib.util
import os
import sys

test_cases_dir = os.path.abspath(os.path.join(os.getcwd(), "dataset/test_cases"))
if test_cases_dir not in sys.path:
    sys.path.insert(0, test_cases_dir)


def str_to_func(code_str):
    local_vars = {}
    exec(code_str, globals(), local_vars)
    Solution = local_vars["Solution"]
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
    test_cases = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_cases)
    passed, total, accuracy = test_cases.calculate_accuracy(soln_func)
    print(f"Accuracy: {accuracy:.1f}% ({passed}/{total})")
    print(f"Passed: {passed}/{total} ({accuracy:.1f}%)")
