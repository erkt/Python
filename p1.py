#!/usr/bin/python

fh=open("data","r")


lines=fh.readlines()

fh.close()

c=0

for i in lines:
	c=c+1

print c
