#oops code, using constructor, to build bank debit,credit,display info functions
class bank:
  def __init__(self,name,accounts_no,pin,Balance):
    self.name=name
    self.accounts_no=accounts_no
    self.pin=pin
    self.Balance=Balance

  def info(self):
    print(f"Name:{self.name}")
    print(f"Accounts_no:{self.accounts_no}")
    print(f"Balance:{self.Balance}")

  def credit(self,amount):
    attempts=0
    while attempts<3:
      ac_no=int(input("Enter your accounts_no:"))
      pin=int(input("Enter your pin:"))
      if ac_no!=self.accounts_no:
        print("❌invalid account no")
        attempts+=1
        print(f"your attempts remaining{3-attempts}")
      elif pin!=self.pin:
        print("❌invalid pin")
        attempts+=1
        print(f"your attempts remaining{3-attempts}")
      else:
        ac_no==self.accounts_no and pin==self.pin
        self.Balance += amount
        print(f"₹{amount} credited successfully.")
        print(f"Available Balance: ₹{self.Balance}")

    print("your account is blocked")

  def debit(self,amount):
     attempts=0
     while attempts<3:
      ac_no=int(input("Enter your accounts_no:"))
      pin=int(input("Enter your pin:"))
      if ac_no!=self.accounts_no:
        print("❌invalid account no")
        attempts+=1
        print(f"your attempts remaining{3-attempts}")
      elif pin!=self.pin:
        print("❌invalid pin")
        attempts+=1
        print(f"your attempts remaining{3-attempts}")
      else:
        ac_no==self.accounts_no and pin==self.pin
        self.Balance -= amount
        print(f"₹{amount} debiited successfully.")
        print(f"Available Balance: ₹{self.Balance}")

     print("your account is blocked")

a=bank("tejas",123456,1111,1000)
