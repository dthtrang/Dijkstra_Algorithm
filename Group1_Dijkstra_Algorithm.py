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
                 'F':{'distance':inf, 'prev':[]},
                 'G':{'distance':inf, 'prev':[]}
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
    graph = {
        'A':{'B':14.1,'C':16.8, 'D':18.6},
        'B':{'A':14.1,'D':6.3},
        'C':{'A':16.8,'D':2.4,'F':7.8},
        'D':{'A':18.6,'B':6.3,'C':2.4,'E':5.2,'F':4.3},
        'E':{'D':5.2,'G':5.3},
        'F':{'C':7.8,'D':4.3,'G':5.4},
        'G':{'E':5.3,'F':5.4}
        }

    start = 'A'
    destination = 'G'
    Dijskstra(graph,start,destination)
