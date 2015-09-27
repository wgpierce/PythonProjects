from mimetypes import _winreg
import shutil

def main():
    #Delete from Registry
    try:
        Key_Name = 'Software\Hyper Hippo Productions Ltd.\AdVenture Capitalist!'
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, Key_Name, 0, _winreg.KEY_ALL_ACCESS)
        _winreg.DeleteValue(key, 'GameState_Earth_h3453209545')  #May need to be changed-  key may not have same name
        _winreg.CloseKey(key)
        print "Key successfully deleted"
    except:
        print "Registry key already deleted."
        
    #Delete from Filesystem
    try:
        shutil.rmtree('C:\Program Files (x86)\Steam\userdata\\106831024\\346900') #Needs to be changed to each user
        print "Folder successfully deleted"
    except:
        print "Save file folder already deleted."
        
        
if __name__ == '__main__':
    main()