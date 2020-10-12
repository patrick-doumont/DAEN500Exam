#Patrick Doumont
#08 OCT 2020
#DAEN 500 Final Exam, Problem #2

class String_Manipulation:
    """Prompts the user for a string and returns the string in upper case."""
    def __init__(self, user_input=''):
        self.user_input = user_input
            
    def getString(self):
        self.user_input = input("Enter a string to be returned in upper case: ")
        
    def printString(self):
        print(self.user_input.upper())
        
new_input = String_Manipulation()
new_input.getString()
new_input.printString()

new_input2 = String_Manipulation()
new_input2.getString()
new_input2.printString()

new_input3 = String_Manipulation()
new_input3.getString()
new_input3.printString()