class Node:
    def __init__(self, matrix, level, f_value):
        self.matrix = matrix
        self.level = level
        self.f_value = f_value

    def print_node_info(self):
        '''prints the node info'''
        print('\nNode Level = {} Node F Value = {}\nNode matrix : \n'.format(self.level, self.f_value))
        for i in self.matrix:
            for j in i:
                print(j, '\t', end="")
            print('\n')
        print('\n')

    def generate_child_nodes(self):
        '''we are going to move blank i.e. _ to possible directios out of left, right, up and down'''
        '''first we need to find location of blank'''
        x_blank, y_blank = self.find_blank()
        '''now we have to find possible values values that our blank can move'''
        possible_positions = []
        if x_blank-1 != -1:
            possible_positions.append([x_blank-1, y_blank])
        if x_blank+1 != len(self.matrix):
            possible_positions.append([x_blank+1, y_blank])
        if y_blank-1 != -1:
            possible_positions.append([x_blank, y_blank-1])
        if y_blank+1 != len(self.matrix):
            possible_positions.append([x_blank, y_blank+1])
        '''now we are going to generate the child nodes that by swapping blank with
        all possible values and append them to list and then return that list'''
        children_nodes = []
        for new_position in possible_positions:
            '''
            temp_matrix = self.matrix
            above line doesn't work because changes in temp_matrix changes the self.matrix
            '''
            temp_matrix = self.create_duplicate_matrix(self.matrix)
            temp_matrix[x_blank][y_blank], temp_matrix[new_position[0]][new_position[1]] = temp_matrix[new_position[0]][new_position[1]], temp_matrix[x_blank][y_blank]
            children_nodes.append(Node(temp_matrix, self.level+1, 0))
        return children_nodes

    def find_blank(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == '_':
                    return i, j
    def create_duplicate_matrix(self, matrix):
        temp = []
        for i in matrix:
            temp_row = []
            for j in i:
                temp_row.append(j)
            temp.append(temp_row)
        return temp
