"""
-> Design HashSet 

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:
• Void add(key) insets the value key into the hashSet.
• Bool contains(key) Returns whether the value key exists in the HashSet or not.
• void remove(key) Removes the value key in the HashSet. if key does not exist in the HashSet, do nothing.

"""

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
    
    def add(self, key: int) -> None:
        curr = self.set[key % len(self.set)] # head index

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)
    
    def remove(self, key: int) -> None:
        curr = self.set[key % len(self.set)]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key % len(self.set)]
        
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


