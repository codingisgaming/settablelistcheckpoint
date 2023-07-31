shopping_list = []
while True :
    print("input your order : (remove/add/view)")
    ch=input()
    if (ch=="remove") :
        x=input("what do u want to remove : " )
        shopping_list.remove(x)
    elif(ch=="add"):
        x=input("what do u want to add : ")
        shopping_list.append(x)
    elif(ch=="view"):
        print(shopping_list)
    else:
        print("thank you")
        break
