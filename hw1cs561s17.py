'''
 name				email
 Keying Zhou  	keyingzh@usc.edu


'''
import sys
lines = []
with open(sys.argv[2]) as f:
    lines.extend(f.read().splitlines())


class Node(object):
    def __init__(self, name, parent_node, path, left_fuel):
        self.name = name
        self.parent_node = parent_node
        self.path = path
        self.left_fuel = left_fuel


def solution(destination_node):
    cost = destination_node.left_fuel
    answer = destination_node.path + " " + str(cost)
    return answer


def bfs(start_name, destination_name, graph_input):
    explore = set()
    start_node = Node(start_name, None, start_name, fuel)
    bfs_queue = [start_node]
    while bfs_queue:
        head = bfs_queue.pop(0)
        if head.name == destination_name:
            return solution(head)
        if head.name not in explore:
            explore.add(head.name)
            for child_t in graph_input[head.name]:
                key = child_t[0]
                value = child_t[1]
                left = head.left_fuel - value
                if (left >= 0) and (key not in explore):
                    path = head.path + "-" + key
                    bfs_queue.append(Node(key, head, path, left))
    return "No Path"


def dfs(start_name, destination_name, graph_input):
    explore = set()
    start_node = Node(start_name, None, start_name, fuel)
    dfs_stack = [start_node]
    while dfs_stack:
        head = dfs_stack.pop()
        if head.name == destination_name:
            return solution(head)
        if head.name not in explore:
            explore.add(head.name)
            for child_t in reversed(graph_input[head.name]):
                key = child_t[0]
                value = child_t[1]
                left = head.left_fuel - value
                if (left >= 0) and (key not in explore):
                    path = head.path + "-" + key
                    dfs_stack.append(Node(key, head, path, left))
    return "No Path"


def ucs(start_name, destination_name, graph_input):
    explore = set()
    start_node = Node(start_name, None, start_name, fuel)
    ucs_priority_queue = [start_node]
    while ucs_priority_queue:
        head = ucs_priority_queue.pop(0)
        if head.name == destination_name:
            return solution(head)
        if head.name not in explore:
            explore.add(head.name)
            for child_t in graph_input[head.name]:
                key = child_t[0]
                value = child_t[1]
                left = head.left_fuel - value
                if (left >= 0) and (key not in explore):
                    path = head.path + "-" + key
                    count = 0
                    if ucs_priority_queue:
                        for i in ucs_priority_queue:
                            if i.left_fuel > left:
                                count += 1
                            if (i.left_fuel == left) and (i.name <= key):
                                count += 1
                        ucs_priority_queue.insert(count, Node(key, head, path, left))
                    else:
                        ucs_priority_queue.append(Node(key, head, path, left))
    return "No Path"

fo = open("output.txt", "wb")
search_alg = lines[0]
lines.pop(0)
fuel = int(lines[0])
lines.pop(0)
start = lines[0]
lines.pop(0)
destination = lines[0]
lines.pop(0)

graph = {}

for i in lines:
    split1 = i.split(': ')
    parent = split1[0]
    split2 = split1[1].split(', ')
    children = []
    for j in split2:
        split3 = j.split('-')
        children_name = split3[0]
        needed_fuel = int(split3[1])
        children_tuple = (children_name, needed_fuel)
        if children:
            count = 0
            for k in children:
                if k[0] < children_name:
                    count += 1
            children.insert(count, children_tuple)
        else:    
            children.append(children_tuple)
    graph[parent] = children

if search_alg == "BFS":
    solution = bfs(start, destination, graph)
elif search_alg == "DFS":
    solution = dfs(start, destination, graph)
elif search_alg == "UCS":
    solution = ucs(start, destination, graph)
fo.write(solution)
