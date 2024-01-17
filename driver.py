import users
import owner
print("="*70,"Welcome to NIMANTRAN","="*70)
print("="*45,"*"*15,"An Authentic Odia Cuisine Restaurant","*"*15,"="*47)
print("\n")
print("1.Customer\n2.Owner")
p=int(input("enter choice: "))
if p==1:
    users.login()
elif p==2:
    owner.login()
else:
    print("invalid input")
