import sys
import random

computer_choices = ("Paper", "Rock", "Scissors")

def main():
    ''' Main method '''
    user_choice = ""
    while (user_choice != "p" and user_choice != "r" and user_choice != "s"):
        user_choice = input("Please insert the first letter of your choose: 'p', 'r' or 's' (paper, rock or scissors): ")

    computer_choice = computer_choices[random.randint(0,2)]
    evaluate(user_choice, computer_choice)

def evaluate(user_choice, computer_choice):
    computer_choice = random.choice(["p", "r", "s"])
    
    if user_choice == "p":
        if computer_choice == "r":
            show_user_victory(computer_choice)
        elif computer_choice == "s":
            show_computer_victory(computer_choice)
        else:
            show_draw(computer_choice)

    elif user_choice == "r":
        if computer_choice == "s":
            show_user_victory(computer_choice)
        elif computer_choice == "p":
            show_computer_victory(computer_choice)
        else:
            show_draw(computer_choice)
    else:
        if computer_choice == "p":
            show_user_victory(computer_choice)
        elif computer_choice == "r":
            show_computer_victory(computer_choice)
        else:
            show_draw(computer_choice)

def show_computer_victory(computer_choice):
    return show_result("Computer selected '" + get_complete_text_computer_choice(computer_choice) + "'. Computer wins")

def show_user_victory(computer_choice):
    return show_result("Computer selected '" + get_complete_text_computer_choice(computer_choice) + "'. User wins")

def show_draw(computer_choice):
    return show_result("Computer selected '" + get_complete_text_computer_choice(computer_choice) + "'. Draw")

def show_result(text):
    print(text)

def get_complete_text_computer_choice(computer_choice):
    if computer_choice == "p":
      return "Paper"
    elif computer_choice == "r":
      return "Rock"
    elif computer_choice == "s":
      return "Scissors"

if __name__ == '__main__':
    ''' Calling the main method '''
    main()
