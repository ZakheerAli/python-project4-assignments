# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def check(n , low , high):
    if n >= low and n <= high:
        return True
    else:
        return False
    
def main():
    n = 5
    low =4
    high = 9
    print(check(n , low , high))

if __name__=="__main__":
    main()