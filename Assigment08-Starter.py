# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# David Grunloh,06.01.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        David Grunloh,06.01.2021,Modified the product class to complete assignment
    """
    # pass
    # TODO: Add Code to the Product class
    def __init__(self, product_name, product_price):
        self.__product_name = ''
        self.__product_price = ''
        self.product_name = product_name
        self.product_price = product_price

    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        if not name.isnumeric():
            self.__product_name = name
        else:
            raise Exception("Names can't be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        try:
            self.__product_price = float(value)  # cast to float
        except ValueError:
            raise Exception("Prices must be numbers")

    # # -- Methods --
    def __str__(self):
        return self.product_name + ',' + str(self.product_price)
    #
    def __doc__(self):
       return 'This class holds product data'
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        David Grunloh,06.01.2021,Modified FileProcessor to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list

        :param file_name: (string) with name of file:
        :param (list_of_rows) list of rows
        :return: (list_of_rows) of rows
        """
        listTable = []  # clear current data
        try:
            file = open(file_name, "r")
            for row in file:
                strData = row.split(",")
                objP = Product(product_name=strData[0].strip(),
                              product_price=strData[1].strip())
                listTable.append(objP)
            file.close()
        except FileNotFoundError:
            print("File not found. ")
        return listTable

    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """Writes list data to the file

        :param file_name: (string) with name of file:
        :param list_of_rows: list_of_objects: (list) of dictionary rows
        :return: list_of_rows: list_of_rows: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for prd in list_of_rows:
            file.write(prd.product_name + ',' + str(prd.product_price) + "\n")
        file.close()
        return 'Success'

    @staticmethod
    def add_data_to_list(objP, list_of_rows):
        """Adds data to the list

        :param (string): product
        :param list_of_rows: (list) you want filled with file data:
        :return: (list of rows) of dictionary rows
        """
        list_of_rows.append(objP)
        return list_of_rows

# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    # pass
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new product
        2) View Data from list        
        3) Save Data to File
        4) Exit the program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_product_in_list(list_of_rows):
        """ Shows the current Tasks in the list

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for prod in list_of_rows:
            print(prod.product_name + "," + str(prod.product_price))
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_data():
        """Allows user to input a new product and cost

        :return list_of_rows: (list) of rows you want to display
        """
        product_name = str(input("What is the product name? - ")).strip()
        product_price = str(input("What is the product cost? - ")).strip()
        objP = Product(product_name=product_name,
                          product_price=product_price)
        return objP

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts


lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data


# Show user a menu of options
while(True):
    # Step 3 Show current data
    IO.print_current_product_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu

# Get user's menu option choice
    strChoice = IO.input_menu_choice()  # Get menu option

    # Let user add data to the list of product objects
    if strChoice.strip() == '1':  # Add a new Task
        data = IO.input_new_product_data()
        FileProcessor.add_data_to_list(data, lstOfProductObjects)
        continue  # to show the menu

    # Show user current data in the list of product objects
    elif strChoice == '2':  # Remove an existing Task
        IO.print_current_product_in_list(lstOfProductObjects)
        continue  # to show the menu

    # let user save current data to file and exit program
    elif strChoice == '3':   # Save Data to File
            FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)

    # let user exit the program
    elif strChoice == '4':  #  Exit the program
        input("Press enter to exit the program")
        break
    else:
        print("Please select a valid option. ")

# Main Body of Script  ---------------------------------------------------- #

