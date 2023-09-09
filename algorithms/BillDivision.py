# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# For example, assume the bill has the following prices:bill = [2,4,6] . Anna declines to eat item k = bill[2]  which costs 6. If Brian calculates the bill correctly, Anna will pay(2+4)/6 = 3 . If he includes the cost of bill[2], he will calculate (2+4+6)/2=6. In the second case, he should refund 3 to Anna.

def bonAppetit(bill, k, b):
    anna_share = (sum(bill) - bill[k]) // 2
    if anna_share == b:
        print("Bon Appetit")
    else:
        print(b - anna_share)

# Take user input for the bill items
bill = list(map(int, input("Enter the cost of each item in the bill, separated by spaces: ").split()))

# Take user input for the index of the item Anna didn't eat
k = int(input("Enter the index (0-based) of the item Anna did not eat: "))

# Take user input for the amount Anna has been charged
b = int(input("Enter the amount Anna has been charged: "))

# Call the function to determine if the bill is correct
bonAppetit(bill, k, b)
