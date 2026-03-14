Number = int(input("Give me a number: "))

for i in range (0, Number):
  print(i)
if Number > 0:
  print("Positive number entered")
elif Number < 0:
  print("Negative number entered")
else:
  print("Zero entered")
