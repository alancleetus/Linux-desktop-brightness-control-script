# Linux-desktop-brightness-control-script
Python script for increasing and decreasing Linux desktop brightness using the xrandr command line utility.

Usage:
1. Make the python scripts executable using chmod command. (ex: chmod 755 ./incBrightness.py)
2. Make 2 keyboard shortcuts and link them to the python scripts
  ex: On my system CTRL+Left will run the command "python3 /decBrightness.py". This in turn decreases the brightness of all my monitors by 10%. Note: make sure to use absolute path to python scripts
  
Troubleshoot:
  Brightness will not change if:
   1. curr.txt does not exist in the same directory
      - rerunning the command should create the file
   2. curr.txt is not accessible/readable
      - change permission on file using chmod or other methods
   3. if brightness is >=100% or <=30%
      - this is expected 
