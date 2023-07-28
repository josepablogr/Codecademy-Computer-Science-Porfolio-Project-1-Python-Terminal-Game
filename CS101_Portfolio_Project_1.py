from art import *

#GAME TITLE
tprint("World Cup Trivia")

#GREETING MESSAGE
print("Welcome to the most exciting FIFA World Cup Trivia Game! There will be multiple-choice questions about the biggest sports event. The first player to answer 6 questions correctly wins the game. If there's a tie, a sudden death round takes off. Please enter the players' names.")

#INPUT PLAYERS NAMES
p1_name = input("P1 Name: ")
p2_name = input("P2 Name: ")

#DICTIONARY WITH TRIVIA QUESTIONS AND ANSWERS

dic_qa = {
    "Where was the very first World Cup held?\n a) Italy\n b) Uruguay\n c)Brazil\n d)West Germany":"b"
}