#from utils import *
visited = []
def fun(graph_matrix):
    graph = {}
    Max = -99
    for each in graph_matrix:
        if each[0] not in graph.keys():
            graph[each[0]]= [each[1]]
        else:
            print(each)
            graph[each[0]].append(each[1])
        if each[1] not in graph.keys():
            graph[each[1]]= []
        if max(each[0],each[1] > Max):
            Max = max(each[0],each[1])
    print(graph)
    global visited
    visited = [False]*(Max+1)
    return validPath(graph, 0,2)
    
def validPath(graph, source ,dest):
    # import pdb; pdb.set_trace()
    queue = graph[source]
    size = len(queue)
    while(size>0):
        edge = queue.pop(0)
        if visited[edge]==False:
            if edge==dest:
                return True
            if validPath(graph, edge, dest)==True:
                return True
            size-=1
    visited[source]=True
    return False

#TODO: TO COMPLETE 

if __name__=='__main__':
    print(fun([[0,1],[0,2],[3,5],[2,3],[5,4],[4,3]]))