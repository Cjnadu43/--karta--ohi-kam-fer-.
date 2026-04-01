from auction_art_SMELLMYFART import logo
print(logo)
name = input("What is your name?: "). lower()
price = int(input("What is your bid you fliping monkey?: $"))
other_bids = input("Are there any other bids?:  Type \"yes\" or \"no\"").lower()

list_of_bids = {}


while other_bids == "yes":
    list_of_bids[name] = price


print(list_of_bids)









# Functionality
# Each person writes their name and bid.
# The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid, the program works out who has the highest bid and prints it.
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
