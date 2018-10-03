import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","fb.com","secure-surf.net","www.pornhub.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(hosts_path, "r+") as hst:
            content = hst.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hst.write(redirect + "       " + website + "\n")
    else:
        with open(hosts_path, "r+") as hst:
            content = hst.readlines()
            hst.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hst.write(line)
            hst.truncate()
            
            
    time.sleep(5)
    print("Work")