print ("Welcome to the tip calculator!")

bill=int(input("What was the total bill? ₹"))

tip=int(input("How much tip would you like to give? 10, 12, or 15? "))

if tip == 10:
	tip = bill * 0.10
	bill += tip

elif tip == 12:
	tip = bill * 0.12
	bill += tip

elif tip == 15:
	tip = bill * 0.15
	bill += tip

else:
	print("Invalid % of tip")

people=int(input("How many people to split the bill? "))

split_bill=bill/people

split_bill=round(split_bill,2)
print (f"Each person should pay: ₹{split_bill}")
