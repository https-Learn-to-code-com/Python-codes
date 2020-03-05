class Node:
    data = 0
    next = None

    def __init__(self):
        self.data = 0
        self.next = None


class LinkedList:
    root = None

    def insert(self, data):
        n = Node()
        n.data = data
        temp = self.root
        if self.root is None:
            self.root = n
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def display(self):
        temp = self.root
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print(end="\n")


if __name__ == "__main__":
    linkedList = LinkedList()
    while True:
        ch = int(input("1.insert\n2.Display\nEnter your choice : "))
        if ch is 1:
            linkedList.insert(int(input("Enter Data : ")))
        elif ch is 2:
            print("List is : ", end=" ")
            linkedList.display()
        elif ch is 10:
            exit(0)
