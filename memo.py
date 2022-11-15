from datetime import datetime

class Memo:
    def __init__(self,memo,date, time):
        self.memo=memo
        self.date=date
        self.time=time



def main(n,l):
    if(n==1):
        memo=input("Enter the memo: ")
        l.append( Memo(memo,datetime.now().strftime("%Y-%m-%d"), datetime.now().time().strftime("%H:%M:%S")), )

    elif(n==2):
        print("Click 'a' to view all the memo")
        print("click 'i' to view the Memo by index")
        ip=input()
        if(ip=='a'):
            for i in l:
                print("The memo is: ",i.memo, ' and the date is {} while the time for the memo is {}: '.format(i.date,i.time) )
        elif(ip=='i'):
            x=int(input("Enter the index of memo to view (you can type the index from: {} to {})".format(0,len(l)-1)))
            print("The memo is: ",l[x].memo, ' and the date is {} while the time for the memo is {}: '.format(i.date,i.time))
        else:
            return

    elif(n==3):
        x=int(input("Enter the index of memo to edit: "))
        print("The memo is: ",l[x].memo)
        memo=input("Enter the new memo: ")
        y=input("Enter 'y' you really want to edit the memo")
        if(y.lower()=='y'):
            l[x]=Memo(memo,datetime.now().strftime("%Y-%m-%d"), datetime.now().time().strftime("%H:%M:%S"))
        else:
            return

    elif(n==4):
        print("Click 'a' to delete all the memo")
        print("click 'i' to delete the Memo by index")
        ip=input()
        if(ip=='a'):
            for i in l:
                print("The memo is: ",i.memo, ' and the date is {} while the time for the memo is {}: '.format(i.date,i.time))
            y=input("Enter 'y' you really want to delete the memo: ")
            if(y.lower()=='y'):
                l.clear()
            else:
                return
            
        elif(ip=='i'):
            x=int(input("Enter the index of memo to delete: "))
            print("The memo is: ",l[x].memo)
            y=input("Enter 'y' you really want to delete the memo: ")
            if(y.lower()=='y'):
                l.remove(l[x])
            else:
                return
        else:
            return
        






    
n=0
l=[]
while(n!=5):
    print("Enter 1 to add a new Memo")
    print("Enter 2 to read the Memo")
    print("Enter 3 to edit the Memo")
    print("Enter 4 to delete Memo")
    print("Enter 5 to exit")
    n=int(input('Enter the operation: '))
    
    main(n,l)
