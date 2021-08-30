import gmpy2
from Crypto.Util.number import bytes_to_long,long_to_bytes
from gmpy2 import invert


p = gmpy2.mpz(473398607161)
q = gmpy2.mpz(4511491)
L = (p-1) *(q-1)
e = gmpy2.mpz(17)
d = gmpy2.invert(e,L)
print d

