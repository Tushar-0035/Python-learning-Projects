"""for i in range(5):
    print(i,end= "" )
    if i==1:
        break
else:
    print("end")
"""

# l= [1,2,3]
# l.append([3,4])
# print(len(l))
# .........................QR CODE.............
import pyqrcode
import png
from pyqrcode import QRCode

link= "https://www.facebook.com/"

url = pyqrcode.create(link)
# url.svg("myqr.svg",scale=8)
url.png('myqr.png',scale=6)