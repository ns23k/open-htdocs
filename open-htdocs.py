from os import path
import os
import time


_ = None
print("finding xampp.....")
if path.isdir("C:\\Program Files (x86)\\xampp"):
    _ = "C:\\Program Files (x86)\\xampp\\htdocs"
    print("searching C:\\Program Files (x86)\\xampp")
    time.sleep(0.2)
elif path.isdir("C:\\Program Files\\xampp"):
    _ = "C:\\Program Files\\xampp\\htdocs"
    print("searching C:\\Program Files\\xampp")
    time.sleep(0.5)
elif path.isdir("C:\\xampp"):
    _ = "C:\\xampp\\htdocs"
    print("searching C:\\xampp")
    time.sleep(0.2)
elif path.isdir("E:\\xampp"):
    print("searching E drive")
    time.sleep(0.5)
    _ = "E:\\xampp\\htdocs"
else:
    print("xampp not found lmao loser")
    time.sleep(5)
    quit()


print(f"found xampp {_}")
print("opening htdocs")
os.system(f"explorer {_}")
    
time.sleep(5)
