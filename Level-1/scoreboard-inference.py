from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Initiate variables
  # Get the maximum answer points achieved (max of S // 2 to get a whole number since it must be returned as int)
  count = max(S) // 2
  
  # Determine if any of the numbers are odd
  # If a number is odd, it means at least 1 answer must have the value of 1
  for ans in S: 
    if ans % 2 == 1: 
      count += 1
      break
  
  return count
