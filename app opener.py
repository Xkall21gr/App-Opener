import os
import subprocess
import time

#if you want to add more apps just copy from the try: to the time.sleep(0.5) and paste it exactly below or in what ored you like
def open_apps():  
    
    # Open the app
    try:
        subprocess.Popen(r" ") #add your path to the exe file of the app (all the path) inside the (" ")
    except FileNotFoundError:
        print("(put the name of the app) not found. Please check the path.") #prints this error if not oppened
        time.sleep(0.5)  # Delay for 500 milliseconds (change it to what you like)

if __name__ == "__main__":
    open_apps()