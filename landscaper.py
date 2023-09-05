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
          Currently Have ${game_data['money']} currently using ${game_data['tools']}""")
    user_input = int(input("""
                    What would you like to do?
                           [1] Cut The Grass
                           [2] Tool Upgrade
                           [3] Reset
                           [4] Quit
                           """))
    if(user_input == 1):
        if{game_data['tools'] == "teeth"}:
            print (f"You have made $1 cutting grass! You now have {game_data['money']}.")

            game_data['money'] += 1

        #elif = short for else if 
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

    elif (user_input == 2):
        if(game_data['tools'] == "teeth" and game_data['money'] >= 5):
            print( "You have upgraded to rusty scissors")
        
        