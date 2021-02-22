import shutil
import win32api
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "Please enter a vlid disk letter"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)
print("This script will let you know how much free space is remaining on a disk")
print("Example disk letter input would be: c://")
print("The disk letters that are on your computer is:")
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)
number1 = input("Enter your disk letter to see how much storage you have left on the drive: ")
usage = shutil.disk_usage(number1)
free_space = formatSize(usage[2])
print('Your free space is:', free_space)

