from List import StudentInfo

number=StudentInfo.keys()
name=StudentInfo.values()
loopcity=True
def Login():
    while loopcity == True:
        StudentID = int(raw_input("what is your ID number: "))
        if StudentID in number:
            print StudentInfo.get(StudentID)
        else:
            print "Not in our system, check with Admin"
              
