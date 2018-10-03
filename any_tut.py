lines  = ["trees are good", "pool is fresh", "face is round"]
website_list = ["face", "clock", "trend"]

for line in lines:
     if not any(website in line for website in website_list):
         print(line)
     
