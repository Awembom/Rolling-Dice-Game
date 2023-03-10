# A rolling Dice game

#code structure
    
    the programming language is python with a few functions used, 
    a function is used to collect player data (take user data) which
    is saved in a list, then another function (roll dice) is used to 
    role dice and the value is returned
    
    A dictionay is created in the third function (making dict) where
    the user data is inputed as the keys and 0 assigned as the value for 
    every user
    
    In the function named "operation", the dictionary is iterated through
    where every key is assigned the value returned when you call the function "roll dice"
    
    finally, there is a block that checks for the list value and the key with it is eliminated using a
    while loop till just one key is left which is outputed as the winner

# How it works
    firstly, it can take an unlimited number of players
    when you chose the number of players, each player has
    a chance to roll the dice twice

# Elimination
    for each roll game: each players results in his 2 rolls is sumed
    the player with the minimun sum is immediately eliminated and the 
    rest continue playing

# conditions
    in case two or more players get the same sum total which is also the minimum
    as compared to the other players, a mini game is immediately
    set up between those  players, now the person who gets the least 
    after the game is eliminated

# winning
    The winner is the last player who remains after everyone has been eliminated

# final message
You may review the code and propose changes and of course, dont forget to star
