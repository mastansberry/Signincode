from List import StudentInfo

number=StudentInfo.keys()
name=StudentInfo.values()
loopcity=True
Time=("{:%H:%M}".format(datetime.now()))
settime = ("{:%H:%M}".format(time(8,30)))


def Login():
    while loopcity == True:
        StudentID = int(raw_input("what is your ID number: "))
        if StudentID in number:
            print StudentInfo.get(StudentID)
        else:
            print "Not in our system, check with Admin"
              
def math():
    if "2:40" < "4:40":
        print "yes"
        
def trash():
    if Time < settime:
        print Time, settime
        print "yes"
    else:
        print Time, settime
        print "no"
def Timecheck():
    if Time > '{8:30:00}'.format(datetime()):
        print "yes"

def Login():
    StudentID = int(raw_input("what is your ID number: "))
    if StudentID in number:
      print StudentInfo.get(StudentID)  


def Try():
    StudentID = int(raw_input("what is your ID number: "))
    print StudentID
    print number
    if StudentID in number:
      print StudentInfo.get(StudentID)  

def greeting(xx):
    return jkl[xx]


def CheckIn():
    StudentPresent=[]
    if flag==True:
        print "What student are you?"
        StudentID = int(raw_input())
        if StudentID in StudentNumbers:
            StudentPresent += [StudentID]
            print "StudentPresent"
            print StudentPresent
            if StudentID in Joined:
                print 'yes' #Joined[StudentName]
                
