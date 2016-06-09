class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def __init__(self,data):
		self.head=Node(data)
		self.ref=self.head
	def add(self,data):
		n=Node(data)
		self.ref.next=n
		self.ref=n
