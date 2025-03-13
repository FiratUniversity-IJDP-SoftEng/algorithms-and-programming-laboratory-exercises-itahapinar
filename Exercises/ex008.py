# Your Student ID:230543019
# Your Name and Surname:IBRAHIM TAHA PINAR
highofPyramid = int(input("Please enter the high of pyramid :"))
for i in range(1,(highofPyramid+1)):
    print(" " * (highofPyramid-i) + "*" * (2 * i - 1))
