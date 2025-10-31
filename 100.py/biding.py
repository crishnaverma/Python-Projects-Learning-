bider_dic={}

bider_avail=True

while bider_avail is True:
    name =input("Enter Your Name: \n")
    bid_price = int(input("Enter Your Bid Price: \n"))
    bider_dic[name]=bid_price
    anyoneelse= input("Is there any other bider: \n")
    print("\n"*100)
    if anyoneelse == "no":
        bider_avail=False

higest = 0
winner = ""

for bidder in bider_dic:
    price = bider_dic[bidder]
    if price > higest:
        higest = price
        winner = bidder

print(f"Highest Bid Was Done by: {winner} and the amount was: {higest}")