"""
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_number(self, linked_list):
        number = ""
        value = linked_list.val
        nxt = linked_list.next
        while value is not None:
            number += str(value)
            if nxt is None:
                break
            value = nxt.val
            nxt = nxt.next
        
        return int(number[::-1])
    
    def str_to_linked_list(self, num_str):

        linked_list = ListNode(val=int(num_str[0]))
        node = linked_list
        
        for idx, s in enumerate(num_str[1:]):
            node.next = ListNode(val=int(s))
            node = node.next
        
        return linked_list
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        
        new_num = str(num1 + num2)[::-1]
        
        new_linked_list = self.str_to_linked_list(new_num)
        
        return new_linked_list