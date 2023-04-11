import random
random.randint(0, 9)

def generate_random_testcase():
    testcase = []
    list_length = random.randint(1, 10e5)
    for _ in range(0, list_length):
        possible_number = random.randint(-10e4, 10e4 + 1)
        testcase.append(possible_number)
    return testcase

def generate_small_testcase():
    testcase = []
    list_length = random.randint(1, 15)
    for _ in range(0, list_length):
        possible_number = random.randint(-10e4, 10e4 + 1)
        testcase.append(possible_number)
    return testcase

def maximum_subarray(array: list) -> int:
       maxSum = -10e4
       currSum = 0

       for i in range(len(array)):
           currSum = currSum + array[i]
           if(currSum > maxSum):
               maxSum = currSum
           if(currSum < 0):
               currSum = 0
      
       return maxSum

if __name__ == "__main__":
    t1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    t2 = [1, 3, 8, -2, 6, -8, 5]
    t3 = [-10e5]
    t4 = [1, 2, 3, 4, 5]
    t5 = [-1, -2, -3, -4, -5]
    print(maximum_subarray(t1))
    print(maximum_subarray(t2))
    print(maximum_subarray(t3))
    print(maximum_subarray(t4))
    print(maximum_subarray(t5))

    print(generate_small_testcase())
    print(generate_small_testcase())
    print(generate_small_testcase())