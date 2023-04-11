### Maximum Sum of Contiguous Subarray (Kadane's Algorithm)

#### Requirements
-  Implement a function max_subarray(lst) that finds the contiguous subarray within the list that has: 
    - the largest sum
    - return the maximum sum
- The list will contain at most 10^5 (100_000) integers.
- Each integer in the list will be between -10^4 (-10_000) and 10^4 (10_000).
- The function should have a time complexity of O(n), where n is the length of the list.

#### Steps
- Create python virtual environment (assuming Linux): `python3 -m venv venv`
- For function implementation, at terminal run following command: `python maximum_subarray.py`.
- For function unittest, at terminal run the following command: `python test_max_subarray_function.py`
- For class implementation, at terminal run the following: `python maximum_subarray_class.py`

#### Implementation
- Implemented Kadane's algorithm to achieve 0(n) execution time for both style. Kadane's will iterate over array once.
- Implementation in two styles:
    - Function-based:
        - function at file `max_subarray_function.py`
        - unittest at file `test_max_subarray_function.py`

    - Class-based:
        - implement array generator to generate small random arrays and random arrays.
        - implement Kadane's which attribute array and get the maximum sum of contiguous sub array
        - 3 function to test cases (edge, small random array, random array)