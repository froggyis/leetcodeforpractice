# Definition for singly-linked list.
def traverse(node):
	print(node.val)
	if(node.next != None):
		traverse(node.next)

def delete(node):
	node.val = node.next.val
	node.next = node.next.next

class ListNode:
	def __init__(self):
         self.val = None
         self.next = None

node0 = ListNode()
node1 = ListNode()
node2 = ListNode()
node3 = ListNode()

node0.next = node1
node1.next = node2
node2.next = node3

node0.val = 4
node1.val = 5
node2.val = 1
node3.val = 9

print("before")
traverse(node0)
print("after")
delete(node1)
traverse(node0)