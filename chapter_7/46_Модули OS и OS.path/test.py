import os

print(os.getcwd())
print(os.listdir("../"))


# os.mkdir("test")
# os.rmdir("test")
os.makedirs("test",exist_ok=True)
# os.removedirs("test")
#os.remove("filename")
#os.rename("filename")
#os.renames()
#os.replace()
#os.truncate()
for root, dirs, files in os.walk('../46_Модули OS и OS.path' ):
    print(f'root {root}')
    print(f'dirs {dirs}')
    print(f'file {files}')