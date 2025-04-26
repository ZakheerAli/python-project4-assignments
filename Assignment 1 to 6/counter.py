# import time

# user_time=int(input("Enter the time in seconds: "))

# for i in range(user_time,0,-1):
#     seconds= i % 60
#     minutes=int((i / 60) % 60)
#     hours= int(i / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("Time's up")



# import time
# try:
#     user_time=int(input("Enter the time in second : "))
# except ValueError:
#     print("invalid Input ! Please inter an integer")

# for i in range(user_time , 0 ,-1):
#     seconds=i % 60
#     minutes=int((i / 60) % 60)
#     hours=int(i / 3600)
#     print(f"\r{hours:02}:{minutes:02}:{seconds:02}",end="" ,flush=True)
#     time.sleep(1)
# print("Time's Up")


import time
try:
    user_time=int(input("Enter time in second: "))
    for i in range(user_time,0,-1):
        hours=int( i / 3600)
        mins=int(( i / 60 ) % 60)
        sec=i % 60
        print(f"\r{hours:02}:{mins:02}:{sec:02}",end="" , flush=True)
        time.sleep(1)
    print("time end")
except ValueError:
    print("Invalid Input")
 


