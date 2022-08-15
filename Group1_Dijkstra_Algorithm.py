'''
To create the infinite value we have to use the sys library.
And we also use utility functions from the heapq library
'''
import sys
from heapq import heapify, heappush, heappop

'''
Define the Dijkstra Shortest Path function
'''
def Dijskstra(graph,start,dest):
    inf = sys.maxsize   # infinite value

    # distance show the distance from the first node to this node
    data_table = {'A':{'distance':inf, 'prev':[]},
                 'B':{'distance':inf, 'prev':[]},
                 'C':{'distance':inf, 'prev':[]},
                 'D':{'distance':inf, 'prev':[]},
                 'E':{'distance':inf, 'prev':[]},
                 'F':{'distance':inf, 'prev':[]}
                 }

    # distance to start node from start is 0
    data_table[start]['distance'] = 0    

    # create an array to store visited node 
    # and a temp variable to start from the neighbors
    visited = []
    temp = start
    for i in range (5):
        if temp not in visited:    # in the first iteration temp is start
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:   # iterate through all the neighbors of a node
                if j not in visited:
                    distance = data_table[temp]['distance'] + graph[temp][j]
                    # in the first iteration, j is B -> distance: 0 + 2 = 2
                    # if this distance is < than the distance to the node in the table, replace the value
                    if distance < data_table[j]['distance']:
                        data_table[j]['distance'] = distance
                        # also update the previous nodes of the temp 
                        # by concatenating the previous nodes in the table with the value of temp
                        # in this case, it is none + A = A -> data_table[B]['prev'] = A
                        data_table[j]['prev'] = data_table[temp]['prev'] + list(temp)

                    # appending the distance of each neighbor node 
                    # and the node to a heap to find min later
                    heappush(min_heap,(data_table[j]['distance'],j))

        # find the neighbor with the min distance and update the temp value
        heapify(min_heap)   # make the min_heap, min element (in distance) has index [0]
        temp = min_heap[0][1]   # acces the second element of the fisrt thing in the heap -> temp is now 'B'

    # After all the looping, we finally get the distance to the destination        
    print("Shortest Distance", str(data_table[dest]['distance']))
    print("Shortest Path", str(data_table[dest]['prev'] + list(dest)))


'''
Driver code. The graph is defined in here
'''
if __name__ == "__main__":
    water_supply = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}
        }

    start = 'A'
    destination = 'E'
    Dijskstra(water_supply,start,destination)
