class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, root) -> None:
        self.root = root

    def prepend(self, val: any) -> None:
        new_node = Node(val)
        tmp = self.root
        new_node.next = tmp
        self.root = new_node

    def popleft(self) -> None:
        tmp = self.root
        tmp = tmp.next
        self.root = tmp

    def output(self) -> list:
        ll = []
        tmp = self.root
        while tmp:
            ll.append(tmp.val)
            tmp = tmp.next
        return ll

    def search(self, key: any) -> bool:
        tmp = self.root
        while tmp:
            if tmp.val == key:
                return True
            tmp = tmp.next
        return False

    def insert_after(self, key: any, value: any) -> None:
        tmp = self.root
        while tmp:
            if tmp.val == key:
                new_node = Node(value)
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next

    def delete_after(self, key):
        tmp = self.root
        while tmp:
            if tmp.val == key:
                if tmp.next:
                    tmp.next = tmp.next.next
                else:
                    break
            tmp = tmp.next

if __name__ == "__main__":
    pass
