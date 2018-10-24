# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import itertools

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  answer = -1
  shortest_distance = times[0]
  unvisitedNodes = times[1:]
  targetIndex = targetServer - 1
  print (unvisitedNodes)
  print (shortest_distance)

  while len(unvisitedNodes) != 0:
      for i in range(len(unvisitedNodes)):
          if unvisitedNodes[i][targetIndex] + shortest_distance[i+1] < shortest_distance[targetIndex]:
              shortest_distance[targetIndex] = unvisitedNodes[i][targetIndex] + shortest_distance[i+1]
      unvisitedNodes = np.delete(unvisitedNodes, (i), axis = 0)
      print(shortest_distance)
     

  return answer

question06(3,1,[[0,7,4],[7,0,2],[4,2,0]])