import os
if os.path.exists("C:\dir"):
    for i in os.listdir():
        print(i)