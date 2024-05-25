from OperationReserach.config.ReadData import ReadData
from OperationReserach.entity.functions import *
from gurobipy import *

node_num = 10
data = ReadData('c202', node_num)
distance = data.process_data()

try:
    # creat model
    m = Model('tsp_miz')

    # add variables
    x = m.addVars(node_num + 1, node_num + 1, vtype=GRB.BINARY, name='x')
    a = m.addVars(node_num + 1, vtype=GRB.INTEGER, name='a')

    # set objective
    m.setObjective(
        quicksum(x[i, j] * distance[i][j] for i in range(node_num + 1) for j in range(node_num + 1) if i != j),
        GRB.MINIMIZE)

    # add constraints
    m.addConstrs((quicksum(x[i, j] for j in range(1, node_num+1) if i != j) == 1 for i in range(node_num)), name='c1')
    m.addConstrs((quicksum(x[i, j] for i in range(node_num+1) if i != j) == 1 for j in range(1, node_num+1)), name='c2')
    m.addConstrs((a[j] - a[i] + (1-x[i, j])*(node_num+2) >= 1 for i in range(node_num+1) for j in range(node_num+1)),
                 name='c3')

    m.optimize()
    if m.Status == GRB.Status.INFEASIBLE:
        m.computeIIS()
        m.write('MTZ.ilp')
    else:
        x_value = m.getAttr('x', x)
        route = getRoute(x_value, node_num)
        print(route)
except GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))
except AttributeError:
    print(' Encountered an attribute error ')
