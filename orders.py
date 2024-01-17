def dispatch():
    fp=open("orderlist.txt",'r')
    c=fp.readlines()
    fp.close()
    print("-"*50,"Live Orders","-"*50)
    print(" "*100)
    print("Order no.","-"*20,">item_specifications")
    for i in c:
        i=i.rstrip().split(',')
        print(i)
    order_no=input("enter order no to be dispatched: ")
    l1=[]
    temp=0
    for i in c:
        l=i.rstrip().split(',')
        if order_no==l[0]:
            temp=1
            continue
        else:
            l1.append(i)
    if temp==1:
        fp1=open("orderlist.txt",'w')
        fp1.writelines(l1)
        fp1.close()
        print("="*50,"Order Dispatched!","="*50)
    else:
        print("No such order exists")
