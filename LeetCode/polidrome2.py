class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# Accept input from user
input_list = input("Enter a list of integers separated by commas: ")
input_list = [int(x) for x in input_list.split(",")]

# Create a linked list from the input list
head = None
for i in reversed(input_list):
    head = ListNode(i, head)

# Check if linked list is a palindrome
instance = Solution()
print(instance.isPalindrome(head))