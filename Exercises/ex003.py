# Your Student ID:230543019
# Your Name and Surname:IBRAHIM TAHA PINAR
import datetime
now = datetime.datetime.now()
currentDate = now.strftime("%m-%d-%y")
currentTime = now.strftime("%H:%M:%S")
currentDateandTime = now.strftime("%m-%d-%y %H:%M:%S")
print(f"Current Date : {currentDate}")
print(f"Current Time : {currentTime}")
print(f"Current Date and Time : {currentDateandTime}")
