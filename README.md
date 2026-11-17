# Student Record Search System (DAA Project)

**Main algorithm:** Iterative Binary Search  
**Language:** Python 3  
**Storage:** JSON file  
**External libraries:** None

## Project features
- Add a student record
- View all student records
- Search a student by ID using Binary Search
- Update a student record
- Delete a student record
- Save records automatically in `students.json`
- Display Binary Search steps and number of comparisons

## How to run in Windows / VS Code
1. Install Python 3 if it is not already installed.
2. Extract the project ZIP into a folder.
3. Open that folder in VS Code (`File > Open Folder`).
4. Open the VS Code terminal (`Terminal > New Terminal`).
5. Run `python main.py`. If that command does not work, try `py main.py`.

## Important
Keep `main.py`, `binary_search.py`, `student_operations.py`, and `students.json` in the same folder. Do not rename or move `students.json` separately. The records are sorted by Student ID before Binary Search is performed.

## Binary Search algorithm
1. Set `low = 0` and `high = number of records - 1`.
2. Find the middle index: `mid = (low + high) // 2`.
3. If the middle Student ID equals the target, the record is found.
4. If the middle ID is smaller, continue in the right half (`low = mid + 1`).
5. Otherwise, continue in the left half (`high = mid - 1`).
6. Repeat until the record is found or `low > high`.

## Complexity
- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)
- Auxiliary space: O(1)

Binary Search requires the records to be sorted by Student ID. This project keeps them sorted after adding, updating, or deleting records.
