#!/usr/bin/python

class employee:
	def __init__(self,a,b):
		self.x=a
		self.y=b
	def print_data(self):
		print self.x
		print self.y

a=employee("rutul","25")

a.print_data()

