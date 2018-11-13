# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  set = portfolios
  n = len(portfolios)

  int_bits = 16
  index = 0
  for i in range(int_bits - 1, -1, -1):
    maxInd = index
    maxEle = -10000
    for j in range (index, n):
      if ((set[j] & (1 << i)) != 0 and set[j] > maxEle):
        maxEle = set[j]
        maxInd = j
    if (maxEle == -10000):
      continue
    
    temp = set[index]
    set[index] = set[maxInd]
    set[maxInd] = temp

    maxInd = index

    for j in range(n):
      if (j != maxInd and (set[j] & (1 << i ) ) != 0):
        set[j] = set[j] ^ maxInd

    index += 1
  
  answer = 0
  for i in range(n):
    answer = answer ^ set[i]
  
  print(answer)
  
  return answer

  # for i in range(len(portfolios)):
  #   for j in range(i+1, len(portfolios)):
  #     # exclusive or
  #     answer = max(answer, portfolios[i] ^ portfolios[j])
  
  # print (answer)
  # return answer

question01([15, 8, 6, 7])
question01([9, 7, 12, 2])