import os

print(os.getcwd())

print(os.listdir())

os.mkdir("test_folder")

os.mkdirs("parent/child")

os.rmdir("test_folder")

os.removedirs("parent/child")

with open("file.txt","w")as f:
    f.write("hello")

os.remove("file.txt")

os.rename("old.txt","new.txt")

os.path.exists("file.txt")

os.path.getsize("file.txt")

os.path.join("folder","file.txt")


