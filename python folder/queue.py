def isEmpty(queue):
    if not queue:
         return True
    else:
        return False
def enqueue(queue,n):
    queue.append(n)
    return queue
def dequeue(queue):
    if isEmpty(queue):
        print("queue is empty")
        return False
    else:
        print(queue.pop(0))
        return queue
queue=[]
print(queue)
enqueue(queue,2)
enqueue(queue,3)
enqueue(queue,4)
dequeue(queue)
dequeue(queue)
dequeue(queue)
print(queue)
