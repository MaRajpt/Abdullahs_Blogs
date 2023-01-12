############################  SECRET BIDDING AUCTION HOUSE #####################
import os

print("Welcome to the secret auction porgram")

bidder = {}
def auctioneer (bidder_name, user_bid):
    
    bidder[bidder_name] = int(user_bid)
    

    


bidding = True

while bidding == True:
    n = 0
    bidder_name = input("What is your name? ")
    user_bid = input("whats your bid? $")
    repeat = input("Is there another bidder? type 'yes' or 'no' ").lower()
    os.system('cls')
    
    auctioneer(bidder_name, user_bid)
    
    if repeat == "no":
        bidding = False
        
        print(f"{max(bidder, key=bidder.get)} has highest bid of : ${bidder[max(bidder, key=bidder.get)]}")
    

