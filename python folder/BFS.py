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

    def bfs(self,startNode):
        visited=[False] *len(self.list)
        queue=[]
        visited[startNode]=True
        queue.append(startNode)

        while queue:
            startNode=queue.pop(0)
            print(startNode,end=' ')

            for i in self.list:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g=graph()
g.createEdge(0,1)
g.createEdge(0,4)
g.createEdge(1,4)
g.createEdge(1,3)
g.createEdge(1,2)
g.createEdge(2,3)
g.createEdge(3,4)

g.display()
g.bfs(2)