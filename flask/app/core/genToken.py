import secrets
import qrcode.image.svg
import qrcode
import os

def genToken():
    return ''.join(secrets.token_urlsafe(16))

print(genToken())

def genQRCode(token, revoked=False):
	qr = 'app/templates/static/token/qrcode.svg'
	if revoked:
		os.remove(qr)
	if not os.path.exists(qr):
		factory = qrcode.image.svg.SvgImage
		img = qrcode.make(token, image_factory=factory)
		img.save(qr)
		print(type(img))
		

	else:
		os.remove(qr)