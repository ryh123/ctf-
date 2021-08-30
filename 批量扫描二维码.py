from pyzbar.pyzbar import decode
from PIL import Image
def QRdecode(filepath):
     result = decode(Image.open(filepath))
     return result[0].data
if __name__ == "__main__":
    c = ''
    for i in range(1,576):
        a = QRdecode(r"C:\\Users\SAM\Desktop\QRcode\{0}.png".format(i))  #打开二维码文件
        a = str(a)
        a = a.replace('b','')     #去掉b
        if a == "'zero'":         #匹配二维码的内容
            a = '0'
        elif a == "'one'":
            a = '1'
        c+= a

print(c)

e = int(c)
print(e)