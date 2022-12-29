from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# helper functions:
def make_linked_list(inputList: list):
    # Strategy: Make a ListNode for each element from back to front, attaching as we go.
    # 1. Make last element into ListNode first.
    currentListNode = ListNode(inputList[-1])
    # 2. Attach each next element until we get through them all
    for element in reversed(inputList[:-1]):
        newListNode = ListNode(element)
        newListNode.next = currentListNode
        currentListNode = newListNode
    # The final current node should be the node made from the element at the front of the list, thus this is our linked list
    return currentListNode


def print_linked_list(linkedList: ListNode):
    print(linkedList.val)
    while(linkedList.next):
        linkedList = linkedList.next
        print(linkedList.val)


# - APPROACHES - 

# 1. Single Loop Using Linked List:

# This solution to the "Add Two Numbers" problem involves creating a linked list to store the sum of the two input linked lists.

# The solution starts by initializing an empty output linked list and a current node to keep track of the current node being worked on. It also initializes a carry variable to store any carry-over value from previous additions and a sum variable to store the current sum.

# The solution then enters a loop that will continue as long as either of the input linked lists has more nodes, or the carry variable is non-zero. Inside the loop, the solution extracts the values of the current nodes of the input linked lists, or sets them to zero if the input lists have run out of nodes. It then calculates the sum of these values and the carry variable, and sets the carry variable to the tens digit of the sum. The current node's value is set to the ones digit of the sum.

# The solution then advances to the next nodes in the input linked lists, if they exist. If the input linked lists have more nodes or the carry variable is non-zero, the solution creates a new node for the output linked list and sets current to point to it.

# Finally, the solution returns the output linked list.

# This solution has a time complexity of O(n) because it only needs to iterate through the input linked lists once, where n is the total number of nodes in the input lists. The space complexity is also O(n) because the size of the output linked list is proportional to the size of the input lists.


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = output = ListNode()
        carry = 0

        # while there are values to make nodes with, make them
        while l1 or l2 or carry:
            # default to zero val if either nodes run out
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            # set carry for nexts and current value off tens
            carry, current.val = divmod(l1Val + l2Val + carry, 10)

            # step to next nodes if lists have more nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # only make next node for output if one is needed
            if l1 or l2 or carry:
                current.next = ListNode()
                current = current.next

        return output
    
# ****************************************************************
# ================================================================
# ****************************************************************

# 2. Single Loop Using Stack:

# This solution to Leetcode #2 ("Add Two Numbers") is a linked list implementation that takes two input linked lists l1 and l2 representing non-negative integers, and returns a new linked list representing the sum of the two input integers.

# The solution first creates two empty stacks, stack1 and stack2, to store the digits of the input linked lists in reverse order. It then iterates over the elements of l1 and l2, appending the digits to the respective stacks.

# Next, the solution reverses the elements in stack1 and stack2 using the reversed function and the list constructor. This step is necessary because the input linked lists are given in forward order (i.e., the most significant digit is at the head of the list), but the solution processes the digits in reverse order (i.e., the least significant digit is at the top of the stack).

# After reversing the elements of the stacks, the solution initializes the output and current variables to a new ListNode, and the carry variable to 0. It then enters a loop that continues as long as there are digits in either stack or a carry value is present.

# Inside the loop, the solution pops the top element from each stack (defaulting to 0 if the stack is empty), and adds them together with the carry value. It then updates the carry and current.val variables using the divmod function, which returns a tuple containing the quotient and remainder of the division. The carry variable is set to the quotient, and the current.val variable is set to the remainder.

# Finally, the solution checks if there are any more digits in either stack or a carry value is present, and if so, it creates a new ListNode and sets it as the current.next node. This continues until all the digits have been processed and the final ListNode has been created. The solution then returns the output linked list.

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # create stacks to store the digits of the input linked lists in reverse order
#         stack1 = []
#         stack2 = []

#         # push the digits onto the stacks
#         while l1:
#             stack1.append(l1.val)
#             l1 = l1.next
#         while l2:
#             stack2.append(l2.val)
#             l2 = l2.next

#         stack1 = list(reversed(stack1))
#         stack2 = list(reversed(stack2))

#         # create the output linked list and initialize the carry variable
#         output = current = ListNode()
#         carry = 0

#         # while there are digits in either stack, pop and add them
#         while stack1 or stack2 or carry:
#             # default to zero if either stack is empty
#             d1 = stack1.pop() if stack1 else 0
#             d2 = stack2.pop() if stack2 else 0
#             carry, current.val = divmod(d1 + d2 + carry, 10)

#             # only make next node for output if one is needed
#             if stack1 or stack2 or carry:
#                 current.next = ListNode()
#                 current = current.next

#         return output


# ****************************************************************
# ================================================================
# ****************************************************************

# 3. Convert To and From Int:

# Another alternative approach is to convert the input linked lists to integers, perform the addition using standard integer arithmetic, and then convert the result back to a linked list.

# This solution has a time complexity of O(n) and a space complexity of O(n), where n is the number of digits in the sum of the input integers. The conversion of the linked lists to integers and back again adds some additional overhead, but this may be acceptable depending on the constraints of the problem.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # convert the input linked lists to integers
        num1 = self.linked_list_to_int(l1)
        num2 = self.linked_list_to_int(l2)

        # convert the result back to a linked list
        return self.int_to_linked_list(num1 + num2)

    def linked_list_to_int(self, node: ListNode) -> int:
        # create a list of the node values in reverse order
        values = []
        while node:
            values.append(str(node.val))
            node = node.next

        # join the values in reverse order and convert to int
        return int(''.join(reversed(values)))

    def int_to_linked_list(self, num: int) -> ListNode:
        # convert the integer to a list of digits in reverse order
        digits = [int(d) for d in str(num)][::-1]
        digitsLen = len(digits)

        # create the output linked list
        output = current = ListNode()
        for i, digit in enumerate(digits):
            current.val = digit
            if not i == digitsLen - 1:
                current.next = ListNode()
                current = current.next

        return output


add_two_numbers_solver = Solution()


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]

# l1 = [2,4,9]
# # l2 = [5,6,4,9]

l1 = [5, 6]
l2 = [5, 4, 9]

# l1 = [2,4,3]
# l2 = [5,6,4]

l1 = make_linked_list(l1)
l2 = make_linked_list(l2)


output = add_two_numbers_solver.addTwoNumbers(l1, l2)


print_linked_list(output)
