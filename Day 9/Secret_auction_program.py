from art import logo
import os
print(logo)



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)




def get_bid():
    user = input('What is your name?: ').title()
    amount = int(input('What\'s your bid?: $'))

    bid_dict[user] = amount
        
    print(bid_dict)

bid_end = False

bid_dict = {}


while not bid_end:
    get_bid()
    
    end_bid = input('Are there other bidders? Type "Y" for "YES" and any other key for "No" >>>').lower()
    
    if end_bid != 'y':
        bid_end = True
        
        max_bid = 0
        max_bidder = ''
        for bidder in bid_dict:
            if bid_dict[bidder] > max_bid:
                max_bid = bid_dict[bidder]
                max_bidder = bidder
        max_bid = "{:,}".format(max_bid)
        
        print(f'\n\nThank you all for participating in this Auction, you all are winners, {max_bidder} won the auction with a bid of ${max_bid}.00 \n\n\n')
    else:
        clearConsole()
        
        
        