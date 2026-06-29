# Design HashMap 
#Qno.6:- Design a HashMap without using any built-in hash table libraries

# Node class to store key-value pairs in linked list
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        # Create 1000 empty buckets, each with a dummy head node
        self.map = [ListNode() for i in range(1000)]

    def hash_func(self, key):
        # Simple hash function: divide key by number of buckets and take remainder
        return key % len(self.map)

    def put(self, key, value):
        # Find the bucket for this key
        cur = self.map[self.hash_func(key)]
        # Look through the linked list in this bucket
        while cur.next:
            if cur.next.key == key:
                # Key already exists, update its value
                cur.next.val = value
                return
            cur = cur.next
        # Key doesn't exist, add new node at end of list
        cur.next = ListNode(key, value)

    def get(self, key):
        # Find the bucket for this key
        cur = self.map[self.hash_func(key)].next
        # Look through the linked list for the key
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        # Key not found
        return -1

    def remove(self, key):
        # Find the bucket for this key
        cur = self.map[self.hash_func(key)]
        # Look through the linked list for the key
        while cur and cur.next:
            if cur.next.key == key:
                # Remove the node by skipping it
                cur.next = cur.next.next
                return
            cur = cur.next


    