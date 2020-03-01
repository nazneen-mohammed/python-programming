# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, read data from file  then
#              added to list.then write data from list of dictionary in
#              to "ToDoToDofile.txt".
# RRoot,1.1.2030,Created started script
# NazneenM,2.20.2020 Added code to complete assignment 5
# NazneenM,2.28.2020, modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r") # read data from text file
        for line in file: # for each line in the file
            task, priority = line.split(",") # look for ',' end of task then assign it
            # to task the other word  to priority.
            dicRow = {"Task": task. strip(), "Priority": priority.strip()} # put it in dictionary
            list_of_rows.append(dicRow) # make list of dictionary
        file.close() # close the file
        return list_of_rows, 'Success' # this function return list of dictionary

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):

        """ add task and priority to list of row

        :param task: task from user to be added
        :param priority: priority of task to be added to list/Table
        :param list_of_rows: list of table that new task add to it
        :return: list of Row after adding
        """
        row = {"Task": task.strip(), "Priority": priority.strip()} # put new task and priority in dic row
        list_of_rows.append(row) # add new dic. to end of the list
        return list_of_rows, 'success' # return updated lis of dictionary

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ remove task from list of row

        :param task: task to be removed
        :param list_of_rows:list of Table that task removed from
        :return: list of dic after task removed
        """
        for row in list_of_rows:  # for each row in the table
            if row["Task"].lower() == task.lower():  # checks if task to be removed in the list
               list_of_rows.remove(row)  # then remove the task from the table

        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ save data to the file
        :param file_name: file to save data in it
        :param list_of_rows: list of table to save it in file_name
        :return:
        """

        file = open(file_name,"w")
        for row in list_of_rows:  # for each row in the table
            # write the data to the file
          file.write(row["Task"].strip() + ',' + row["Priority"].strip() + '\n')
        file.close()


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Data
        2) Add a new Task
        3) Remove an existing Task
        4) Save Data to File        
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip() # get choice from user
        print()  # Add an extra line for looks
        return choice # return user choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower() # return string

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ gets task and priority from user

        :return:task and priority to be added
        """
        task = input(" Enter new task : ") # get from user task to be added
        priority = input(" Task priority [high/low]: ")# get priority from user
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ gets task from user

        :return: task to be removed
        """
        task = input("task to remove: ") # get from user the task to remove it
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName,lstTable)
IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table

while(True): # while loop to continue until user want to exit
    # Display a menu of choices to the user
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
# if condition to check user option
    if strChoice.strip() == '1':  # show curent task

        Processor.read_data_from_file(strFileName, lstTable)  # call function read data fro file
        IO.print_current_Tasks_in_list(lstTable) # fuction to print current task
        IO.input_press_to_continue(strStatus) # ask user to continue or no
        continue  # to show the menu

    elif strChoice.strip() == '2':  # Add a new Task
        # call function to ask user which task to add
        strTask, strPriority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable) # pass the argument task and priority to be added
        IO.print_current_Tasks_in_list(lstTable) # call function print current task
        IO.input_press_to_continue(strStatus)# call function for continuty
        continue  # to show the menu

    elif strChoice == '3':  # Remove an existing Task

        strTask = IO.input_task_to_remove() # assign return value from function to strtask
        Processor.remove_data_from_list(strTask, lstTable) # pass it to function to remove task
        IO.print_current_Tasks_in_list(lstTable)# print list
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '4':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ") # make sure to user if want to save
        if strChoice.lower() == "y": # if answer y
            Processor.write_data_to_file(strFileName, lstTable) # call function write to file
            IO.input_press_to_continue(strStatus) # ask for continue
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!") # notice to user
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName,lstTable) # call function first to read data from file
            # return list of table
            IO.print_current_Tasks_in_list(lstTable) # print it so user can see it
            IO.input_press_to_continue(strStatus) # ask for continue
        else:
            IO.input_press_to_continue("File Reload  Cancelled!") # else reload cancel
        continue  # to show the menu1

    elif strChoice == '6':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
