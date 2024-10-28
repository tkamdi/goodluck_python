import datetime

def good_luck_message():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")

    print(f"\nToday's Date: {current_date}")
    print(f"Current Time: {current_time}\n")
    print("Wishing you the very best of luck!")
    print("May your day be filled with success, happiness, and prosperity.")
    print("You got this!")
    print("I got it!!!!!!!!!!!!!")


good_luck_message()
