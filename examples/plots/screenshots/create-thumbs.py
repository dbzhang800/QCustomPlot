#!/usr/bin/env python
import os, shutil, distutils.dir_util, sys, subprocess

os.chdir(sys.path[0]); # change current working dir to script dir

if not os.path.isdir("./thumbs"):
  os.mkdir("./thumbs");
elif len(os.listdir("./thumbs")) > 0:
  if raw_input("Warning: ./thumbs not empty! Continue anyway? (y/n): ") != "y":
    sys.exit();

#sizes = ["264x200"];
sizes = ["220x168"];

for fileName in os.listdir("./"):
  if os.path.isfile(fileName) and "." in fileName and fileName.split(".")[1] == "png":
    print "processing "+fileName;
    for size in sizes:
      subprocess.call("convert -resize "+size+" "+fileName+" -sharpen 0x1 ./thumbs/"+fileName.split(".")[0]+"-thumb.png", shell=True);
    #subprocess.call("convert -crop 548x288+0+66 "+fileName+" ./thumbs/"+fileName.split(".")[0]+"-548x288.png", shell=True);
    shutil.copy2("./"+fileName, "./thumbs");

#  f = open("main.cpp", "r");
#  content = f.read();
#  f.close();
#  content = content.replace("q"+name.lower()+"hash.h", "../q"+name.lower()+"hash.h");
#  f = open("main.cpp", "w");
#  f.write(content);
#  f.close();



