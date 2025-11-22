# shoppinglist=[]
# while True:
#     print("Please add an item to your list. If you are done, please enter Q:")
#     item=input()
#     if item=="Q":
#         print("Here is your final shopping list:")
#         print(shoppinglist)
#         break
#     shoppinglist.append(item)
#     print(shoppinglist)

# Please choose the operation
# 1. Insert
# 2. Delete 
# 3. View
# 4. Exit

shoppinglist=[]
while True:
    print("Please choose the operation \n\t1.Insert\n\t2.Delete\n\t3.View\n\t4.Exit")
    choice = input()
    if choice == "1":
        if count>5:
            print("Can't add more items, delete and insert again")
            continue
        print("Enter item name: ")
        item=input()
        shoppinglist.append(item)
    if choice == "2":
        print("Enter item that you would like to remove:")
        item=input()
        if item in shoppinglist:
            shoppinglist.remove(item)
            print(item+" has been successfully deleted")  
        else:
            print("item is not found")      
    if choice == "3":
        print(shoppinglist)
    if choice == "4":
        print("goodbye")
        break