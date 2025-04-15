# Write a program that doubles each element in a list for example if you start with this [1,2,3,4,5] and ends with [2,4,6,8,10]
def main():
    new_list=[]
    def double_elem(number_list):
        for elem in number_list:
            new_list.append(elem*2)
        return new_list

    print(double_elem([1,2,3,4,5,6]))   
if __name__=="__main__":
    main()
