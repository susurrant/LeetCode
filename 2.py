"""
2. Add Two Numbers
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        tag = 0
        while True:
            if l1 or l2:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0
                temp = v1 + v2 + tag

                if temp >= 10:
                    tag = 1
                    result.append(temp % 10)
                else:
                    tag = 0
                    result.append(temp)

                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            else:
                if tag:
                    result.append(1)
                break

        p = ListNode(result[-1])
        for i in range(len(result) - 2, -1, -1):
            temp =  ListNode(result[i])
            temp.next = p
            p = temp

        return p

def create_list(vals):
    print(vals)
    p = ListNode(vals[-1])
    for i in range(len(vals)-2, -1, -1):
        temp = ListNode(vals[i])
        temp.next = p
        p = temp
    print_list(p)
    return p

def print_list(l):
    while True:
        print(l.val)
        if l.next:
            l = l.next
        else:
            break

if __name__ == '__main__':
    l1 = create_list([5])
    l2 = create_list([5])

    print('result:')
    s = Solution()
    print_list(s.addTwoNumbers(l1, l2))

