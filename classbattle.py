
def game():
    # Importing the random module so it may be used to randomize elements in the game
    import random

    # Defining a class which stores methods and attributes that classify they player's pokemon
    class PlayerPokemon:

        # Creating a constructor method for the player
        # Default attributes placed within constructor
        def __init__(self):
            # Self keyword used as a placeholder which will be replaced by the instantiated object's name
            # Player's pokemon has a name, a level, and a certain amount of HP
            self.name = ''
            self.player_level = 0
            self.player_HP = 0

        def choose_pokemon(self):

            """
            () -> str
            Allows player to choose a pokemon by choosing a number between 0 and 3
            """
            # A list which stores the available pokemon that the player can choose from
            pokemon = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle']
            print(" ")

            # Try except
            while True:
                # Tries this block of code and if a ValueError is encountered
                try:
                    print("(0) = Pikachu , (1) = Charmander , (2) = Bulbasaur , (3) = Squirtle")
                    choosing_pokemon = int(input("Enter a number between 0 and 3 to choose a pokemon : "))
                    break
                # Catches the error and prints the message
                except ValueError:
                    print("Invalid input")

            # While the number provided by the player is less than 0 or greater than 3 continue to ask until a valid
            # number is provided
            while choosing_pokemon < 0 or choosing_pokemon > 3:
                choosing_pokemon = int(input("Enter a number between 0 and 3 to choose a pokemon : "))

            # Indexes the specific pokemon from the list provided and returns the pokemon's name
            chosen_pokemon = pokemon[choosing_pokemon]
            return chosen_pokemon

        # Method that determines the player's level and HP
        def choose_level_hp(self):
            """
            () -> list
            A level is randomly chosen from 1 and 5 and a certain amount of HP is assigned depending on the random
            number generated
            """

            # Level is determined randomly between by assigning a number between 1 and 5
            level_chosen = random.randint(1, 5)
            # HP in this game will always be 20 more than the level
            hp_chosen = level_chosen * 20
            # level_chosen = 1
            # hp_chosen = 20
            # Returns the level and HP as a list so it can be indexed and assigned properly
            return [level_chosen, hp_chosen]

        # Assigning the player's level and HP
        def assign_level_hp(self):
            """
            () -> ()
            The level and HP that were returned in the method above, are now assigned according to index
            to the player_level and player_HP attributes defined in the constructor
            """
            # variable is being assigned to the values returned
            level_hp = self.choose_level_hp()
            # Variables created in the constructor method are being assigned according to the list that was returned
            self.player_level = level_hp[0]
            self.player_HP = level_hp[1]

        # Creating the pokemon itself
        def create_player_pokemon(self):
            """
            () -> ()
            The name attribute defined in the constructor
            is assigned to the value returned from the choose_pokemon
            method and the assign_level_hp method is called
            """
            self.name = self.choose_pokemon()
            self.assign_level_hp()
            print(" ")
            print("Your", self.name, "is level", self.player_level, "and has", self.player_HP, "Hp")
            print(" ")

        # Recreates the player pokemon if player loses
        def recreate_player_pokemon(self):
            """
            () -> ()
            The player_HP attribute is reassigned to the starting hp that the player started off with
            before losing the match
            """
            # If the player loses the level remains the same as it was prior to the match starting
            # HP is just the level multiplied by a factor of 20
            self.player_HP = self.player_level * 20
            print(" ")
            print("Your", self.name, "is level", self.player_level, "and has", self.player_HP, "Hp")
            print(" ")

        # Method is used to reveal pokemon's upgraded level and HP whenever player wins a match
        def show_player_pokemon_if_player_wins(self):
            """
            () -> ()
            Recreates an updated pokemon different from the previous method and displays the player pokemon's
            level and HP
            """
            print(" ")
            print("Your", self.name, "is level", self.player_level, "and has", self.player_HP, "Hp")
            print(" ")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    class OpponentPokemon:

        # Constructor method for the opponent pokemon
        def __init__(self):
            # The opponent has a name, HP, and a level
            self.opponent_pokemon_name = ' '
            self.opponent_level = 0
            self.opponent_HP = 0

        def assigning_random_opponent_pokemon(self):
            """
            () -> str
            A pokemon is randomly chosen from the list and the pokemon chosen is returned as is used when
            the pokemon is being created
            """
            list_of_pokemon = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle']

            # Random module function'choice' is used to randomly select a pokemon from the list
            opponent_chosen_pokemon = random.choice(list_of_pokemon)
            return opponent_chosen_pokemon

        def determine_opponent_pokemon_level(self):
            """
            () -> list
            The level of the opponent is randomly chosen from a number between 1 and 5. The HP is determined by
            multiplying the level by a factor of 20
            """
            # The integer chosen from 1-5 is assigned to the opponent_level attribute
            opponent_level = random.randint(1, 5)
            # The opponent HP attribute is assigned by multiplying the opponent_level attribute by 20
            opponent_hp = opponent_level * 20
            # Returns the attributes assigned above as a list so they may be indexed accordingly
            return [opponent_level, opponent_hp]

        def assigning_opponent_level_hp(self):
            """
            () -> ()
            The level and HP generated are assigned based on the index value provided in the list that was returned
            """
            # Calling the function that determined the hp and level of the opponent pokemon
            hp_level = self.determine_opponent_pokemon_level()
            # Assigning according to index value to the attributes provided in the constructor
            # The instance to be created is assigned by index
            self.opponent_level = hp_level[0]
            self.opponent_HP = hp_level[1]

        def create_opponent(self):
            """
            () ->()
            Function creates the opponent pokemon and prints out the name, level, and HP
            """
            # Calling the function that assigned the level and HP
            self.assigning_opponent_level_hp()
            # Calling the function that determined the name of the pokemon
            self.opponent_pokemon_name = self.assigning_random_opponent_pokemon()
            print(" ")
            print("Your opponent is", self.opponent_pokemon_name, "with level", self.opponent_level, "and has",
                  self.opponent_HP, "HP")

    # - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Instantiating the PlayerPokemon class by creating an object called player
    player = PlayerPokemon()
    # Calling the function that creates the player
    player.create_player_pokemon()

    # Instantiating the OpponentPokemon class by creating an object called opponent
    opponent = OpponentPokemon()
    # Calling the function that creates the opponent
    opponent.create_opponent()

    # - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    class GameMechanics:
        # Creating a constructor that has the player's input, opponent's input, number of wins, and number of losses
        def __init__(self):

            self.player_input = ''
            self.input_opponent = 0
            self.wins = 0
            self.losses = 0

        def let_player_input(self):
            """
            () -> str
            Allows player to enter a character that corresponds to a certain move in the game
            """
            valid = ['r', 'p', 's']
            print(" ")
            user_in = input("Enter (r) for rock, (p) for paper, (s) for scissors : ")
            # While the user doesn't choose an item found in the valid list of moves
            # keep asking
            while user_in not in valid:
                print("Enter a valid input")
                user_in = input("Enter (r) for rock, (p) for paper, (s) for scissors : ")
                # if user enters a valid answer break out of while loop and return that input
                if user_in in valid:
                    break
            return user_in

        def wins_counter(self):
            """
            () -> int
            Increments the win attribute by 1 each time when called
            """
            self.wins += 1

        def wins_return(self):
            """
            () -> int
            Returns the value stored in the win attribute
            """
            return self.wins

        def losses_counter(self):
            """
            () -> int
            Increments the losses attribute by 1 each time when called
            """
            self.losses += 1

        def losses_return(self):
            """
            () -> int
            Returns the value stored in the losses attribute
            """
            return self.losses

        def show_wins_losses(self):
            """
            () -> ()
            Function shows the user what their total wins and losses were
            """
            print("WINS :", self.wins_return())
            print("LOSSES :", self.losses_return())

        def opponent_input(self):
            """
            () -> int
            Function determines the opponent's move by randomly generating a number between 1 and 3 and returns it
            """
            opponent_move = random.randint(1, 3)
            return opponent_move

        def show_player_opponent_move(self):

            """
            () -> ()
            Function shows the player's and the opponent's move to the user
            """
            # Assigning the player_input and opponent_input attributes to the values returned from their
            # respective functions
            self.player_input = self.let_player_input()
            self.input_opponent = self.opponent_input()

            if self.player_input == 'r':
                print(" ")
                print("You chose", self.player_input + 'ock!')
            elif self.player_input == 'p':
                print(" ")
                print("You chose", self.player_input + 'aper!')
            elif self.player_input == 's':
                print(" ")
                print("You chose", self.player_input + 'cissors!')

            if self.input_opponent == 1:
                print("Your opponent chose rock!")
            elif self.input_opponent == 2:
                print("Your opponent chose paper!")
            elif self.input_opponent == 3:
                print("Your opponent chose scissors!")

        def retrieve_player_pokemon(self, objplayer):
            """
            (objplayer) -> str
            Returns the name attribute from the instance of the PlayerPokemon class
            >>> objplayer.name
            squirtle
            >>> objplayer.name
            pikachu
            """
            return objplayer.name

        def leveling(self, objplayer):
            """
            (objplayer) -> int
            Returns the level attribute from the instance of the PlayerPokemon class
            >>> objplayer.player_level
            5
            >>> objplayer.player_level
            6
            """
            objplayer.player_level += 1
            return objplayer.player_level

        def hp_increase(self, objplayer):
            """
            (objplayer) -> int
            Returns the HP attribute from the instance of the PlayerPokemon class
            >>> objplayer.player_HP
            20
            >>> objplayer.player_HP
            40
            """
            # Increases the HP by 20 if the player wins
            objplayer.player_HP = objplayer.player_level * 20
            return objplayer.player_HP

        def show_player_pokemon_win(self, objplayer):
            """
            (objplayer) -> method
            Returns the method that shows the stats of the pokemon if the player wins
            >>> Your pikachu is level 2 and has 40 HP
            >>> Your charmanader is level 3 and has 60 HP
            """

            return objplayer.show_player_pokemon_if_player_wins()

        # Methods are self explanatory
        def reset_opponent(self, objopponent):
            # Returns the new opponent pokemon by using the
            # instance of the OpponentPokemon class to call the create_opponent method
            return objopponent.create_opponent()

        def reset_player(self, objplayer):
            # Returns the same player pokemon with the same stats by using the
            # instance of the PlayerPokemon class to call the recreate_player_pokemon method
            return objplayer.recreate_player_pokemon()

        def show_opponent_hp(self, objopponent):
            # Returns the new opponent's HP by using the
            # instance of the OpponentPokemon class to call the opponent_HP attribute
            return objopponent.opponent_HP

        def show_player_hp(self, objplayer):
            # Returns the players's HP by using the
            # instance of the PlayerPokemon class to call the player_HP attribute
            return objplayer.player_HP

        def reduce_opponent_health(self, reduce):
            # takes the instance of the OpponentPokemon class and reduces
            # the attribute that determines opponent's HP by 5 whenever this is called
            reduce.opponent_HP -= 5
            return reduce.opponent_HP

        def reduce_player_health(self, reduce):
            # takes the instance of the PlayerPokemon class and reduces
            # the attribute that determines player's HP by 5 whenever this is called
            reduce.player_HP -= 5
            return reduce.player_HP

        def if_player_wins(self):
            """
            () -> ()
            Function asks for user input and determines if the user wants to play again
            """
            play_again = input("Enter (y) to play again or (n) to quit : ")
            valid = ['y', 'n']

            if play_again == 'y':
                # Because player won, calls the method that upgrades the player's pokemon
                self.show_player_pokemon_win(player)
                self.reset_opponent(opponent)
                self.the_game()
            elif play_again == 'n':
                # Shows total wins and losses
                self.show_wins_losses()
                quit()
            # While the input provided is not in the valid list
            # Keep asking
            while play_again not in valid:
                play_again = input("Please Enter (y) to play again or (n) to quit : ")
            if play_again == 'y':
                self.show_player_pokemon_win(player)
                self.reset_opponent(opponent)
                self.the_game()
            elif play_again == 'n':
                self.show_wins_losses()
                quit()

        def if_opponent_wins(self):
            """
            () -> ()
            Function asks for user input and determines if the user wants to play again
            """
            valid = ['y', 'n']
            play_again = input("Enter (y) to play again or (n) to quit : ")
            # Player did not win so no upgrade to the  stats
            # Resets the player pokemon to how it was when the game started
            if play_again == 'y':
                self.reset_player(player)
                self.reset_opponent(opponent)
                self.the_game()
            elif play_again == 'n':
                self.show_wins_losses()
                quit()
            # While the input provided is not in the valid list
            # Keep asking
            while play_again not in valid:
                play_again = input("Please Enter (y) to play again or (n) to quit : ")
                if play_again == 'y':
                    self.reset_player(player)
                    self.reset_opponent(opponent)
                    self.the_game()
                elif play_again == 'n':
                    self.show_wins_losses()
                    quit()

        def the_game(self):
            """
            () -> ()
            Official game method that checks for user input and opponent's input to determine rock paper scissor
            combinations
            """
            self.show_player_opponent_move()
            # Tie game instances
            if (self.player_input == 'r' and self.input_opponent == 1) or (self.player_input == 'p' and self.input_opponent == 2) \
                    or (self.player_input == 's' and self.input_opponent == 3):
                print("Your attacks negated each other!")
                print(" ")
                print('Player HP:', self.show_player_hp(player))
                print('Opponent HP:', self.show_opponent_hp(opponent))

            # Winning instances for player
            elif (self.player_input == 'r' and self.input_opponent == 3) or (self.player_input == 'p' and self.input_opponent == 1) \
                    or (self.player_input == 's' and self.input_opponent == 2):
                print("Your attack dealt 5 damage to your opponent!")
                print(" ")
                print('Player HP:', self.show_player_hp(player))
                print('Opponent HP:', self.reduce_opponent_health(opponent))

            # Losing instances for the opponent
            elif (self.player_input == 'r' and self.input_opponent == 2) or (self.player_input == 'p' and self.input_opponent == 3) \
                    or (self.player_input == 's' and self.input_opponent == 1):
                print("Oh no! Your opponent dealt 5 damage to you!")
                print(" ")
                print('Player HP:', self.reduce_player_health(player))
                print('Opponent HP:', self.show_opponent_hp(opponent))

            # If opponent's HP becomes 0, player wins and calls respective methods because player won
            if self.show_opponent_hp(opponent) == 0:
                print("Congratulations! You win!")
                self.wins_counter()
                print(" ")
                print("Your", self.retrieve_player_pokemon(player), "grew to level", self.leveling(player),
                      "and now has", self.hp_increase(player), "HP!")
                print(" ")
                self.if_player_wins()
            # If players's HP becomes 0, opponent wins and calls respective methods because opponent won
            elif self.show_player_hp(player) == 0:
                print("Oh no! You lost!")
                self.losses_counter()
                print(" ")
                self.if_opponent_wins()
            # Game loop
            # while neither the player nor opponent has 0 HP, keep running this function
            while self.show_opponent_hp(opponent) != 0 or self.show_player_hp(player) != 0:
                self.the_game()

    # - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Instantiating the game1 object which is an instance of the GameMechanics class
    game1 = GameMechanics()
    game1.the_game()


game()
