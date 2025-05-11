def fun1(): # outer function
    msg = "Geeks for geeks"
    
    def fun2(): # inner function
        print(msg)  # accessing outer function's variable
    
    fun2()
fun1()

# nonlocal allows inner function to modify variables of outer function

def fun1(): # outer function
    a = 45
    
    def fun2(): # inner function
        nonlocal a  # allows modification of `a` from fun1
        a=54
        print(a)
    
    fun2()
    print(a)

fun1()

# solid example
def process_data(data):
    # removes extra spaces from a list
    
    def clean_data():
        return [item.strip() for item in data]  # Strip spaces
    
    return clean_data()  # return cleaned list

print(process_data(["  Python  ", "  Inner Function  "]))