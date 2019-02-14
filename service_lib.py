import os
import subprocess


def check_internet(ip):
    print('Check for %s' % ip)
    response = os.system('ping -c5 %s' % ip)
    if response == 0:
        return(True)
    else:
        print('response - ', response)
        return(False)


def ping(ip):
    process = subprocess.Popen(['ping', '-c', '5', ip], stdout=subprocess.PIPE)
    raw_res = process.communicate()[0]
    if raw_res != None:
        return raw_res
    else: return 'Empty answer'