# function for comparing two strings
def compare(str1,str2):
    op1=""
    op2=""
    for i in str1:
        if i not in str2 :
            op1=op1+i
    for j in str2:
        if j not in str1:
            op2=op2+j
    print("Output1:", op1)
    print("Output2:", op2)

def main():
    str1 = input("Enter the string1:")
    str2 = input("Enter the string2:")
    compare(str1, str2)

if __name__ == "__main__":
    main()