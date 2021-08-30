# -*- coding: UTF-8 -*-
import gmpy2
import libnum

def CRT(data):
	sum = 0
	m = 1
	for n in data:
		m = m*n[0]
	for n,c in data:
		m1 = m/n
		mr = gmpy2.invert(m1,n)
		sum = sum+mr*m1*c
	return sum%m

#N,C
N1 = 
c1 = 
N2 = 
c2 = 
N3 =
c3 =
#题目没有给出加密指数e，但是根据低加密指数广播攻击的特性猜e=3、10、17等
e = 

#N1 = int(N1,5)
#原题中给出的是5进制数，所以变为十进制，需要的话可以这么转


n = [N1,N2,N3]
c = [c1,c2,c3]
data = zip(n,c)
m_e = CRT(data)
m = gmpy2.iroot(m_e,e)[0]
print libnum.n2s(m)
