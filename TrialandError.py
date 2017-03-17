from List import StudentInfo
from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
from time import mktime



StudentName=['Abel','Diego']
StudentNumbers=[1126, 1134]
Joined= zip(StudentName,StudentNumbers)
flag=True

number=StudentInfo.keys()
name=StudentInfo.values()

jkl ={
    234:"x",
    345:"y"
}

morn= time(4, 0, 1)
after = time(5,0,2)
now = time()


today=date.today()
fg= date(today.year,4,1)
yuh = str(datetime.now())
#localtime = time.localtime(time.time())
Time=("{:%H:%M}".format(datetime.now()))
#Timer=int(Time)
settime = ("{:%H:%M}".format(time(8,30)))
tester="6:30"
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
                
                
def checker():
    #print '#'
    x= int(raw_input("Enter Student Number: "))
    if x == 3:
        print "madeit"
    