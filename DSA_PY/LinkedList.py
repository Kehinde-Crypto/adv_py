# goes through a linked list  read , modify and delate the node 

class Node:
  def __init__(self , data):
    self.data = data
    self.next = None
    def traversalAndPrint(head):
      currentNode = head
      while currentNode:
        print(currentNode.data , end = "->")
        currentNode = currentNode.next  
        print("null")
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traversalAndPrint(node1)

# Finding the lowest value in a singly linked list in Python:

# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def findLowestValue(head):
#   minValue = head.data
#   currentNode = head.next
#   while currentNode:
#     if currentNode.data < minValue:
#       minValue = currentNode.data
#     currentNode = currentNode.next
#   return minValue

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print("The lowest value in the linked list is:", findLowestValue(node1))
# usng the delete feature with python in linked list
# def deleteSpecificNode(head, nodeToDelete):
#   if head == nodeToDelete:
#     return head.next

#   currentNode = head
#   while currentNode.next and currentNode.next != nodeToDelete:
#     currentNode = currentNode.next

#   if currentNode.next is None:
#     return head

#   currentNode.next = currentNode.next.next

#   return head

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print("Before deletion:")
# traverseAndPrint(node1)
