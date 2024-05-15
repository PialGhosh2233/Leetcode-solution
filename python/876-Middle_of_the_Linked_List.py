# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        list=[]
        while current!=None:
            list.append(current.val)
            current = current.next
        if len(list)%2==0:
            index = (len(list)+1)//2
        else:
            index = (len(list))//2
        for i in range(index,len(list)):
            new_node = ListNode(list[i])
            if i == index :
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node
        return head