# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    num-=7
    return num

def main():
    num:int=15
    num = subtract_seven(num)
    print(f"This should be zero:  {num}")

if __name__=="__main__":
    main()