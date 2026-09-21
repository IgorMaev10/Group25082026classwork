import pyotp
import qrcode

secret = 'testsecret88888888sytghefdargyfdf'

totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(
    name='johndoe@test.com',
    issuer_name='RandomApp',
    image='https://png.pngtree.com/png-clipart/20220604/ourmid/pngtree-gradient-circle-text-box-prmotion-sale-banner-png-image_4852602.png'
)

qr = qrcode.make(uri)
qr.show()
qr.save("qr.png")

otp_user = input('enter otp: ')
is_valid = totp.verify(otp_user)
print(is_valid)