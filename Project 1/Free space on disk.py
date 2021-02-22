import shutil
import win32api
def bytestogb(bytes):
    try:
        bytes = float(bytes)
        kilo = bytes / 1024
    except:
        return "Please enter a valid disk letter"
    if kilo >= 1024:
        Megabytes = kilo / 1024
        if Megabytes >= 1024:
            Gigabytes = Megabytes / 1024
            return "%.2fG" % (Gigabytes)
        else:
            return "%.2fM" % (Megabytes)
    else:
        return "%.2fkb" % (kilo)
##The lines above were not written by me. The code has slight changes but is similar to the source
#https://www.tutorialexample.com/a-simple-guide-to-python-get-disk-or-directory-total-space-used-space-and-free-space-python-tutorial/
print("This script will let you know how much free space is remaining on a disk")
print("Example disk letter input would be: C:\\")
print("The disk letters that are on your computer is:")
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)
number1 = input("Enter your disk letter to see how much storage you have left on the drive: ")
usage = shutil.disk_usage(number1)
remaininggb = bytestogb(usage[2])
##the drives declaration is also taken from snippets of code from stack overflow due to the drives command running from the import
##https://stackoverflow.com/questions/827371/is-there-a-way-to-list-all-the-available-drive-letters-in-python
print('Your free space is:', remaininggb)