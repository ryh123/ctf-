from Crypto.Util.number import *
msg1 = 0x123654AAA678876303555111AAA77611A321
msg2 = 0x123654AAA678876303555111AAA77611A321
print (hex(msg1 ^ msg2).upper())
s = bin(msg2)[6:]
print (s)
r=""
tmp = 0
for i in xrange(len(s)/2):
    c = s[i*2]
    if c == s[i*2 - 1]:
        r += '1'
    else:
        r += '0'
print (hex(int(r,2)).upper())