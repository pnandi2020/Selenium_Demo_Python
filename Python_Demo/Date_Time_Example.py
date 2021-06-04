from datetime import datetime

presentime = datetime.now()

print(" NOW THE TIME IS:", presentime)

print("Todays Date is:", presentime.strftime('%Y-%m-%d') )
print("Year is:", presentime.year)
print("MOnth is:", presentime.month)
print("Day is:", presentime.day)
