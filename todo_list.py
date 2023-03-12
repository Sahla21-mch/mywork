#to-do list in python
user_input = "random"
# using a dictionary ad storage
store = {}
print(type (store))
def request():
    print("your options are:")
    print("i. add")
    print("ii. delete")
    print("iii view")
    print("iv exit")
while user_input != "exit":
    request()
    user_input = input("choose your request: ")
    #using 4 methods add, delete, view, and update, exit, mark as done 
    if user_input == "add":
        key = input("what number do you want (key) ?")
        item = input("what do you want to add here (value) ?")
        store.update({ key: item})
        print("first item added!", item)
    elif user_input == "delete":
        key = input("what do you want to delete  (key) ?")
        item = input("what do you want to delete (value) ?")
        if key and item in store:
            store.pop(key, item)
            print("deleted item:", item)
        else:
            print("oops item doesn't exist in your list!")
    elif user_input == "view":
        print("list of things to-do")
        print(store)
    elif user_input == "exit":
        print("Till next time !!")
