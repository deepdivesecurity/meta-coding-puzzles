from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # NOTE: Need to switch from pop/append to a hashmap to improve speed since this currently only passes 36/37 tests
  
  # Initialize variables
  previous = []
  count = 0
  
  # Loop through list of food plates
  for i in D: 
    # Check if the plate has recently been eaten; if yes, continue to the next food
    if i in previous: 
      continue
    else: 
      # Check if the previous eaten food list count is >= K
      if len(previous) >= K: 
        # If yes, remove the first element of the previously eaten food list
        previous.pop(0)

      # Add the plate to the previously eaten food list
      previous.append(i)
      
      # Increase count of eaten food by 1
      count += 1
    
  return count
