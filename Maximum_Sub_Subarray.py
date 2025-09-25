def best_subarray_under_constraint(arr, constraint):
    if not arr or constraint <= 0:
        return None, 0, None, None
    
    left = 0
    current_sum = 0
    best_sum = 0
    best_range = None

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > constraint and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum > best_sum:
            best_sum = current_sum
            best_range = (left, right)

    if best_range is None:
        return None, 0, None, None
    
    start, end = best_range
    return arr[start:end+1], best_sum, start, end


test_cases = [
    {"desc": "Basic small array", "resources": [2, 1, 3, 4], "constraint": 5},
    {"desc": "Exact match to constraint", "resources": [2, 2, 2, 2], "constraint": 4},
    {"desc": "Single element equals constraint", "resources": [1, 5, 2, 3], "constraint": 5},
    {"desc": "All elements larger", "resources": [6, 7, 8], "constraint": 5},
    {"desc": "Multiple optimal subarrays", "resources": [1, 2, 3, 2, 1], "constraint": 5},
    {"desc": "Large window valid", "resources": [1, 1, 1, 1, 1], "constraint": 4},
    {"desc": "Sliding window shrink needed", "resources": [4, 2, 3, 1], "constraint": 5},
    {"desc": "Empty array", "resources": [], "constraint": 10},
    {"desc": "Constraint = 0", "resources": [1, 2, 3], "constraint": 0},
    {"desc": "Very large input (stress test)", "resources": list(range(1, 100001)), "constraint": 10**9},
]

for i, case in enumerate(test_cases, 1):
    subarray, total, start, end = best_subarray_under_constraint(case["resources"], case["constraint"])
    print(f"Test {i}: {case['desc']}")
    print("  Constraint:", case["constraint"])
    print("  Best Sum:", total)
    if subarray is None:
        print("  Best Subarray: None")
    else:
        preview = subarray if len(subarray) <= 15 else subarray[:15] + ["..."]
        print("  Best Subarray:", preview)
        print("  Start Index:", start, " End Index:", end)
    print()
