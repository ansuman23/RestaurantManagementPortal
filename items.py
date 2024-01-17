import random


def add():
    fp=open("items.txt",'a')
    item_no=input("enter item no.: ")
    item_name=input("enter item name: ")
    item_price=input("enter item price: ")
    fp1=open("items.txt",'r')
    c=fp1.readlines()
    fp1.close()
    temp=0
    for i in c:
        i=i.rstrip().split(',')
        if item_no==i[0]:
            print("-"*50,"This item no. already exists.\n Try a unique item no.","-"*50)
            break
        else:
            temp+=1
    if temp==len(c):
        detail=item_no+','+item_name+','+item_price+'\n'
        fp.writelines(detail)
        print("-"*50,"Item added Successfully","-"*50)
        fp.close()
    else:
        pass

    
def delete():
    fp=open("items.txt",'r')
    c=fp.readlines()
    for i in c:
        i=i.rstrip().split(',')
        print(i[0],'---->',i[1],'---->',i[2])
    fp1=open("items.txt",'w')
    item_no=input("enter item no. to be deleted: ")
    for i in c:
        l=i.rstrip().split(',')
        if l[0]!=item_no:
            fp1.write(i)
    fp1.close()
    print("-"*50,"Item Deleted Successfully","-"*50)

    
def update_price():
    fp=open("items.txt",'r')
    c=fp.readlines()
    for i in c:
        i=i.rstrip().split(',')
        print(i[0],'---->',i[1],'---->',i[2])
    item_no=input("enter item no. of which price needs to be updated: ")
    item_price=input("enter new price for the item: ")
    check=item_price.isdigit()
    if check==True:
        for i in range(len(c)):
            if item_no in c[i]:
                l=c[i].rstrip().split(',')
                c[i]=item_no+','+l[1]+','+item_price+'\n'
                print("-"*50,"Updated the Price of the Item Successfully","-"*50)
                break
        else:
            print("Item does not exists")
        fp1=open("items.txt",'w')
        fp1.writelines(c)
        fp1.close()
        fp.close()
    else:
        print("-"*50,"Non acceptable Price......Price should be numeric","-"*50)
            
        
def itemlist():
    print("-"*50,"Menu Card","-"*50)
    print(" "*100)
    fp=open('items.txt','r')
    c=fp.readlines()
    fp.close()
    print("item_no"," "*20,"item_name"," "*20,"item_price")
    for i in c:
        i=i.rstrip().split(',')
        print(i[0],"-"*25,">",i[1],'-'*20,'>',i[2])
    d={}
    total=0
    while True:
        ch=input("Choose your dish number: ")
        q=int(input("enter quantity of above dish you want to order: "))
        temp=0
        for i in c:
            i=i.rstrip().split(',')
            if ch==i[0]:
                temp=1
                if ch not in d.keys():
                    d[i[1]]=q
                else:
                    d[i[1]]+=q
                total=total+(q*int(i[2]))
        if temp==0:
            print("Invalid Dish Number")
        t=input("hit y to add more dishes: ")
        if t=='y':
            continue
        else:
            break
    ord=random.randint(100,200)+random.randint(400,500)
    order=','
    print("*"*50,"Your Order","*"*50)
    print(" "*100)
    print(f"Order number:{ord}")
    [print(key,":",value) for key,value in d.items()]
    print("\n")
    print("-"*40,f">>>>>>>>>>>>  Total Amount={total} in INR  <<<<<<<<<<<<","-"*40)
    for i in d:
        order=order+i+" "+str(d[i])+','
    order=str(ord)+order
    t1=input("enter y to confirm the order: ")
    if t1=='y':
        fp=open("orderlist.txt",'a')
        fp.write(order+'\n')
        fp.close()
        print("="*50,"Congratulations!Please Visit Again!","="*50)
    else:
        print("="*50,"Thank You!Relogin To Order Again!","="*50) 
    
        
