# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
      # exclusive or
      answer = max(answer, portfolios[i] ^ portfolios[j])
  
  print (answer)
  return answer

question01([15, 8, 6, 7])
question01([9, 7, 12, 2])