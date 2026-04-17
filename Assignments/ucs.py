import heapq
import time
cost=1
nodes=1

def initialize_matrix(matrix):
  string=input("Enter Matrix: ")
  k=0
  for _ in range(3):
    row=list()
    for _ in range(3):
      row.append(int(string[k]))
      k+=1
    matrix.append(row)

def print_matrix(matrix):
  for i in range(3):
    for j in range(3):
      print(matrix[i][j], end=" ")
    print()

def back_track(parent, current, initial_matrix):
  input("Press Enter to see the Path...")
  print("The path is:")
  current=tuple(tuple(row) for row in current)
  while current!=initial_matrix:
    global cost
    cost+=1
    print(current)
    current=parent[current]
    current=tuple(tuple(row) for row in current)
  print(current)
        
def bfs(initial_matrix, goal_matrix):
  global nodes
  visited=list()
  queue=list()
  heapq.heappush(queue, (0, initial_matrix))
  parent=dict()
  # Have to use tuples for backtracking
  start_matrix=tuple(tuple(row) for row in initial_matrix)
  parent[start_matrix]=None
  while queue:
    _, current_matrix=heapq.heappop(queue)
    # Get the state which has not visited yet
    valid=False
    while not valid:
      valid=True
      for _ in visited:
        #Already checked that location
        if current_matrix==_:
          _, current_matrix=heapq.heappop(queue)
          valid=False
          break
    # We have current matrix a tuple, but we need a list
    current_matrix=list(list(row) for row in current_matrix)
    if current_matrix==goal_matrix:
      print(current_matrix)
      print("Goal Reached!")
      back_track(parent, current_matrix, start_matrix)
      return
    print(current_matrix)
    visited.append(current_matrix)
    #Find the blank space in matrix
    for i in range(3):
      for j in range(3):
        # Make the appropriate moves from current blankspace
        if current_matrix[i][j]==0:
          # Check if we are not in the last row, we can move down
          if i!=2:
            matrix=[row[:] for row in current_matrix]
            matrix[i][j], matrix[i+1][j] = matrix[i+1][j], 0
            new_matrix=tuple(tuple(row) for row in matrix)
            heapq.heappush(queue, (0, new_matrix))
            parent[new_matrix]=current_matrix
            nodes+=1
          # Check if we are not in the first row, we can move up
          if i!=0:
            matrix=[row[:] for row in current_matrix]
            matrix[i][j], matrix[i-1][j] = matrix[i-1][j], 0
            new_matrix=tuple(tuple(row) for row in matrix)
            heapq.heappush(queue, (0, new_matrix))
            parent[new_matrix]=current_matrix
            nodes+=1
          # We can move right
          if j!=2:
            matrix=[row[:] for row in current_matrix]
            matrix[i][j], matrix[i][j+1] = matrix[i][j+1], 0
            new_matrix=tuple(tuple(row) for row in matrix)
            heapq.heappush(queue, (0, new_matrix))
            parent[new_matrix]=current_matrix
            nodes+=1
          # We can move left
          if j!=0:
            matrix=[row[:] for row in current_matrix]
            matrix[i][j], matrix[i][j-1] = matrix[i][j-1], 0
            new_matrix=tuple(tuple(row) for row in matrix)
            heapq.heappush(queue, (0, new_matrix))
            parent[new_matrix]=current_matrix
            nodes+=1
# End of the Function

initial_matrix=list()
print("Initial Matrix")
initialize_matrix(initial_matrix)
print_matrix(initial_matrix)

goal_matrix=list()
print("Goal Matrix")
initialize_matrix(goal_matrix)
print_matrix(goal_matrix)

start_time=time.time()
bfs(initial_matrix, goal_matrix)
end_time=time.time()
print("Time taken: ", end_time-start_time)
print("Path Cost: ", cost)
print("Nodes Visited: ", nodes)