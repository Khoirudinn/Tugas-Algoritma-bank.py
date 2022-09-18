hai=input(" ").lower().replace(" ", "")
y =hai[0:5]
if(hai == "hello"):
    money = 0
elif(y == "hello"):
    money = 0
elif(hai[0] == "h"):
    money = 20
else:
    money = 100

print("$", money)
