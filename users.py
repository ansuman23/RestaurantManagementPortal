import items

def validate(pwd):
    a=0
    b=0
    c=0
    d=0
    if len(pwd)>=6:
        for i in pwd:
            if i.isdigit():
                a+=1
            elif i.islower():
                b+=1
            elif i.isupper():
                c+=1
            elif i=='!'or i=='@'or i=='#' or i=='*' or i=='%':
                d+=1
        if a>=1 and b>=1 and c>=1 and d>=1:
            return 'valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'
    
def login():
    print("="*50,"Customer Page","="*50)
    print(" "*100)
    print("1.New User\n2.Existing User")
    n=int(input("enter 1 or 2: "))
    if n==1:
        name=input("enter your name: ")
        print("password must contain\natleast 6 characters \natleast one digit\natleast one lower case and atleast one upper case\natleast one special character")
        password=input("enter password: ")
        p=validate(password)
        while p!='valid':
            print("Choose a valid password")
            password=input("enter password: ")
            p=validate(password)
        detail=name+','+password+'\n'
        print("-"*20,"Account created successfully","-"*20)
        fp=open('customer.txt','a')
        fp.write(detail)
        fp.close()
        items.itemlist()
    elif n==2:
        name=input("enter name: ")
        password=input("enter password: ")
        detail=name+','+password+'\n'
        fp=open('customer.txt','r')
        c=fp.readlines()
        fp.close()
        for i in c:
            if detail in i:
                print("*"*40,"Login Successful","*"*40)
                print(" "*100)
                items.itemlist()
                break
        else:
            print("Invalid Credentials")
            
        
