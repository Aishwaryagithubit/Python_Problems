principle = float(input("enter the principle"))
year = float(input("enter the year"))
month = float(input("enter the month"))
time = year + month/12
rate = float(input("enter the rate in percent"))
Interest = principle *time* rate /100
print(f"Interest is {Interest}")
