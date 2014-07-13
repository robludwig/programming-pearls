#programming pearls book problems:
'''
input: a file containing at most n positive integers, each less than n
where n = 10^7. It is a fatal error if any integer occurs twice in the input.
No other data is associated with the integer.

output: a sorted list in increasing order of the input integers.

constraints vary:
	a) 1MB of storage in main memory but ample disk storage.
	b) run time on the order of minutes.
	c) try speeding the run time up to the order of seconds
	d) try not using as much disk space
'''

import os, random
import time
import bitmap

def generate_file(filename, num_integers, write_probability = 0.98):
	all_integers = range(1, num_integers)
	random.shuffle(all_integers)
	with open(filename, "wb") as outfile:	
		for out_int in all_integers:
			if random.random() < write_probability:
				outfile.write(str(out_int) + "\n")
	
#python stdlib version of a bitmap-based sort: a dictionary hashmap
#this probably will use a lot of memory though...
def dict_read(filename):
	bit_dict = {}
	with open(filename) as infile:
		for line in infile:
			currentnumber = int(line.strip())
			bit_dict[currentnumber] = True
	return bit_dict
def dict_write(outfilename, bit_dict, num_integers):
	with open(outfilename, 'w') as writeout:
		for writeint in xrange(num_integers):
			if bit_dict.get(writeint, False):
				writeout.write(str(writeint) + "\n")

def dict_sort(inputfilename, outputfilename, num_integers):
	dict_write(outputfilename, dict_read(inputfilename), num_integers)
#end dict sort fxns


#naive version: read all the numbers into a list, sort them, and then write them out
def list_read(filename):
	all_numbers = []
	with open(filename) as infile:
		for line in infile:
			all_numbers.append(int(line.strip()))
	return all_numbers
def list_write(outfilename, sorted_numbers):
	with open(outfilename, 'w') as writeout:
		for writeint in sorted_numbers:
			writeout.write(str(writeint) + "\n")
def list_sort(inputfilename, outputfilename):
	numbers = list_read(inputfilename)
	numbers.sort()
	list_write(outputfilename, numbers)
#end list sort fxns

#using third-party bitmap library
def bitmap_read(filename, num_integers):
	intmap = bitmap.BitMap(num_integers)
	with open(filename) as infile:
		for line in infile:
			currentnumber = int(line.strip())
			intmap.set(currentnumber)
	return intmap
def bitmap_write(outfilename, intmap, num_integers):
	with open(outfilename, 'w') as writeout:
		for writeint in xrange(num_integers):
			if intmap.test(writeint):
				writeout.write(str(writeint) + "\n")

def bitmap_sort(inputfilename, outputfilename, num_integers):
	bitmap_write(outputfilename, bitmap_read(inputfilename, num_integers), num_integers)
#end bitmap sort fxns


def validate_file(filename):
	ints_read = 0
	with open(filename) as infile:
		lastnumber = -1 #numbers are all positive..
		currentnumber = 0
		for line in infile:
			currentnumber = int(line.strip())
			#print "read current number ", currentnumber, " and last number is ", lastnumber
			if currentnumber <= lastnumber:
				print " non monotonically-increasing file, %i <= %i " % (currentnumber, lastnumber)
				return False
			else:
				lastnumber = currentnumber
				ints_read += 1
		print "read %i numbers and they were all in order" % ints_read
		return True

def compare_solutions(firstsolution, secondsolution):
	with open(firstsolution) as file1:
		with open(secondsolution) as file2:
			for line in file1:
				if line != file2.readline():
					return False
			if file2.read():
				print "there was more input in the second file..."
				return False
			return True


if __name__ == '__main__':
	num_ints = 1000000
	generate_file("test", num_ints)
	
	start_time = time.time()
	dict_sort("test", "testout_dict", num_ints)
	dict_time = time.time() - start_time
	valid = validate_file("testout_dict")
	print "does dict work? ", valid
	
	start_time = time.time()
	list_sort("test", "testout_list")
	list_time = time.time() - start_time
	valid = validate_file("testout_list")
	print "does list work? ", valid
	
	
	start_time = time.time()
	bitmap_sort("test", "testout_bitmap", num_ints)
	bitmap_time = time.time() - start_time
	valid = validate_file("testout_bitmap")
	print "does bitmap work? ", valid
	
	same = compare_solutions("testout_list", "testout_dict")
	if same:
		same = compare_solutions("testout_bitmap", "testout_list")
	print "were the solutions the same?", same
	
	print "time to sort using dict: %03f" % dict_time
	print "time to sort using builtin list sort: %03f" % list_time
	print "time to sort using bitmap: %03f" % bitmap_time