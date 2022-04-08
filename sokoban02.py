"""
    Author: Salvador Hernandez Mendoza
    Date: 30/03/2022
    Description: Sokoban game template

    0 - Character
    1 - Floor
    2 - Box
    3 - Wall
    4 - Target
    5 - Box_Target
    6 - Character_Target
"""


class Sokoban:
    """_summary_: Sokoban class"""

    map = []
    character_row = 0
    character_col = 0

    def __init__(self):
        """_summary_: Constructor"""
        pass

    def loadMap(self):
        """_summary_: Load the map from a file"""
        file = open("level1.s", "r")  # Open the file
        # TODO: read the file and load the map
        self.map = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 0, 1, 2, 1, 4, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]

    def printMap(self):
        """_summary_: Print the map"""
        # TODO: Print the map
        for row in self.map:  # For each row in map
            print(row)  # Print the row

    def findCharacterPosition(self):
        """_summary_: Find the character position"""
        for row in range(len(self.map)):  # Get rows number on the map
            for col in range(len(self.map[row])):  # Get columns number on the map
                if self.map[row][col] == 0:  # If the character is found
                    self.character_row = row  # Update the character row position
                    self.character_col = col  # Update the character col position

    def moveLeft(self):
        """_summary_: Move the character to the left rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col - 1] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][
                self.character_col
            ] = 1  # put floor character last position
            self.map[self.character_row][
                self.character_col - 1
            ] = 0  # move the character to next position
            self.character_col = self.character_col - 1  # update the character position
        # TODO: 1. character, target
        # TODO: 2. character, box, floor
        # TODO: 3. character, box, target
        # TODO: 4. character, box_target, floor
        # TODO: 5. character, box_target, target
        # TODO: 6. character_taget, floor
        # TODO: 7. character_taget, target
        # TODO: 8. character_taget, box, floor
        # TODO: 9. character_taget, box, target
        # TODO: 10. character_taget, box_target, floor
        # TODO: 11. character_taget, box_target, target

    def moveRight(self):
        """_summary_: Move the character to the right rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][
                self.character_col
            ] = 1  # put floor character last position
            self.map[self.character_row][
                self.character_col + 1
            ] = 0  # move the character to next position
            self.character_col = self.character_col + 1  # update the character position
        # TODO: 1. character, target
        # TODO: 2. character, box, floor
        # TODO: 3. character, box, target
        # TODO: 4. character, box_target, floor
        # TODO: 5. character, box_target, target
        # TODO: 6. character_taget, floor
        # TODO: 7. character_taget, target
        # TODO: 8. character_taget, box, floor
        # TODO: 9. character_taget, box, target
        # TODO: 10. character_taget, box_target, floor
        # TODO: 11. character_taget, box_target, target

    def moveUp(self):
        """_summary_: Move the character up rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row - 1][self.character_col] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][
                self.character_col
            ] = 1  # put floor character last position
            self.map[self.character_row - 1][
                self.character_col
            ] = 0  # move the character to next position
            self.character_row = self.character_row - 1  # update the character position
        # TODO: 1. character, target
        # TODO: 2. character, box, floor
        # TODO: 3. character, box, target
        # TODO: 4. character, box_target, floor
        # TODO: 5. character, box_target, target
        # TODO: 6. character_taget, floor
        # TODO: 7. character_taget, target
        # TODO: 8. character_taget, box, floor
        # TODO: 9. character_taget, box, target
        # TODO: 10. character_taget, box_target, floor
        # TODO: 11. character_taget, box_target, target

    def moveDown(self):
        """_summary_: Move the character down rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][
                self.character_col
            ] = 1  # put floor character last position
            self.map[self.character_row + 1][
                self.character_col
            ] = 0  # move the character to next position
            self.character_row = self.character_row + 1  # update the character position
        # TODO: 1. character, target
        # TODO: 2. character, box, floor
        # TODO: 3. character, box, target
        # TODO: 4. character, box_target, floor
        # TODO: 5. character, box_target, target
        # TODO: 6. character_taget, floor
        # TODO: 7. character_taget, target
        # TODO: 8. character_taget, box, floor
        # TODO: 9. character_taget, box, target
        # TODO: 10. character_taget, box_target, floor
        # TODO: 11. character_taget, box_target, target

    def checkLevelComplete(self):
        """_summary_: Check if level is complete

        Returns:
            complete(bool): Return if level is complete or not
        """
        # TODO: Check if the level is complete
        # If return True, the level is complete
        # If return False, the level is not complete
        complete = False
        return complete

    def play(self):
        """_summary_: Play the game"""
        self.loadMap()  # Call the map
        self.findCharacterPosition()  # Update the character position for new map
        instructions = "d-Right, a-Left, w-Up, s-Down"  # Instructions
        print(instructions)  # Print the instructions
        while True:  # Infinite loop
            complete = self.checkLevelComplete()  # Check if the level is complete
            if complete == True:  # If the level is complete
                print("Level Complete")  # Print the level complete
                input("Press Enter to continue...")  # Wait for the user to press enter
                self.loadMap()  # Call the map
                self.findCharacterPosition()  # Update the character position for new map
            self.printMap()  # Call the printMap method
            print(
                "Character position: [{},{}]".format(
                    self.character_row, self.character_col
                )
            )  # Print the character position
            move = input("Select move: ")  # Ask for the move
            if move == "a":  # If the move is left
                self.moveLeft()  # Call moveLeft rules
            elif move == "d":  # If the move is right
                self.moveRight()  # Call moveRight rules
            elif move == "w":  # If the move is up
                self.moveUp()  # Call moveUp rules
            elif move == "s":  # If the move is down
                self.moveDown()  # Call moveDown rules
            elif move == "q":  # If the move is quit
                break  # Game quit


game = Sokoban()  # Create a object from Sokoban class
game.play()  # Fun Fun Fun ;)
