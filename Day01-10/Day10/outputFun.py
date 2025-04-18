## Fucntion with Outputs

def foramt_name():
    f_name = str(input("Enter Your First Name: ")).title()
    l_name = str(input("Enter Your Last Name: ")).title()
    
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    # print(f"{f_name} {l_name}")
    return f"Result: {f_name} {l_name}"
    
print(foramt_name())
