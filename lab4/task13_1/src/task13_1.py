class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, root) -> None:
        self.root = root

    def push(self, val: int) -> None:
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)

    def output(self) -> list:
        ll = []
        tmp = self.root
        while tmp:
            ll.append(tmp.val)
            tmp = tmp.next
        return ll

    def is_empty(self) -> bool:
        tmp = self.root
        if tmp is None:
            return True
        else:
            return False

    def pop(self):
        tmp = self.root
        if tmp.next:
            while tmp.next.next:
                tmp = tmp.next
            tmp.next = None
        else:
            self.root = None


if __name__ == "__main__":
    pass
