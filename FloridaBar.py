import webbrowser, sys, pyperclip
#Windows Key R
sys.argv

#CHECK IF COMMAND LINE ARGUMENTS WERE PASSED

if len(sys.argv) >1:
    #['mapit.py', '870', 'Valencia', 'St.']  
    firstName = (sys.argv[1])
    lastName = (sys.argv[-1])
else:
    fullName = pyperclip.paste()
    fullName = list(fullName.split(" "))
    print (fullName)
    firstName = fullName[0]
    lastName = fullName[-1]
    print (firstName)
    print (lastName)

webbrowser.open("https://www.floridabar.org/directories/find-mbr/?lName=" +lastName + " +&sdx=N&fName=" + firstName)
                
