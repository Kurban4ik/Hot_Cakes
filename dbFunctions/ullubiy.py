from dbFunctions.muslim import add_worker
import qrcode
import sqlite3
from random import sample

host = 'http://ec83-176-120-220-18.ngrok.io/'

def qr(name, company):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    uniq = ''.join(sample([i for i in a], len(a)))
    guy_slug = f'{host}{company}/' + uniq
    add_worker(name, guy_slug, company)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=2,
    )
    qr.add_data(guy_slug)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'../templates/{uniq}.jpg')
    return f'../templates/{uniq}.jpg'
