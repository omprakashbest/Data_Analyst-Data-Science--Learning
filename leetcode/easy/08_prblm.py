# Middle of Linked List (Leetcode No.876)
# Given the head of a singly linked list return the middle node of the linked list.
# if there are two middle nodes, return the second middle node.

class Solution(object):
    def middle_Node(self, head): #head: Optional[ListNode]) -> Optional[ListNode]: also use that
        slow, fast = head, head # start both pointers at the head

        while fast and fast.next: # move until fast reaches the end
            slow = slow.next      # slow moves one step
            fast = fast.next.next # fast moves two steps
        return slow              # when fast is done, slow is at the middle


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val           # value of the node
        self.next = next         # pointer to the next node