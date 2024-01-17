import items
import orders
def login():
    pwd=input("enter password: ")
    if pwd=="Owner@123":
        print("**************Logged in Successfully**************")
        print("="*50,"Welcome","="*50)
        while True:
            print("-----What do you want to do?-----")
            print("1.Update Itemslist\n2.Dispatch Order\n3.View The Item List\n4.Close\n")
            
            q=int(input())
            if q==1:
                print("----what do you want to update?----")
                print("1.Add items\n2.Delete items\n3.Update price of the item\n")
                q1=int(input())
                if q1==1:
                    items.add()
                elif q1==2:
                    items.delete()
                elif q1==3:
                    items.update_price()
                else:
                    pass
            elif q==2:
                orders.dispatch()
                
            elif q==3:
                fp=open('items.txt','r')
                c=fp.readlines()
                for i in c:
                    i=i.rstrip().split(',')
                    print(i)
                fp.close()
            else:
                print("="*40,"THANK YOU","="*40)
                break
    else:
        print("Invalid Password")
            
        
