from datetime import date, timedelta

day,month,year=map(int,(input().split()))
current_date = date(year, month, day)
new_date = current_date + timedelta(days=7)
    
print(f"Day: {new_date.day}  Month: {new_date.month} Year: {new_date.year}")

