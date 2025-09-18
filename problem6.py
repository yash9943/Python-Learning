for i in range(5):
    print(f"you are run {i+1} miles")
    tried = input("Are you tried ? : ")
    if tried == 'yes or Yes':
        break

if i == 4 :
    print("Hurry up ! Your near complate race.")
else:
    print("You are tried ! But well played.")