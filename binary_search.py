'''
"Given ample time, only about ten percent of  professional programmers
were able to get this small program right... Knuth points out that while
the first binary search was published in 1946, the first published binary
search without bugs did not appear until 1962. "

Formal Description: Determine whether the sorted array x[0...n-1] contains
the target element t. We know that n>=0 and that x[0] <= x[1] <= x[2]... <=x[n-1].
The types of t and the elements of x are the same; the code should work equally
well for integers, floats or strings. The answer returned is an integer p, indicating
the position in the n corresponding to the target. When p is -1, the target is not
in x, otherwise 0<=p<=n and t=x[p].

'''

import random

def binary_search(array, target):
    search_range = [0, len(array)]
    def range_empty():
        return (search_range[1] - search_range[0]) <= 0
    def range_middle():
        return (search_range[1] + search_range[0])/2
    middle = range_middle()
    while not range_empty():
        middle = range_middle()
        #print "beginning another iteration, range is", search_range, "middle is ", middle, "middle value", array[middle]
        #raw_input()
        if (array[middle] == target):
            #print "target found!"
            return middle
        elif array[middle] < target:
            #print "middle was less than target, adjusting the lower bound up"
            search_range[0] = middle + 1
        elif array[middle] > target:
            #print "middle was greater than target, adjusting the lower bound down"
            search_range[1] = middle - 1

        if range_empty(): #test bounds before flunking out
            if array[0] == target:
                return 0
            elif array[search_range[1]] == target:
                return search_range[1]
            #print "empty range, returning -1"
            return -1
    return -1
        

def generate_random_array(array_length, max_element):
        rand_array = []
        for i in range(array_length):
            rand_array.append(random.randint(0, max_element))
        return sorted(rand_array)

def python_array_search(array, target):
        if target in array:
            return array.index(target)
        return -1

def test(trials = 100, array_length = 5000):
    max_target = 10000
    for i in range(trials):
        print "begin test ", i
        test_array = generate_random_array(array_length, max_target)
        target = random.choice(range(max_target)) #have the possiblity that the target is not in the array
        python_result = python_array_search(test_array, target)
        my_result = binary_search(test_array, target)
        if my_result != python_result:
            if test_array[my_result] != target:
                print "test failed!!!"
                print "python returned", python_result, "i returned", my_result
                return False
            elif test_array[my_result] == test_array[python_result]:
                print "different indexes, but both found it"
        else:
            print "found it!"
            
    return True

if __name__ == '__main__':
    test()

##test_array = generate_random_array(15, 45)
##target = random.choice(test_array)
##print "looking for ", target, " in ", test_array
##print "python search result: ", python_array_search(test_array, target)
##print "my search result: ", binary_search(test_array, target)
