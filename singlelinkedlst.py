class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
	
class singleLL:
	def __init__(self):
		self.head=None
		
	def get_length(self):
		n=self.head
		count=0
		while n is not None:
			count+=1
			n=n.next
		return count
		
	def add_begin(self,data):
		new_node=Node(data)
		new_node.next=self.head
		self.head=new_node
		
	def add_end(data):
		new_node=self.head
		if self.head is None:
			self.head=new_node
			
		else:
			n=self.head
			while n.next is not None:
				n=n.next
			n.next=new_node
			
	
			
			
		