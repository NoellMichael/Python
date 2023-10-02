print('''             %%%%
                    %%%%-(
                  _%%%%%_/                        \ ' /
                _%%%%%%%%                        - (_) -
              _%%%%%%%/ \%                        / , \
             %%%%%%%%%\\ \_
               %%%%%%   \ \\
                   )    /\_/
                 /(___. \
                 '----' (
                /       )
    ---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___
              /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_
            ,'          (         ```--.._= -_= -_= _-=- -_= _=-
         ,-'            )                 ``--._=-_ =-=_-= _-= _
         '-._    '-..___(                       ``-._=_-=_- =_-=
             ``---....__)                            `-._-=_-_=-
                   )|)|                                  `-._=-_
                   '-'-.\_                                    `-.''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You're at the beach, where do you want to go? Left or right? ").lower()

if choice1 == 'left':
    print("You have now reached the sea.")
    choice2 = input("Do you want to wait for a boat or swim? ").lower()
    
    if choice2 == 'swim':
        print("Oops. You've been eaten by sharks!")
    elif choice2 == 'boat':
        print("You've now reached an island. You see a broken house, a cave, and the forest.\n")
        choice3 = input("Where do you want to go? ").lower()
        
        if choice3 == 'broken house':
            print("A monster pounces and uses its claws and fangs, tearing you apart!")
        elif choice3 == 'cave':
            print("You see three doors.")
            choice4 = input("Which door? Red, yellow, or blue? ").lower()
            
            if choice4 == 'red':
                print("You died in a fire!")
            elif choice4 == 'yellow':
                print("Congratulations! You've found the treasure!")
            elif choice4 == 'blue':
                print("You drowned in a pool of water!")
            else:
                print("Invalid choice. You are now lost.")
        else:
            print("Invalid choice. You are now lost.")
    else:
        print("Invalid choice. You are now lost.")
else:
    print("Shii! You stepped on a cast of crabs!")
