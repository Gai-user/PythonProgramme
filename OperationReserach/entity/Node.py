from typing import List


class Node:
    def __init__(self, info: List[int]) -> None:
        self.pos_x = info[1]
        self.pos_y = info[2]
        self.demand = info[3]
        self.ready_time = info[4]
        self.due_time = info[5]
        self.servie = info[6]
