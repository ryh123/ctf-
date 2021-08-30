# -*- coding: UTF-8 -*- 

c = int(raw_input("Enter c(int): "))
d = int(raw_input("Enter d(int): "))
n = int(raw_input("Enter n(int): "))
#c=0x1e2
#d=12ab
#n=14ce
print c
print d
print n
print ('%x' % pow(c,d,n)).decode('hex')


