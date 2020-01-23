#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    other_array = []
    my_array = [['rock'], ['paper'], ['scissors']]
    if len(other_array) == 3 ** n:
      return other_array
    else: 
        for i in my_array:
            other_array.append(i)
            print(other_array)
            return rock_paper_scissors(n-1)    
   
    return other_array

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


other_array = []
my_array = [['rock'], ['paper'], ['scissors']]

for i in my_array:
    for i in my_array:
        for i in my_array:
            other_array.append(i+i+i)
    
print(len(other_array))    


#rock_paper_scissors(3)


 