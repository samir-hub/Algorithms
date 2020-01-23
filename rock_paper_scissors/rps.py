#!/usr/bin/python

import sys

def add_plays(arr):
    other_array = []
    my_array = [['rock'], ['paper'], ['scissors']]
    for i in arr: 
        for j in my_array:
            other_array.append(i+j)
    return other_array 

def rock_paper_scissors(n):
    if n == 0: 
        return [[]]
    elif n == 1: 
        return [['rock'], ['paper'], ['scissors']]   
    return add_plays(rock_paper_scissors(n-1))     


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


#other_array = []
#my_array = [['rock'], ['paper'], ['scissors']]

#for i in my_array:
    #for j in my_array:
        #for k in my_array:
            #other_array.append(i+j+k)
    
#print(other_array)


#print(rock_paper_scissors(2))


