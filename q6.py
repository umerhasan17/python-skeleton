# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# def question06(numServers, targetServer, times):
#   # modify and then return the variable below

#   # times is the unvisited set and contains all edge weights

#   # filling distances array with pseudo infinite values
#   distances = [0]
#   for i in range(numServers):
#     distances.append(2 << 20)
  
#   for i in times:
#     for j in times[i]:
#       if (times[i][j] < distances[j]):
#         distances[j] = times[i][j]
#     times.remove(i)

#   # might be +/- 1 
#   answer = distances[targetServer]
#   print (distances)
#   print (answer)
#   return answer

def question06(numServers, targetServer, times):
  answer = -1
  
  unvisited = [i for i in range(numServers)]
  infinity  = 10000
  graph     = times
  djikstra  = [infinity for _ in range(numServers)]
  djikstra[0] = graph[0][0]
  visited = [0]

  for node in unvisited:
    if node not in visited:
      djikstra[node] = min(djikstra[node], djikstra[0] + graph[0][node])
    
  while len(visited) < numServers:
    nextNode = findNextNode(djikstra, visited, infinity)
    visited.append(nextNode)
    for node in unvisited:
      if node not in visited:
        djikstra[node] =  min (djikstra[node], djikstra[nextNode] + graph[nextNode][node])

  print (visited)
  print (answer)
  answer = djikstra[targetServer]

def findNextNode(djikstra, visited, infinity):
  nextNode = djikstra.index(min(djikstra))
  if nextNode not in visited:
    return nextNode
  djikstraTmp = djikstra[:]
  djikstraTmp[nextNode] = infinity

  return findNextNode(djikstraTmp, visited, infinity)

question06(3, 2, [[1, 2, 3] , [1, 2, 3], [3, 4, 5]])