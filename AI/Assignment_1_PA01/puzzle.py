from node import Node

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.open = []
        self.closed = []

    def dundundundun(self):
        print('Enter the start matrix \n(whitespace seperated n numbers on n lines) \n( _ for blank)')
        start_matrix = self.accept_matrix()
        print('Enter goal matrix in above format')
        goal_matrix = self.accept_matrix()
        '''Now we have to convert start matrix into node that can generate children'''
        start_node = Node(start_matrix, 0, 0)
        '''finding the f value of start node and then appending it to open list'''
        start_node.f_value = self.find_f_value(start_node, goal_matrix)
        self.open.append(start_node)
        '''many nodes can be duplicated when heuristic function is difference between matrices
        to avoid that, we are appending every already explored matrices to list
        so that if already explored child node is already explored, its childre aren't generated again'''
        already_explored = []
        while True:
            current_node = self.open[0]
            already_explored.append(current_node.matrix)
            current_node.print_node_info()
            '''stop condition (when current matrix becomes equal to goal matrix)'''
            if self.find_h_value(current_node.matrix, goal_matrix) == 0:
                break
            '''creating childs by moving the blank i.e. _ in all possible directions,
            finding their heuristic (f) values and appending them to open list'''
            for i in current_node.generate_child_nodes():
                if i.matrix not in already_explored:
                    already_explored.append(i.matrix)
                    i.f_value = self.find_f_value(i, goal_matrix)
                    self.open.append(i)
            '''add current node to closed list and delete it from open list'''
            self.closed.append(current_node)
            del self.open[0]
            '''we have to sort open list according to f values of nodes so that
            we in next loop, we will check node with list '''
            self.open.sort(key = lambda node:node.f_value)


    def accept_matrix(self):
        '''accepts square of given size'''
        temp = []
        for i in range(self.size):
            temp.append(input().split(" "))
        return temp

    def find_f_value(self, start_node, goal_matrix):
        '''finds heuristic value of a node'''
        return start_node.level + self.find_h_value(start_node.matrix, goal_matrix)

    def find_h_value(self, start_matrix, goal_matrix):
        '''finds the difference between given puzzles'''
        diff = 0
        for i in range(self.size):
            for j in range(self.size):
                if start_matrix[i][j] != goal_matrix[i][j] and start_matrix[i][j] != '_':
                    diff = diff+1
        return diff
