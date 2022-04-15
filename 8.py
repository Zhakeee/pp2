import os
if os.path.exists('C:\dir'):
    for i in os.listdir():
        os.remove('C:\dir')
else:
    print("file doesn't exist")