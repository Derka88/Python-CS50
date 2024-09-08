while True : 
    try:
        x = int(input("what's X "))
    except ValueError:
        print("x is not an integer") #tu peux utiliser pass aussi pour ne pas renvoyer print
    else:
        break
print(f"x is {x}")