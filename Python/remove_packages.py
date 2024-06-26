import os

def rem():
    pg = input("which program do you want to uninstall?: ")
    os.system("sudo yum remove " + pg + " -y")
    os.system("sudo yum autoremove")
rem()
