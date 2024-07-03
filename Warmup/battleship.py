from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  shipCounter = 0
  
  # Iterate through the rows counting the number of 1s - we can assume that if it's not a 1, it must be a 0
  for row in G: 
    # Use list count method to count number of 1s in the row
    shipCounter = shipCounter + row.count(1)

  return shipCounter / (R * C)
