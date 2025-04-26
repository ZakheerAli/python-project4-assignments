import time
while True:
    timer= time.strftime("Date: %Y-%m-%d Time %H:%M:%S %p",time.localtime())
    print(f"{timer}",end="\r" ,flush=True)
    time.sleep(1)