import os
import shutil
from_dir = "/Users/alvindo/Desktop/Downloads"
to_dir= "/Users/alvindo/Desktop/Document_Files"

listoffiles = os.listdir(from_dir)
for filename in listoffiles:
    name,ext=os.path.splitext(filename)
    path1=from_dir+'/'+filename
    path2=to_dir+'/'+"Document_Files"
    path3=to_dir+'/'+"Document_Files"+'/'+filename
    if os.path.exists(path2):
        print("moving")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("moving")
        shutil.move(path1,path3)

