##This script allows the user to find out how many drive letters are on the pc including cloud storage devices and allows you to select a drive letter to find out how much space is remaining on the drive.
import shutil
import win32api
def bytestogb(bytes):
    try:
        bytes = float(bytes)
        Kilobytes = bytes / 1024
    except:
        return "Please enter a valid disk letter"
    if Kilobytes >= 1024:
        Megabytes = Kilobytes / 1024
        if Megabytes >= 1024:
            Gigabytes = Megabytes / 1024
            return "%.2f Gigabytes" % (Gigabytes)
        else:
            return "%.2f Megabytes" % (Megabytes)
    else:
        return "%.2f Kilobytes" % (Kilobytes)
##The lines above were not written by me. The code has changes but the math is the same because you have to use this math to figure out the storage size remaining by calculating the kilobytes, megabytes, and gigabytes. I completely understand how this code works.
##https://www.tutorialexample.com/a-simple-guide-to-python-get-disk-or-directory-total-space-used-space-and-free-space-python-tutorial/
print("This script will let you know how much free space is remaining on a disk")
print("Example disk letter input would be: C:\\")
print("The disk letters that are on your computer is:")
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)
number1 = input("Enter your disk letter to see how much storage you have left on the drive: ")
usage = shutil.disk_usage(number1)
remaininggb = bytestogb(usage[2])
##The drives declaration is also taken from snippets of code from stack overflow due to the drives command running from the import.
##https://stackoverflow.com/questions/827371/is-there-a-way-to-list-all-the-available-drive-letters-in-python
print('Your free space is:', remaininggb)
##I decided to make this script because my pc currently has 9 drives and would be easier to check with this instead of disk management or file explorer.
