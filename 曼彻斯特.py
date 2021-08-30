n=0x123654AAA678876303555111AAA77611A321
flag=''
bs='0'+bin(n)[2:]
r=''
def conv(s):
    return hex(int(s,2))[2:]
for i in range(0,len(bs),2):
        if bs[i:i+2]=='01':
            r+='1'
        else:
            r+='0'
for i in range(0,len(r),8):
    tmp=r[i:i+8][::-1]
    flag+=conv(tmp[:4])
    flag+=conv(tmp[4:])
print flag.upper()