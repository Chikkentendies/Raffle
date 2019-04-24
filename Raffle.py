from sys import argv
import random

script, input_file = argv

def print_all(f):
    print(f.read())

current_file = open(input_file)

print("This month's raffle entrants are: \n")

print_all(current_file)



print("\nPress enter to randomly select a winner! ")

input("")

raff_winner = random.choice(open(input_file).readlines())
print(f"Congrats! {raff_winner}")
