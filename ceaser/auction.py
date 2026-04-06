from auction_art_SMELLMYFART import logo
print(logo)

def get_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_amount = bids[bid]
        if bid_amount > highest_bid:
            highest_bid = bids[bid]
            winner = bid

    print(f"the highest bis is {highest_bid} by {winner}")

list_of_bids = {}
is_game_on = True
while is_game_on:
    name = input("what is ur name?: ").lower()
    price = int(input("what is ur bid: $"))
    other_bids = input("are there any other bids?: type \"yes\" or \"no").lower()

    list_of_bids[name] = price

    if other_bids == "no":
        is_game_on = False
        get_highest_bid(list_of_bids)
    elif other_bids == "yes":
        print("\n" * 67)
    else:
        print("please enter either yes or no!")
