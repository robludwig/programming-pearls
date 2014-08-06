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

def binary_search(array, target):
	search_range = (0, len(array))
	def range_empty():
		return (search_range[1] - search_range[0]) <= 0
	while not range_empty():
		middle = 
		if range_empty():
			return -1
		

		
		


tester = [0,1,2,3,4,5,6,7,8,9,10]
print binary_search(tester, 5)