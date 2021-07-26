import pyqrcode
from pyqrcode import QRCode
import time
#when you scan the qr code , you'll be redirected to the link here.
content =  input('Input a link to be redirected while you scan the qr code')
  
url = pyqrcode.create(content)
scl = input('Input scale for your qr code(Recommended - 5)')
qrname = input('Input a name for your qr code with file extention (Eg- .png)')
url.png(qrname, scale = scl) 

print('Qr code Generating ... ')
time.sleep(1)
print('Done !')
