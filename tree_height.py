import sys
import threading

def dfs(node, depth, parent, graph):
    if parent[node] == -1:
       depth[node] = 0
    else:
      depth[node] = depth[parent[node]] + 1
    for child in graph[node]:
    if child != parent[node]:
        dfs(child, depth, parent, graph)
def tree_height(n, parent):
graph = defaultdict(list)
for i in range(n):
    if parent[i] != -1:
        graph[parent[i]].append(i)
        graph[i].append(parent[i])
        
  depth = [-1] * n
for i in range(n):
    if parent[i] == -1:
        dfs(i, depth, parent, graph)

return max(depth) + 1
  
    def compute_height(n, parents):
return tree_height(n, parents)

def main():
    input_type = input("Enter F for file or K for keyboard")
    
    if input_type == 'F':
        file_name = input("File name?")
        while 'a' in file_name:
            file_name = input("File name is not valid")
        try:
            with open(file_name, 'r') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except:
            print("Could not read file")
            return
    else:
        try:
            n = int(input("Enter the number of nodes: "))
            parents = list(map(int, input("Enter the parents of the nodes: ").split()))
        except:
            print("Invalid input")
            return

    print("Height of the tree:", (compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
