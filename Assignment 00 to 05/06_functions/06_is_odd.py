# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def check_odd_even():
    for i in range(20):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")
def main():
    check_odd_even()

if __name__=="__main__":
    main()
