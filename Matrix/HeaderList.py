from Matrix.HeaderNode import HeaderNode

class HeaderList:
    def __init__(self):
        self.first = None
        self.last = None

    def insertNode(self,index):
        if self.first:
            if index < self.first.index:
                self.first.prev = HeaderNode(index)
                self.first.prev.next = self.first
                self.first = self.first.prev
            elif index > self.last.index:
                self.last.next = HeaderNode(index)
                self.last.next.prev = self.last
                self.last = self.last.next
            else:
                current = self.first
                while current.next:
                    if index > current.index and index < current.next.index:
                        temp = HeaderNode(index)
                        temp.prev = current
                        temp.next = current.next

                        current.next.prev = temp
                        current.next = temp
                        return
                    current = current.next
            return
        self.first = HeaderNode(index)
        self.last = self.first

    def isHearIndex(self,index):
        if self.first:
            current = self.first
            while current:
                if current.index == index:
                    return True
                current = current.next
            return False

    def print(self):
        current = self.first
        w = ''
        while current:
            w += f'{current.index}'
            current = current.next
        print(w)