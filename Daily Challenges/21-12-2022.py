class Solution:
    def addInGraph(self, graph, el, el2):
        graph[el].add(el2)
        graph[el2].add(el)

    def possibleBipartition(self, n, dislikes):
        self.visited = [False for x in range(0, n)]
        graph = {index+1: set() for index, key in enumerate(self.visited)}
        for each in dislikes:
            self.addInGraph(graph, each[0], each[1])
        self.v1 = [set(), set()]
        print('graph => ', graph)
        # import pdb; pdb.set_trace()
        for index in range(1, n+1):
            if not self.visited[index-1]:
                if not self.dfs(graph, index, 0):
                    return False
        return True
    
    def dfs(self, graph, source, half):
        if self.visited[source-1]:
            return True
        if  set(graph[source]).intersection(self.v1[half]):
            # print(' inters -> ', self.v1[half], source)
            return False
        self.v1[half].add(source)
        self.visited[source-1]=True
        for each in graph[source]:
            # print('running for ', each)
            result = self.dfs(graph, each, 0 if half==1 else 1)
            # print('result -> ', each, result)
            if not result:
                # print(self.v1[half], source)
                return False
        # self.visited[source-1]=True
        return True




        #     self.visited[source]=True
        #     # add its enemies to the other half
        #     for each in graph[source]:
        #         dfs()
        # else:
        #     pass


    # def rem(self,k):
    #     try:
    #         self.p1.remove
    #     for each in self.graph.keys():
    #         element_to_pair = self.getEl(each)
            

    # def addInSet(self, el):
    #     if set(self.graph[el]).intersection(self.p1)

    # def getEl(self, source):
    #     for each in self.graph.keys():
    #         if each not in self.graph[source]:
    #             return each

def fun():
    sol = Solution()
    return sol.possibleBipartition(3, [[1,2],[1,3],[2,3]])


if __name__=='__main__':
    print(fun())