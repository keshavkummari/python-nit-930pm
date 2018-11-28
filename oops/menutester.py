# menutester.py
# This program tests the menu class

from menu import Menu

mainMenu = Menu()

mainMenu.addOption("Open new account")

mainMenu.addOption("Log into existing account")

mainMenu.addOption("Help")

mainMenu.addOption("Quit")

choice = mainMenu.getInput()

print("Input",choice)

