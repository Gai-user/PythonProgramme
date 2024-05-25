import copy
from gurobipy import *

class EliminateSubTour:
    def __init__(self, x_value, node_num):
        self.value = x_value
        self.node_num = node_num

    def min_length_subtour(self):
        """
        寻找长度最小的子环路
        :return: None
        """
        print('程序运行')
        un_find_nodes = [i for i in range(self.node_num + 1)]
        sub_tour = []

        while un_find_nodes:
            temp_sub_tour = []
            cur_node = un_find_nodes.pop(0)
            temp_sub_tour.append(cur_node)
            while 1 == 1:
                # print(temp_sub_tour, cur_node)
                for i in range(self.node_num + 1):
                    if self.value[cur_node, i] > 0.5:
                        cur_node = i
                        if i in un_find_nodes:
                            temp_sub_tour.append(i)
                            un_find_nodes.remove(i)
                        break
                if cur_node == self.node_num or cur_node == temp_sub_tour[0]:
                    if sub_tour == [] or len(sub_tour) > len(temp_sub_tour):
                        sub_tour = copy.deepcopy(temp_sub_tour)
                    break
        return sub_tour

    def sub_tour_lim(self, model, where):
        if where == GRB.Callback.MIPSOL:
            cur_tour = self.min_length_subtour()
            if len(cur_tour) < self.node_num+1:
                print('--- add sub')


if __name__ == '__main__':
    x_value = {(0, 0): 0.0, (0, 1): -0.0, (0, 2): -0.0, (0, 3): -0.0, (0, 4): -0.0, (0, 5): 1.0, (1, 0): 0.0,
               (1, 1): 0.0, (1, 2): 1.0, (1, 3): -0.0, (1, 4): -0.0, (1, 5): -0.0, (2, 0): 0.0, (2, 1): 1.0,
               (2, 2): 0.0, (2, 3): -0.0, (2, 4): -0.0, (2, 5): -0.0, (3, 0): 0.0, (3, 1): -0.0, (3, 2): -0.0,
               (3, 3): 0.0, (3, 4): 1.0, (3, 5): -0.0, (4, 0): 0.0, (4, 1): -0.0, (4, 2): -0.0, (4, 3): 1.0,
               (4, 4): 0.0, (4, 5): -0.0, (5, 0): 0.0, (5, 1): -0.0, (5, 2): -0.0, (5, 3): -0.0, (5, 4): -0.0,
               (5, 5): 0.0}
    sub_tour_eliminate = EliminateSubTour(x_value, 5)
    min_sub_tour = sub_tour_eliminate.min_length_subtour()
    print(min_sub_tour)
