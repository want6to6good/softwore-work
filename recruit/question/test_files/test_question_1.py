# test_question_1.py

import sys
import importlib.util
from typing import List  # 添加这行


def load_solution(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    solution_module = importlib.util.module_from_spec(spec)
    # 在执行模块之前，确保 List 是可用的
    solution_module.List = List
    
    spec.loader.exec_module(solution_module)
    return solution_module.Solution()


def run_tests(solution):
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.twoSum(nums, target)
        passed = result == expected
        all_passed &= passed

        # print(f"Test case {i}:")
        # print(f"Input: nums = {nums}, target = {target}")
        # print(f"Output: {result}")
        # print(f"Expected: {expected}")
        # print(f"{'Passed' if passed else 'Failed'}")
        # print()

    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_question_1.py <solution_file_path>")
        sys.exit(1)

    solution_filepath = sys.argv[1]
    solution = load_solution(solution_filepath)
    run_tests(solution)
