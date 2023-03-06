import sys

def tree_height(n, parent):
    nodes = [[] for i in range(n)]
    for i in range(n):
        if parent[i] == -1:
            root = i
        else:
            nodes[parent[i]].append(i)
    height = 0
    stack = [(root, 0)]
    while stack:
        node, h = stack.pop()
        height = max(height, h)
        for child in nodes[node]:
            stack.append((child, h+1))
    return height

if __name__ == "__main__":
    source = input("Enter F for file or K for keyboard")
    if source == "F":
        file = open("input.txt", "r")
        n = int(file.readline())
        parent = list(map(int, file.readline().split()))
    else:
        n = int(input("Enter the number of nodes: "))
        parent = list(map(int, input("Enter the parents of the nodes: ").split()))

    print(tree_height(n, parent))
