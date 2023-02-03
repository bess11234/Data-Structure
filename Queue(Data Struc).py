class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    def Enqueue(self, data):
        data = Member(data)
        if self.front == None:
            self.front = data
        if self.rear == None:
            self.rear = data
        else:
            self.rear.link = data
            self.rear = data
        self.count += 1
    def Dequeue(self):
        if self.count != 0:
            self.front = self.front.link
            self.count -= 1
        else:
            print("Queue Empty!!")
    def Queuefront(self):
        if self.count != 0:
            print(self.front.data)
            return self.front.data
        else:
            print("Queue Empty!!")
    def Queuerear(self):
        if self.count != 0:
            print(self.rear.data)
            return self.rear.data
        else:
            print("Queue Empty!!")
    def seeall(self):
        if self.count != 0:
            posi = self.front
            while posi != None:
                print(posi.data, end=" ")
                posi = posi.link
            print()
        else:
            print("Queue Empty!!")
class Member:
    def __init__(self, name):
        self.data = name
        self.link = None
myq = Queue()
myq.Enqueue("John")
myq.Enqueue("Jame")
myq.Enqueue("Jane")
myq.Enqueue("Jim")
myq.Enqueue("Jam")
myq.seeall()
myq.Dequeue()
myq.Dequeue()
myq.Dequeue()
myq.Dequeue()
myq.Dequeue()
myq.seeall()