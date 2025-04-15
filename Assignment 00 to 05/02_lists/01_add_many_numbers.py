# Write a function that takes a list print the sum of all element in a list

def main():
    def sum_of_list(number):
        sum=0
        for i in number:
            sum+=i
        print(sum)
    sum_of_list([1,2,3,4,5,6])
if __name__=="__main__":
    main()    

