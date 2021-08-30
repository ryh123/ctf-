#coding:utf-8

from Crypto.PublicKey import RSA
import gmpy2
import rsa

#1.从公钥文件中分解n和e
public_key = RSA.importKey(open("pubkey.pem").read())  #读取pubkey.pem文件
n = public_key.n
e = public_key.e
#print("n=\n%s\ne=\n%s"%(n,e))

#2.在线分解n得到p和q
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239

#3.计算出d
d = int(gmpy2.invert(e, (p-1)*(q-1)))
#print(d)

#通过已知条件，生成私钥，并解密密文
private_key = rsa.PrivateKey(n, e, d, p, q)#生成私钥
with open("./tmp/flag.enc") as f:
    flag = rsa.decrypt(f.read(), private_key)
    print(flag)
    #print(rsa.decrypt(f.read(), private_key).decode())