#For mapping list of Numbers from 1 to 26 to Alphabets A , B , C ,D .. respectively #

num=[i for i in range(1,27)]
alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

dict1={alphabet[i]:num[i] for i in range(0,len(alphabet))}

#accepting data from user only of the type string #
s = input("Enter text: ")
if any(char.isdigit() for char in s):
    print("Please do not include digits in your text.")
else:    
    key=int(input("enter key to be shifted"))
    t1=s.upper()
    x=list(t1)
    w=0
    for i in range(0,len(x)):
        w=dict1.get(x[i]) #for converting the alphabets into rheir corresponding numbers#
        w=w+key # New key after shifting# 
        g=w % 26 # If key is greater than 26 then this converts to corresponding value which lies within 1-26 #
        print("position of letter",i+1," after shifting is",g)
        print(alphabet[g-1])
    

        


    
