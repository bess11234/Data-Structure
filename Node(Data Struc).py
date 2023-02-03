class DataNode:
    def __init__(self, input_name=""):
        self.name = input_name
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
        else:
            pos = self.head
            while pos != None:
                print(pos.name, end=" ")
                pos = pos.next

    def insertfront(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1

    def insertlast(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
            self.count += 1
        else:
            pos = self.head
            for _ in range(self.count-1):
                pos = pos.next
            pos.next = pNew
            self.count += 1
                
    def insertbefore(self, node, data):
        pNew = DataNode(data)
        if self.count == 0:
            print("Cannot insert, <%s> does not exist."%node)
        else:
            recent = self.head
            prev = recent
            countt = 0
            while countt != self.count:
                if recent.name == node:
                    break
                prev = recent
                recent = recent.next
                countt += 1
            if countt == self.count and prev.name != node:
                print("Cannot insert, <%s> does not exist."%node)
                return
            if recent == self.head:
                pNew.next = self.head
                self.head = pNew
            else:
                pNew.next = recent
                prev.next = pNew
            self.count += 1
            
    def delete(self, data):
        if self.count == 0:
            print("Cannot delete, <%s> does not exist."%data)
        else:
            recent = self.head
            prev = recent
            countt = 0
            while countt != self.count:
                if recent.name == data:
                    break
                prev = recent
                recent = recent.next
                countt += 1
            if countt == self.count and prev.name != data:
                print("Cannot delete, <%s> does not exist."%data)
                return
            if recent == self.head:
                self.head = recent.next
            else:
                prev.next = recent.next
            self.count -= 1
        

mylist = SinglyLinkList()
mylist.insertlast("John")
mylist.insertlast("Tony")
mylist.insertfront("Bill")
mylist.traverse()
print()
mylist.insertbefore("Tony","Kim")
mylist.traverse()
print()
mylist.delete("John")
mylist.traverse()