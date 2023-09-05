print("Welcome To Landscaper")

player = input("What is your name?")
print(f"hello {player}")

game_data = {
    "money": 0,
    "tools": "teeth",
    "quit": False
}

while(True):
    print(f"""
          Currently Have ${game_data['money']} currently using {game_data['tools']}""")
    user_input = int(input("""
                    What would you like to do?
                           [1] Cut The Grass
                           [2] Tool Upgrade
                           [3] Reset
                           [4] Quit
                           """))
    # inserting user_input
    if(user_input == 1):
        if{game_data['tools'] == "teeth"}:
            print (f"You have made $1 cutting grass! You now have {game_data['money']}.")

            game_data['money'] += 1

        #elif = short for else if 
        #Inserting data using = game_data = "money, tools"
        elif {game_data['tools'] == "rusty scissors"}:
            print(f"You have made $5 for cutting grass using the rusty scissors! You now have ${game_data['money']}.")

            game_data['money'] += 5
        
        elif (game_data['tools'] == "push lawn Mower"):
            print(f"You have made $50 cutting grass witht the lawn mower! You now have ${game_data['money']}.")

            game_data['money'] += 50
        
        elif (game_data['tools'] == "electric mower"):
            print(f"You have made $100 cutting grass using the electric lawn mower! You now have ${game_data['money']}.")

            game_data['money'] += 100

        elif (game_data['tools'] == "team"):
            print(f"You have made $250 cutting grass using your team! You now have ${game_data['money']}.")

            game_data['money'] += 250
#inserting user_input
#upgrading your tools
    elif (user_input == 2):
        if(game_data['tools'] == "teeth" and game_data['money'] >= 5):
            print( "You have now upgraded to rusty scissors! Now making $5 cutting grass")

            game_data['money'] -= 5
            game_data['tools'] = "rusty scissors"
        
        elif(game_data['tools'] == "rusty scissors" and game_data['money'] >= 25): 
            print("You have now upgraded to the push lawnmower! Now making $50 cutting grass")

            game_data['money'] -= 25
            game_data['tools'] = "push lawnmover"
        
        elif(game_data['tools'] == "push" and game_data['money'] >= 250):
            print("You have now upgraded to a electric lawnmower! Now making $100 cutting grass")

            game_data['money'] -= 250
            game_data['tools'] = "electric lawnmower"
        
        elif(game_data['tools'] == "electric lawnmower" and game_data['money'] >= 500):
            print("You have now upgraded to starving student team! Now making $250 cutting grass")

            game_data['money'] -= 500
            game_data['tools'] = "team"
        
        else:
            print("Can not Upgrade at this time")
 #inserting user_input      
    elif(user_input == 3):
        print("You now have reset the game!")
        game_data['money'] = 0
        game_data['tools'] = 'teeth'
#inserting user_input
## quiting the game 
    elif(user_input == 4):
        game_data['quit'] = True
    
    elif(game_data['quit'] is True):
        print("You have quit the game!")
#Printing congratulations after reaching over $1000 and using team to cut grass
    if(game_data['money'] >= 1000  and game_data['tools'] == "team"):
        print("Congratulations You Win!!!")