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
            "Light": {"val": "Green", "Options": {"Red", "Yellow", "Green"}},
            "Person": {"val": "Yes", "Options": {"Yes", "No"}},
            "Vehicle": {"val": "Yes", "Options": {"Yes", "No"}},
        }

        self.inputOptions = ["0", "1", "2", "3"]

        self.rules = { 
            ("Green", "No", "No"): "Go",
            ("Yellow", "No", "No"): "Caution"
        }
        pass

    # Replace these comments with your function commenting
    def update_status(self, param): # You may decide how to implement the arguments for this function
        while(True):
            options = self.status[param]["Options"]
            print(f"You have selected: {param}  please enter one of the follow options: {options}")
            userIn = input()
            if(self.checkInput(userIn)):
                self.status[param]["val"] = userIn
                print(self.status[param]["val"])
                return
            else:
                print("Incorrect entry, please try again") 
        

    def checkInput(self, input):
        for keys in self.status: 
            if (input in self.status[keys]["Options"]):
                return True
        if(input in self.inputOptions):
            return True
        else: 
            return False 
        
    def evaluate(self):
        input_tuple = (self.status["Light"]["val"], self.status["Person"]["val"], self.status["Vehicle"]["val"])
        for condition in self.rules:
            if(input_tuple==condition):
                return self.rules[input_tuple]
        return "Stay"


        
def userInterface(sens: Sensor):
    while(True):
        print(f"Please select an option from {sens.inputOptions}")
        userIn = input()
        if(sens.checkInput(userIn)): 
            match userIn: 
                case "0": 
                    break
                case "1": 
                    #option to change light color (Red, Green, Yellow)
                    sens.update_status("Light")
                    print_message("Light", sens)
                case "2": 
                    #option to change pedestrain status (Yes or No) 
                    sens.update_status("Person")
                    print_message("Person", sens)

                case "3": 
                    #Option to change car status (Yes or No)
                    sens.update_status("Vehicle")
                    print_message("Vehicle", sens)
        else:
            print("Input did not match possible options")
        print(f"\n")



        



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(action, sensor: Sensor):
    print(f"The paramter {action} was changed to {sensor.status[action]["val"]}")
    print(f"Light = {sensor.status["Light"]["val"]}, Person = {sensor.status["Person"]["val"]}, Vehicle = {sensor.status["Vehicle"]["val"]} ")
    print(sensor.evaluate())
    



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sens = Sensor()
    userInterface(sens)

    
    

    





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

