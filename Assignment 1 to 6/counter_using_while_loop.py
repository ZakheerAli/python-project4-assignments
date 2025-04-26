import time

def count_down(t):
    while t:
        hours=int(t/3600)
        mins=int((t/60)%60)
        secs= t % 60
        timer=f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        t-=1
    print("Time'ups")
try:
    t=int(input("Enter time in second: "))
except ValueError:
    print("Invalid Input,Please enter an ineteger!")

count_down(t)
