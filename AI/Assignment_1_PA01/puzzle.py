from node import Node

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.open = []
        self.closed = []
        self.solution = []

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
        while len(self.open) != 0:
            current_node = self.open[0]
            '''stop condition (when current matrix becomes equal to goal matrix)'''
            if self.find_h_value(current_node.matrix, goal_matrix) == 0:
                while current_node.parent != None:
                    self.solution.append(current_node)
                    current_node = current_node.parent
                self.solution.append(current_node)
                break
            '''creating childs by moving the blank i.e. _ in all possible directions,
            finding their heuristic (f) values and appending them to open list'''
            for i in current_node.generate_child_nodes():
                '''many nodes can be duplicated when heuristic function is difference between matrices
                to avoid that, we are checking if the matrix is already in open or closed nodes, its childre aren't generated again'''
                if self.is_not_duplicate(i.matrix):
                    i.f_value = self.find_f_value(i, goal_matrix)
                    self.open.append(i)
            '''add current node to closed list and delete it from open list'''
            self.closed.append(current_node)
            del self.open[0]
            '''we have to sort open list according to f values of nodes so that
            we in next loop, we will check node with list '''
            self.open.sort(key = lambda node:node.f_value)
        for i in reversed(self.solution):
            i.print_node_info()
        print('\nGoal was reached after checking {} state spaces'.format(1+len(self.closed)))
        print('Solution moves are : ')
        for i in reversed(self.solution):
            print('\t', i.move)

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

    def is_not_duplicate(self, matrix):
        '''check if matrix exists in open or closed list'''
        for i in self.open:
            if i.matrix == matrix:
                return False
        for i in self.closed:
            if i.matrix == matrix:
                return False
        return True
