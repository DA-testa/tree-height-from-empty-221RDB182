# python3

import sys
import threading

def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    max_height = 0
    queue = [root]
    
    while queue:
        height = 0
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            children = tree[node]
            for child in children:
                queue.append(child)
        max_height = height if height > max_height else max_height
        height += 1
    return max_height

    # input number of elements
    # input values in one variable, separate with space, split these values in an array

def main():
    # implement input form keyboard and from files
    input_type = input("Enter F for file or K for keyboard")
    
    if input_type == 'F':
        file_name = input("File name?")
    # let user input file name to use, don't allow file names with letter a
        while 'a' in file_name:
            file_name = input("File name is not valid")
        try:
            with open('folder/' + file_name, 'r') as file:
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

    height = compute_height(n, parents)

    # call the function and output it's result
    print("Height of the tree: ", height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
