actual_cost = float(input("Please enter the Actual Product Price: "))
sales_amount = float(input("Please enter the Sales Amount: "))

if (sales_amount > actual_cost):
    amount = sales_amount - actual_cost
    print("Total Profit {0}".format(amount))
else:
        print("No profit!!!")