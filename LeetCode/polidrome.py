       
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode("t", ListNode("a", ListNode("l", ListNode("i", ListNode("t", ListNode("a"))))))




class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
          

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next

        return True       
    
instance = Solution()
print (instance.isPalindrome(head))  