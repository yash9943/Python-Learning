india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter city : ")
if city in india:
    print(f"{city} is placed in india.")
elif city in pakistan:
    print(f"{city} is placed in pakistan.")
elif city in bangladesh:
    print(f"{city} is placed in bangladesh.")
else:
    print(f"Your Enterd city {city} is not placed in acia.")