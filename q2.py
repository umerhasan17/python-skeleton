# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below

  # finding all possible ways of adding numbers and storing it in array

  cumulative_sums_in = [0]

  # n ^ 2 time complexity
  for i in range(len(cashFlowIn)):
    add = []
    for j in cumulative_sums_in:
      add += [j + cashFlowIn[i]]
    cumulative_sums_in += add

  cumulative_sums_out = [0]

  # n ^ 2 time complexity
  for i in range(len(cashFlowOut)):
    add = []
    for j in cumulative_sums_out:
      add += [j + cashFlowOut[i]]
    cumulative_sums_out += add
  
  # sort taking n log n time
  cumulative_sums_in.sort()
  cumulative_sums_out.sort()

  # big number using bitwise for faster processing
  # due to constraints this is suitable
  answer = 2 << 20

  # n ^ 2 time complexity
  # the number i must be bigger than j for the difference to be +ve
  for i in range(1, len(cumulative_sums_in)):
    # starting from 1 otherwise smallest diff = 0 - 0 which is incorrect
    for j in range(len(cumulative_sums_out)):
      # only calculate diff once to save processing time
      diff = cumulative_sums_in[i] - cumulative_sums_out[j]
      if diff < answer and diff >= 0:
        answer = diff

  print (answer)
  return answer

question02([66, 293, 215, 188, 147, 326, 449, 162, 46, 350], [170, 153, 305, 290, 187])
question02([189, 28],[43, 267, 112, 166])
question02([72, 24, 73, 4, 28, 56, 1, 43], [27])