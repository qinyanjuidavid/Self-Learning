file=open("file.txt","w")
try:
    file.write("What are... you doing?")
finally:
    file.close()
file=open('file.txt','r')
try:
    f=file.readlines()
    print(f)
finally:
    file.close()
#With is the context manager
with open("file.txt","w") as file:
    file.write("Who are you..?")
    file.close()
#Context manager
class File:
    def __init__(self,filename,method):
        self.file=open(filename,method)
    def __enter__(self):
        print("Enter")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type}, {exc_val} {exc_tb}")
        print("Exit")
        self.file.close()
        # if type == Exception:
        return True

with File("file.txt", "w") as f:
    print("middle")
    f.write("hello!")
    raise FileExistsError()

import contextlib
from contextlib import contextmanager
@contextmanager
def file(filename,method):
    file=open(filename,method)
    yield file
    file.close()
with file("text.txt","w") as f:
    print("middle")
    f.write("hello")

