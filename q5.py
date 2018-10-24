# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  answer = 0
  val = 0
  allowedAllocations.sort(reverse = True)
  while (val < totalValue):
    val += allowedAllocations[answer]
    answer += 1
  return answer
