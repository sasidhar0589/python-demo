# to handel known and unknown exceptions
def stack_operations():
    stack = []
    stack.append(10)
    stack.append(20)
    stack.append(30)
    for i in range(5):
            try:
                popped = stack.pop()
                print("Popped element is:", popped)
            except Exception as e:
                print("IndexError exception is caught",e)
    print("stack is empty")
stack_operations()

def key_error_handeler():
    dictionary = {"name": "surya", "age": 25}
    try:
        print(dictionary["name"])
        print(dictionary["phone"])
    except Exception as e:
        print("KeyError exception is caught",e)
    finally:
        print("Finally block executed")
        dictionary["phone"]= ""
        print(dictionary)
    print(dictionary['age'])
key_error_handeler()

def empty_list_handeler():
    temp_list = []
    temp_list.append(10)
    temp_list.append(20)
    temp_list.append(0)
    for i in range(5):
        print(temp_list[i])
        if temp_list[i] == 0:
            raise ValueError("zero identified in the list")
        else:
            continue
    print("List is empty")
empty_list_handeler()

