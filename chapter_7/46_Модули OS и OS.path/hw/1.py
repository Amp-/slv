import os, os.path


os.makedirs("./Test/A/A1/",exist_ok=True)
os.makedirs("./Test/A/A2/",exist_ok=True)
os.makedirs("./Test/B/",exist_ok=True)
os.makedirs("./Test/C/",exist_ok=True)

if (os.path.exists("./Test/A/A1/") == True):
    with open("./Test/A/A1/Test1.txt","w") as f:
        f.write("")
if (os.path.exists("./Test/A/A2/") == True):
    with open("./Test/A/A2/Test2.txt","w") as f:
        f.write("")
if (os.path.exists("./Test/B/") == True):
    with open("./Test/B/Test3.txt","w") as f:
        f.write("")
if (os.path.exists("./Test/") == True):
    with open("./Test/Test4.txt","w") as f:
        f.write("")

for root, dirs, files in os.walk("./Test"):
    for t in dirs:
        if(dirs != []):
            print(f"Is dirs: {t}")

for root, dirs, files in os.walk("./Test"):
    for t in files:
        if(files != []):
            print(f"Is file: {t}")
