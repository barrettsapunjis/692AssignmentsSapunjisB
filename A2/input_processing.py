# input_processing.py
# Barrett Sapunjis, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.status = { 
            "Light": {"val": "", "Options": {"Red", "Yellow", "Green"}},
            "Person": {"val": "", "Options": {"Yes", "No"}},
            "Vehicle": {"val": "", "Options": {"Yes", "No"}},
        }

        self.inputOptions = ["0", "1", "2", "3"]
        pass

    # Replace these comments with your function commenting
    def update_status(self, param): # You may decide how to implement the arguments for this function
        while(True): 
            userIn = input()
            if(self.checkInput(userIn)):
                pass

    def checkInput(self, input):
        if(input in self.status.values()): 
            return True 
        if(input in self.inputOptions):
            return True
        else: 
            return False 
        



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    pass



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sens = Sensor()
    print(sens.status["Person"]["Options"])
    while(True):
        userIn = input()
        if(sens.checkInput(userIn)): 
            match userIn: 
                case "0": 
                    break
                case "1": 
                    #option to change light color (Red, Green, Yellow)
                    x = 1 

                case "2": 
                    #option to change pedestrain status (Yes or No) 
                    x = 1

                case "3": 
                    #Option to change car status (Yes or No)
                    x = 1
        else:
            print("Input did not match possible options")


    





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

