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
#��Ŀû�и�������ָ��e�����Ǹ��ݵͼ���ָ���㲥���������Բ�e=3��10��17��
e = 

#N1 = int(N1,5)
#ԭ���и�������5�����������Ա�Ϊʮ���ƣ���Ҫ�Ļ�������ôת


n = [N1,N2,N3]
c = [c1,c2,c3]
data = zip(n,c)
m_e = CRT(data)
m = gmpy2.iroot(m_e,e)[0]
print libnum.n2s(m)
