# test_question_2.py

import sys
import importlib.util


def load_solution(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    return solution_module.Solution()


def run_tests(solution):
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.lengthOfLongestSubstring(s)
        passed = result == expected
        all_passed &= passed

        # print(f"Test case {i}:")
        # print(f"Input: s = \"{s}\"")
        # print(f"Output: {result}")
        # print(f"Expected: {expected}")
        # print("Explanation: " + get_explanation(s, result))
        # print(f"{'Passed' if passed else 'Failed'}")
        # print()

    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_question_2.py <solution_file_path>")
        sys.exit(1)

    solution_filepath = sys.argv[1]
    solution = load_solution(solution_filepath)
    run_tests(solution)
