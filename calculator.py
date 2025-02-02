#Calculator which can only perform addition 
total = int(input("How many numbers do you want to add? "))
sum = 0
num = 0
for i in range (1,total+1):
    num = float(input(f"Enter number {i} "))
    sum = sum + num
#Rounded result of the numbers
sum = round(sum)
print (f"The approximate sum of the given numbers is {sum:,}")
