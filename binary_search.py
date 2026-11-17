"""Binary Search implementation for Student Record Search System."""


def binary_search_student(students, target_id):
    """Find a student by ID in a list sorted by student_id.

    Returns (student_or_none, comparisons, trace).
    Time complexity: O(log n); auxiliary space: O(1).
    """
    low = 0
    high = len(students) - 1
    comparisons = 0
    trace = []

    while low <= high:
        mid = (low + high) // 2
        current_id = int(students[mid]["student_id"])
        comparisons += 1
        trace.append(
            f"low={low}, high={high}, mid={mid}, checked ID={current_id}"
        )

        if current_id == target_id:
            return students[mid], comparisons, trace
        if current_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None, comparisons, trace
