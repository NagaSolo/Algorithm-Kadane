import random
from typing import List

class RandomCase:
    """ Generate random or small array list, 'small' will return array maximum 15 items.
        Whilst 'random' will return items up to 1000_000 items

        Small testcase:
            case1 = RandomCase('small')
        
        Random testcase:
            case1 = RandomCase('random')
    
    """
    def __init__(self, option: str):
        self.option = option
        self.array = self._generate_array()

    def _generate_random_testcase(self):
        testcase = []
        list_length = random.randint(1, 10e5)
        for _ in range(0, list_length):
            possible_number = random.randint(-10e4, 10e4 + 1)
            testcase.append(possible_number)
        return testcase

    def _generate_small_testcase(self):
        testcase = []
        list_length = random.randint(1, 15)
        for _ in range(0, list_length):
            possible_number = random.randint(-10e4, 10e4 + 1)
            testcase.append(possible_number)
        return testcase
    
    def _generate_array(self):
        if self.option == 'small':
            return self._generate_small_testcase()
        elif self.option == 'random':
            return self._generate_random_testcase()
        else:
            print("Pass 'small' or 'random' to option")


class KadaneAlgorithm:
    """ Kadane's algorithm implementation to solve sum of contiguous subarray

        Array length up to 1_000_000
        Item will consist of integer between -100_000 up to 100_000
    """
    def __init__(self, array: List[int]) -> int:
        self.array = array
        
    def maximum_subarray(self):
       max_sum = -10e4 # minimum value that test case will cover
       curr_sum = 0

       for i in range(len(self.array)):
           curr_sum = curr_sum + self.array[i]
           if(curr_sum > max_sum):
               max_sum = curr_sum
           if(curr_sum < 0):
               curr_sum = 0
      
       return max_sum
    

def test_edge_case():
    """ To test edge cases that I could possibly imagine """

    print('TESTING EDGE CASES\n')
    t1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    t2 = [1, 3, 8, -2, 6, -8, 5]
    t3 = [-10e5]
    t4 = [1, 2, 3, 4, 5]
    t5 = [-1, -2, -3, -4, -5]

    for t in [t1, t2, t3, t4, t5]:
        test_t = KadaneAlgorithm(t).maximum_subarray()
        print(f"For array {t}, maximum contiguous array is: {test_t}")
        print('\n')

def test_small_generated():
    """ To test small list of generated test cases """
    
    print('TESTING SMALL GENERATED ARRAY CASES\n')
    for _ in range(10):
        temp_array = RandomCase('small').array
        test_temp_array = KadaneAlgorithm(temp_array).maximum_subarray()
        print(f"For array {temp_array}, maximum contiguous array is: {test_temp_array}")
        print('\n')

def test_random_generated():
    """ To test random list of generated test cases """
    
    print('TESTING RANDOM GENERATED ARRAY CASES\n')
    for _ in range(10):
        temp_array = RandomCase('random').array
        test_temp_array = KadaneAlgorithm(temp_array).maximum_subarray()
        print(f"For array {temp_array}, maximum contiguous array is: {test_temp_array}")
        print('\n')

def main():
    """ Run all tests """
    test_edge_case()
    print('\n')
    test_small_generated()
    print('\n')

if __name__ == "__main__":
    main()