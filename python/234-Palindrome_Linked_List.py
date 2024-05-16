# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current_node = head
        list=[]
        while current_node !=None:
            list.append(current_node.val)
            current_node = current_node.next
        if list == list[::-1]:
            return True
        else:
            return False    