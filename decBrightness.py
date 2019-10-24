import subprocess
import re

currBrightness = 1.0
path = "./curr.txt"

def saveBrightness():
    global currBrightness
    global path
    currFile = open(path, "w")
    currFile.write(str(currBrightness))
    currFile.close()
    print("saving", currBrightness)

def getOutputDevices():
    try:
        screens = []
        output = (subprocess.check_output(["xrandr","-q"]).decode("utf-8"))
        for match in re.finditer(r'(.*) connected', output):
            #print(match.group(1))
            screens.append(match.group(1))
        return screens
    except:
        print("Error: unable to get screens")
        return None

def changeBrightness():
    global currBrightness

    try:
        with open(path,"r") as content:
            currBrightness = content.read().split()[0]
            
            if float(currBrightness)>1.0:
                currBrightness = 1.0
                saveBrightness()
            elif float(currBrightness)<0.3:
                currBrightness = 0.3
                saveBrightness()

            if float(currBrightness)<=1.0 and float(currBrightness)>=0.0:
                screens = getOutputDevices()
                if screens:
                    if float(currBrightness)>=0.4:
                        currBrightness = float(currBrightness)-0.1
                    for screen in screens:
                        if float(currBrightness)>=0.3:
                            subprocess.call(["xrandr","--output",str(screen), "--brightness",str(currBrightness)])
                            print("dec")
                            saveBrightness()  
                else:
                    print("Error getting screens")            
            else:
                currBrightness = 1.0 
        
    except FileNotFoundError:
        saveBrightness()

changeBrightness()