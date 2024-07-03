# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  returnStr = ""
  # Write your code here
  for char in C: 
    if char == "A": 
      returnStr = returnStr + "B"
    else: 
      returnStr = returnStr + "A"
      
  return returnStr
