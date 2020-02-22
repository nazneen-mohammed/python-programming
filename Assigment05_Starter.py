# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "homeInventory.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Nazneen  m, 02/20/2020 Created a script to make a list and dictionary from File.
# Adding item to a liist of dictionary, removing items from list of dictionary and
# save change to file again .
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "homeInventory.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- # Step 1 - When the program s1tarts, load the any data you have
# in a text file called homeInventory.txt into a python Dictionary.
# Use a for loop to build a table of dictionaries
objFile = open("homeInventory.txt",'r') # open the homeInventory file to be ready for read
for row in objFile:
     # For each row in the objFile look for "," by  split function
    lstRow = row.split(",")
     # create a dictionary of Item and Value and take away any unlike character by strip
    dicRow = {"Item":lstRow[0].strip(), "Value":lstRow[1].strip()}
    lstTable.append(dicRow) # adding the ddictionary to a table
objFile.close() # file closed after reading its data to memory (lstTable)
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding empty line after to look clear
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'): # checks the user optition if 1 execute the followig steps
        print("\n--- using a Dictionary objects-----\n")
        objFile = open("homeInventory.txt", "r") # open the file to read from it the data
        for row in objFile: # for each row in the file
           lstRow = row.split(",") # looking for "," by split function
           # create a dictionary in the statement below
           dicRow = {"Item":lstRow[0].strip(), "Value": lstRow[1].strip()}
           # display the current data
           print(dicRow)
        objFile.close() # close the file after finished read from it

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'): # checks users option if =2 perform the steps below
        lstTable = [] # set list of table to empty value
        dicRow = {} # set the dictionary to empty value
        objFile = open("homeInventory.txt","r") # open the file to read data from it
        for row in objFile: # for each row in the file
            lstRow = row.split(",") # looking for "," end of the first item
            dicRow = {"Item": lstRow[0], "Value": lstRow[1]} # create the dictionary
            lstTable.append(dicRow) # append the dictionary items to lastTable
        print(lstTable , '<<list with Dictionary object >>') # printing out the list of dictionary
        objFile.close() # closing objFile after reading data to memory

        while (True): # loop for repeating adding Items
              strItem = input("Item to be added: ") # get from user the item to be added
              strValue = input("Value: ")  # get from user the price of the item
              lstTable.append({"Item":strItem, "Value":strValue}) # append the item and its value to lstTable
              strChoice = input("exit?('y/n'):") # asking the user if want to exit or staying adding item
              if strChoice.lower() == 'y': # checking the user decision if y exit if n asking for adding item3
               break # then break (stop) return to main menu
        # then print the list of dictionary
        print(lstTable ,  '<< list with Dictionary object after adding items >>')

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'): # if the user choice 3 then perfom removing item
        dicRow = {} # set the dictionary to empty value
        print(lstTable , '<<list with Dictionary object >>') # displaty the table for user to see
        # which item to remove
        while(True): # loop for repeation removing item
            strItem = input("Item to remove: ") # get from user the item to remove it
            strStatus="row not found" # set this string to row not found
            for row in lstTable: # for each row in the table
                if row["Item"].lower() == strItem.lower(): # checks if item to be removed the same
                    # as an item in table and chang both to loweer case for matching
                    lstTable.remove(row) # then remove the item from the table
                    strStatus=("row removed") # then set the string status to row found

            print(strStatus) # print strStatus found or not found
            print("Curent Data", lstTable) # then print out the current data
            strChoice = input("exit?('y/n'):") # get from user want continue remove or exit (y,n)
            if strChoice.lower() == 'y': # checks if user choose y the
               break   # stop then return to main menu
            # dispplay current data
            print(lstTable, '<<with Dictionary object')
            continue # go back to remove another item
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'): # checks user choice if 4 then execute
        # these steps for saving data to file
         objFile = open("homeInventory.txt","w") # open the file for write on it
         for row in lstTable: # for each row in the table
             # write the data to the file
            objFile.write(str(row["Item"]).strip() + ',' + str(row["Value"].strip() + '\n'))
          # after writting all data from memory place to file then close it
         objFile.close()
         print("now in file") # print for user data now in file
         continue # return to main menue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'): # checks if the user choice =5 then exit
       break # exit the while loop and Exit the program
    else:
        #  give the user hint to choos the correct option
        print( " please choose the options from [1-5] ")
# after exiting the program this will print out
print ("end of task") # print for user end of task

