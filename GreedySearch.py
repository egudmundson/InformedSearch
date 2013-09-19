from Node import * 
from hash import *
from collections import deque
from actions import *
def GreedySearch(StartNode,GoalNode,h):
	fronteir = deque();
	fronteir.append(StartNode)
	if(StartNode == GoalNode):
		return StartNode
	while(len(fronteir) !=0):
		parent = fronteir.popleft()
		tmp = []
		actions = getActions(parent);
		for x in actions:
			tmp.append(Node(x(parent)))
		best = tmp[0]
		for x in tmp:
			x.cost = h(x)
			if(x.cost > best.cost):
				best = x
		print best

def h(node):
	if(node.state == [1,0,2,3,4,5,6,7,8]):
		return 5
	else:
		return 1

parent=Node([1,2,0,3,4,5,6,7,8])
goal=Node([0,1,2,3,4,5,6,7,8])
GreedySearch(parent,goal,h);
