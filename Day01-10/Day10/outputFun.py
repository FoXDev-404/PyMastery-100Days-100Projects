## Fucntion with Outputs

def foramt_name():
    f_name = str(input("Enter Your First Name: ")).title()
    l_name = str(input("Enter Your Last Name: ")).title()
    
    # print(f"{f_name} {l_name}")
    return f"{f_name} {l_name}"
    
print(foramt_name())
