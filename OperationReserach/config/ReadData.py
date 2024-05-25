import math

import numpy as np
import os

from numpy import ndarray

from OperationReserach.entity.Node import Node

file_path = os.path.abspath('..')


class ReadData:
    def __init__(self, filename, rows_num):
        self.path = file_path + r'\config\Solomn Instance\solomon-100\{}.txt'.format(filename)
        self.rows_num = rows_num
        self.nodes = []

    def process_data(self) -> ndarray[float]:
        """
        rows_num 为客户（点个数）数，第一个点为仓库（起始点）
        """
        data = np.loadtxt(self.path, skiprows=9, dtype=int)
        for row in range(self.rows_num):
            node = Node(data[row])
            self.nodes.append(node)
        #
        distance = np.zeros((self.rows_num + 1, self.rows_num + 1))
        for i in range(self.rows_num):
            for j in range(self.rows_num):
                distance[i][j] = math.sqrt((self.nodes[i].pos_x - self.nodes[j].pos_x) ** 2 +
                                           (self.nodes[i].pos_y - self.nodes[j].pos_y) ** 2)
        for i in range(self.rows_num):
            distance[self.rows_num][i] = distance[0][i]
            distance[i][self.rows_num] = distance[i][0]
        return distance
