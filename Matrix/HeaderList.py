from Matrix.HeaderNode import NodeH

class HeaderList:
    def __init__(self):
        self.first : NodeH = None
        self.last : NodeH = None

    def add(self,index):
        if self.first:
            if index < self.first.index:
                self.first.previous = NodeH(index)
                self.first.previous.next = self.first
                self.first = self.first.previous
            elif index > self.last.index:
                self.last.next = NodeH(index)
                self.last.next.previous = self.last
                self.last = self.last.next
            else:
                current = self.first
                while current.next:
                    if index > current.index and index < current.next.index:
                        tmp = NodeH(index)
                        tmp.previous = current
                        tmp.next = current.next

                        current.next.previous = tmp
                        current.next = tmp
                        return

                    current = current.next
            return
        self.first = NodeH(index)
        self.last = self.first

    def isHearIndex(self,index):
        if self.first:
            current = self.first
            while(current):
                if current.index == index:
                    return True
                current = current.next
            return False

    def print(self):
        current = self.first
        w = ''
        while(current):
            w += f'{current.index}'
            current = current.next
        print(w)