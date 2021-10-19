import pyqrcode
import png
from pyqrcode import QRCode
qrstring="https://developer.mozilla.org"
url=pyqrcode.create(qrstring)
url.png('myfirstqrcode ',scale = 8)