from Node import Node
import queue
#Grobal Declarations
states = []
actions = []
transitionTable = []
testCases = []
M = 0
N = 0
T = 0


def get_state(state, action):
    return transitionTable[state][action]


def get_action_index(action):
    return actions.index(action)


def goal_test(node, goal):
    return node.state == goal


def Breadth_First_Search(initial_state, goal_state):
    node = Node(initial_state, -1, 0, None)
    if goal_test(node, goal_state):
        return node
    frontier = []
    frontier.append(node)
    explored = set()
    while(True):
        if len(frontier) == 0:
            return None
        node = frontier.pop(0)
        explored.add(node.state)
        for action in actions:
            child = Node(get_state(node.state, get_action_index(action)), get_action_index(action), node.cost+1, node)
            if not ((child in frontier) or (child.state in explored)):
                if goal_test(child, goal_state):
                    return child
                frontier.append(child)


def take_input():
    MNT = input().split(' ')
    global M, N, T
    M = int(MNT[0])
    N = int(MNT[1])
    T = int(MNT[2])
    input()
    for i in range(M):
        states.append(input())
    input()
    for i in range(N):
        actions.append(input())
    input()
    for i in range(M):
        temp = input().split(' ')
        transitionTable.append([])
        for j in range(N):
            transitionTable[i].append(int(temp[j]))
    input()
    for i in range(T):
        testCases.append(input().split('\t'))
    #print(testCases)


def start():
    for test in testCases:
        initial_state = states.index(test[0])
        goal_state = states.index(test[1])
        result = Breadth_First_Search(initial_state, goal_state)
        #Test
        #print(result.action, result.parent, result.state, result.cost)
        #EndTest
        if result is None:
            print("No Solution Exists")
        else:
            stack = []
            while result.action != -1:
                stack.append(actions[result.action])
                result = result.parent
            print_result(stack)


def print_result(stack):
    while len(stack) != 0:
        print(stack.pop(), end='')
        if len(stack) != 0:
            print(" -> ", end='')
    print('')


# Function Callings
take_input()
start()