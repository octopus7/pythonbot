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
# crontab 실행시 사용자 홈으로 가기때문에 동일한 경로 접근을 위해서 __file__ 경로를 얻어온다
# c1
# c2

with open('test.txt') as f:
    lines = f.read().split()
    print("idx 0:"+lines[0])
    print("idx 1:"+lines[1])
