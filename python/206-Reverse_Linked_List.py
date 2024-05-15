# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        list=[]
        while current !=None:
            list.append(current.val)
            current = current.next
        list.reverse()
        head = None
        current = None
        for i in list:
            new_node = ListNode(i)
            if head == None:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node
        return head        