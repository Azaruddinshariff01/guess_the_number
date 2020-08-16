n=54
number_of_guesses=1
print("number of guesses only 9 times:")
while(number_of_guesses<=9):
    c=int(input("guess the number which i stored:\n"))
    if c<n:
        print("increase the number\n")
    elif c>n:
        print("decrease the number\n")
    else:
        print("you won the game")
        break
    print("no of guesses left more",9-number_of_guesses)
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>9):
    print("game over")