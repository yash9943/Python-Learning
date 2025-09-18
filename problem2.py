india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter first city : ")
city2 = input("Enter second city : ")

if city1 in india and city2 in india:
    print(f"{city1} and {city2} both placed in same country which is india.")
elif city1 in pakistan and city2 in pakistan:
    print(f"{city1} and {city2} both placed in same country which is pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"{city1} and {city2} both placed in same country which is bangladesh.")
else:
    print(f"{city1} and {city2} both city not placed in same country.")