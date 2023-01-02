#from utils import *
# from ..Leetcode.utils.utility  import Graph

class Solution:
    def allPathsSourceTarget(self, graph):#
        adc_list = {index:val for index,val in enumerate(graph)}
        self.visited=[False]*len(graph)
        self.hash = []
        self.paths = []
        self.dfs(graph,0,(len(graph))-1,[])
        return self.paths


    def dfs(self, graph, source, dest,chain):
        if source==dest:
            self.paths.append(chain+[dest])
            return
        queue = list(graph[source])
        ln= len(queue)
        while(ln>0):
            element = queue.pop()
            path = self.dfs(graph,element,dest,chain+[source])
            ln-=1
def fun():
    args=[[4,3,1],[3,2,4],[3],[4],[]]
    sol = Solution()
    return sol.allPathsSourceTarget(args)

if __name__=='__main__':
    print(fun())