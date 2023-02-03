class Stack():
    def __init__(self):
        self.count = 0
        self.top = None
    def push(self, data):
        data = member(data)
        data.link = self.top
        self.top = data
        self.count += 1
    def pop(self, dataout=None):
        if self.count != 0:
            dataout = self.top
            self.top = self.top.link
            self.count -= 1
            return dataout.data
        else:
            print("Stack Empty!!")
    def StackTop(self, dataout=None):
        if self.count != 0:
            print(self.top.data)
            return self.top.data
        else:
            print("Stack Empty!!")
    def seeall(self):
        if self.count != 0:
            posi = self.top
            while posi != None:
                print(posi.data, end=" ")
                posi = posi.link
            print()
        else:
            print("Stack Empty!!")
class member():
    def __init__(self, name):
        self.data = name
        self.link = None
mystack = Stack()
mystack.push("1")
mystack.push("2")
mystack.push("3")
mystack.push("4")
mystack.push("5")
mystack.seeall()
mystack.seeall()