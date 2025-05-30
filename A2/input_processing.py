# input_processing.py
# Barrett Sapunjis, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.





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
            ("Green", "No", "No"): "Proceed",
            ("Yellow", "No", "No"): "Caution"
        }
        pass

    # Given the parameter to be changed (Light, Person, Vehicle)
    # the function will loop through promting the user with for an input with options and checking if the input is correct. 
    # If correct, the input will be stored as the value for the respective parameter and the loop will break. 
    def update_status(self, param): 
        while(True):
            options = self.status[param]["Options"]
            userIn = input(f"You have selected: \"{param}\".  What changes have been identified? ")
            if(self.checkInput(userIn, "status")):
                self.status[param]["val"] = userIn
                #print(self.status[param]["val"])
                return
            else:
                print("Incorrect entry, please try again") 
        
    # Checks the input against the possible options initialized within the class. 
    # Must be passed a name of the list/dict to be checked. 
    def checkInput(self, input, list):
        if (list == "status"):
            for keys in self.status: 
                if (input in self.status[keys]["Options"]):
                    return True
        elif(list == "inputOptions"):
            if(input in self.inputOptions):
                return True
        else: 
            return False 
    # Checks the current state of the sensor and compares it against the rules list. 
    # Outputs the corresponding action, or a "stay" if no match is found in the rules dict.     
    def evaluate(self):
        input_tuple = (self.status["Light"]["val"], self.status["Person"]["val"], self.status["Vehicle"]["val"])
        for condition in self.rules:
            if(input_tuple==condition):
                return self.rules[input_tuple]
        return "Stay"


# Encapsulation of the main program loop. 
# Takes in the sensor and prompts user to select a menu item.
# Checks if the menu input is valid and initializes the status update loop. 
def userInterface(sens: Sensor):
    while(True):
        print(f"Are changes detected in the vision input?")
        userIn = input("Please select 1 for light, 2 for Person, and 3 for Vehicle or enter 0 to end the program: ")
        if(sens.checkInput(userIn, "inputOptions")): 
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



        



# Prints the current state/status of the sensor from current class variables
# Prints the result of the evaluation (wether to go, stay, or have caution)
def print_message(action, sensor: Sensor):

    print(f"The parameter {action} was changed to {sensor.status[action]["val"]}")
    print(f"\n{sensor.evaluate()}")
    print(f"\nLight = {sensor.status["Light"]["val"]}, Person = {sensor.status["Person"]["val"]}, Vehicle = {sensor.status["Vehicle"]["val"]} ")

    



# Creates a Sensor and enters the user interface loop. 
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sens = Sensor()
    userInterface(sens)


    
    

    





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

