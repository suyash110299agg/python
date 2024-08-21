#BUG_LIST
#BUG01: How can expense subtracted be greater than income added?//same as BUG04
#BUG02: The code doesn't care if the uer dint give the date input--- FIXED
#BUG03: How to view the total income or total expense with the respective dates?--- FIXED
#BUG04: The current code gave the error statement- "You can't debit more than the available amount" followed by debit of the unavailable amount... let's call it v1.0... make any further changes in v2.0
#BUG05: Print the final array / list in the output OR give the user the option to view it --- FIXED
#BUG06: Now this version v2.0 is accepting any stuff as the date which shopuldn't be the case.. This bug will be worked out in v3.0 --- FIXED



from datetime import datetime


data=[]
balance=0
def display_menu():
    print("1. add income")
    print("2. add expense")
    print("3. my net income")
    print("4. save and exit")

def add_income():
    amount=int(input("Enter the amount"))
    date=input("Enter the date YYYY-MM-DD")
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validates the date format
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    data.append({"amount": amount, "date":date, "type":"income"})
    print("Income Added\n")

def add_expense():
    amount=int(input("Enter the amount\n"))
    date=input("Enter the date YYYY-MM-DD")
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validates the date format
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    balance= sum((entry['amount'] for entry in data if entry['type']=='income')) - sum((entry['amount'] for entry in data if entry['type']=='expense'))
    if balance < amount:
        print("You can't debit more than the available amount\n")
        return
    else:
        data.append({"amount": amount, "date":date, "type":"expense"})
 

def net_income():
    #balance= sum(entry['amount'] for entry in data if entry['type']=='income')
    total_income= sum(entry['amount'] for entry in data if entry['type']=='income')
    total_expense= sum(entry['amount'] for entry in data if entry['type']=='expense')
    balance=total_income-total_expense
    return balance


def main():
    display_menu()
    for choice in range(1,5):
        
        choice=int(input("choose outta the given options\n"))
        if choice==1:
            add_income()
        elif choice==2:
            add_expense()
        elif choice==3:
            net_income()
            break
        else:
            print("Invalid choice. Please try again\n")

if __name__=="__main__":
    main()
    print("Your current available balance is:\n",net_income())
    print(data)
