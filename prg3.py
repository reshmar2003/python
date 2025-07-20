print(1 and 0)
print(not 1)

minMark=30
studentmarks=float(input("Enter the mark : "))
if studentmarks >= minMark:
    print("you are eligible")
elif studentmarks >=25:
    print("You have been put into waiting list ")
else:
    print("you are not eligible")