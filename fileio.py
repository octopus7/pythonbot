#-*- coding: utf-8 -*-
import os

f = open("test.txt", 'w')
for i in range(1, 11):
    data = "%dlines.\n" % i
    f.write(data)

# split 은 space 도 인지

pypath = os.path.realpath(__file__)
f.write(pypath+"\n")
pypath = os.path.dirname(os.path.abspath(__file__))
f.write(pypath+"\n")
f.close()

with open('test.txt') as f:
    lines = f.read().split()
    print("idx 0:"+lines[0])
    print("idx 1:"+lines[1])
