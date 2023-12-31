class graph:
    def __init__(self):
        self.list={}

    def createEdge(self,start,end):
        if start in self.list.keys():
            self.list[start].append(end)
        else:
            self.list[start]=[end]

    def display(self):
        for i in self.list:
            print(i,'->','->'.join([str(j) for j in self.list[i]]))

    def dfs(self,start):
        stack=[start]
        path=[]

        while stack:
            vexter=stack.pop()
            if vexter in path:
                continue
            path.append(vexter)
            for i in self.list[vexter]:
                stack.append(i)
        return path
g=graph()
g.createEdge(1,2)
g.createEdge(1,5)
g.createEdge(2,5)
g.createEdge(2,0)
g.createEdge(2,6)
g.createEdge(0,3)
g.createEdge(3,5)
g.createEdge(7,5)
g.createEdge(5,6)
g.createEdge(6,6)


g.display()
print("DFS -> ")
print(g.dfs(1))