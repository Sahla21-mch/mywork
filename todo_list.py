#to-do list in python
user_input = "random"
# using a dictionary ad storage
store = {}
print(type (store))
def work():
    print("your options are:")
    print("i. methods")
    print("ii. add")
    print("iii. delete")
    print("iv. view")
    print("v exit")

to_do = print("what are you working on? ")
work()
#using 4 methods add, delete, view, and update, exit, mark as done 
user_input = input("enter your request: ")
if user_input == "add":
    key = input("what number do you want (key) ?")
    item = input("what do you want to add here (value) ?")
    store.update({ key: item})
    print("first item added!", item)
elif user_input == "delete":
    key = input("what do you want to delete  (key) ?")
    item = input("what do you want to delete (value) ?")
    if key and item in store:
        store.pop("item", "key")
        print("deleted item:", item)
    else:
        print("oops item doesn't exist in your list!")
elif user_input == "view":
    print("list of things to-do")
    for key in store:
        print(store)
elif user_input == "exit":
    print("Till next time !!")


