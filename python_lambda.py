# lambda is small function which is return in one line 
# Syntax: lambda arguments: expression
 
string = " the function has no arguments"

string = lambda string: string.replace("no", "some")
print(string(" the function has no arguments"))
def  string_replace(string):
    return lambda : string.replace("no", "some")