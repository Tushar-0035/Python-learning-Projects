import pyqrcode
import png
from pyqrcode import QRCode
Link="https://www.youtube.com/"
url = pyqrcode.create(Link)
url.png("myqr.png",scale=6)
url.svg("myqr.svg",scale=8)