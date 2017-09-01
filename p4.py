#!/usr/bin/python

my_list=["rutul","reni","ok","helllllo","o"]

c=0

for i in my_list:
	if len(i) > c:
		l_word=i
		c=len(i)

print "larger_word={0} and len={1}".format(l_word,c)	









