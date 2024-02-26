from node import Node

class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"
    
    def append(self, item):
        """adding element to the end of linked list"""
        my_node = Node(item)

        if self.is_empty():
            self._head = my_node
            return
        
        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(my_node)

    def index(self, item):
        """return an index of item"""
        current = self._head
        found = False
        index = 0
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                index += 1
                current = current.get_next()
        if found == False:
            return f"No element with data {item}"
        else:
            return index

    def pop(self, index):
        """delete element by index"""
        current = self._head
        previous = None

        if index < self.size():
            for i in range(index):
                if i > index:
                    break
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def insert(self, index, item):
        """insert element before the index"""
        current = self._head
        previous = None

        if index < self.size():
            for i in range(index):
                if i > index - 1:
                    break
                else:
                    previous = current
                    current = current.get_next()
        
        my_node = Node(item)
        if previous is None:
            self._head = my_node
            my_node.set_next(current)
        else:
            previous.set_next(my_node)
            my_node.set_next(current)
    
    def slice_list(self, start, stop):
        """make a slice of linked list between start and stop indexes (not including stop)"""
        new_list = UnsortedList()
        current = self._head
        previous = None

        if start >= 0 and start < stop:
            if stop < self.size():
                for i in range(start):
                    if i > start:
                        break
                    else:
                        previous = current
                        current = current.get_next()
                for i in range(stop - start):
                    if i < stop - start:
                        new_list.append(current.get_data())
                        print(current.get_data())
                        current = current.get_next()
        return new_list
    
if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.append(72)

    print(my_list)
    print(my_list._head.get_data())
    print(my_list.index(54))
    print(my_list.index(72))
    my_list.pop(4)
    print(my_list)
    my_list.insert(0, 7)
    print(my_list)
    print(my_list.slice_list(4, 6))