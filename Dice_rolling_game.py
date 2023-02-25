import random

#to take number of players and player names
def take_user_data():
    player_data = []
    n = int(input("Enter the number of players participating: "))
    for i in range(1, n+1):
        Pname = input(f"Player{i}, Enter your name: ")
        player_data.append(Pname)

    return player_data

#to roll the dice 2 times 
def roll_dice():
    count = 0 
    n = 0
    while True:
        roll = input("Press r to toll dice: ")
        if roll == "r":
            n += random.randint(1,6)
        else:
            continue
        count += 1
        if count == 2:
            break
    return n

#to make a dictionary which will be used for operations
def making_dict(player_data):
    W_player_data = {}
    player_data
    for names in player_data:
        W_player_data[names] = 0

    return W_player_data

def operation(W_player_data):

    #using recursion with base condition len of dictiornary W_player_data ==1
    if len(W_player_data) == 1:
        for keys in W_player_data.keys():
            print(f"the Winner is: {keys}  ")
        return 1

    #calling the function to roll dice, then after assigning values, sorting into a list and using that list to check for
    #corresponding keys and eliminating the keys
    else:
        for names in W_player_data.keys():
            print(f"Current player is:  {names}")            
            W_player_data[names] = roll_dice()
        check = sorted(W_player_data.values())

                
        print(check)
        print(f"this is the results of this round: {W_player_data}")

        for keys in W_player_data.keys():
            if W_player_data[keys] == check[0]:
                print(f"Player with name {keys} has been eliminated with a score of {check[0]}")
                player_to_delete = keys
                break
        del(W_player_data[keys])
        print(W_player_data)
    return operation(W_player_data)

#calling the various functions
player_data = take_user_data()
W_player_data = making_dict(player_data)
operation(W_player_data)


