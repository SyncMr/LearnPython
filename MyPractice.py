#! /usr/bin/env 

#-------------------------------------------------------------------------------------------
# sumOfNum(myList)
#       Function to calculate the sum of numbers
#-------------------------------------------------------------------------------------------
def sumOfNum(myList):
    sumList = 0

    for elmt in myList:
        sumList += elmt

    return sumList

#-------------------------------------------------------------------------------------------
# printList(myList)
#       Function to calculate the sum of numbers
#-------------------------------------------------------------------------------------------
def printList(myList):

    # METHOD 1
    print(myList)

    # METHOD 2
    for elmt in myList:
        # Extra comma at end makes sure that it gets printed on the same line
        print(elmt, ', ', end=''),
    print()

    # METHOD 3
    for index in range(len(myList)):
        # Extra comma at end makes sure that it gets printed on the same line
        print(myList[index], ', ', end=''),
    print()

#-------------------------------------------------------------------------------------------
# getInputList(myList):
#        Get Input Numbers to a list
#-------------------------------------------------------------------------------------------
# Main Function
def getInputList(myList):
    # Get a list of numbers until the user enters a blank line
    line = input("Enter list of numbers: \n")

    #while (line not in ['\n', '\r\n']):
    while (line):
        myList.append(int(line))

        line = input()

        if (line in ('\n', '\r\n')):
            break

#-------------------------------------------------------------------------------------------
# findFirstRepeatedChar(myStr):
#       Find First Repeated Char
#-------------------------------------------------------------------------------------------
def findFirstRepeatedChar(myStr):
    strDict = {}
    repChar = ''

    for c in myStr:
        if (c in strDict):
            repChar = c
            break;
        else:
            strDict[c] = 1

    if (repChar):
        print("First Repeated Char in \"%s\" : %c" % (myStr, repChar))
    else:
        print("No Repeated Char in \"%s\"" % myStr)

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    print("hello")

    # Declare a list
    myList = []

    # Fill the list with Numbers
    getInputList(myList)

    # Print the List
    printList(myList)

    # Calculate the Sum of Numbers in the List
    sumList = sumOfNum(myList)

    # Problem 1
    # Use the inbuilt sum function to get the sum
    print(sum(myList))
    print(sumList)

    # Problem 2
    # Find First Repeated Character in a String
    myStr = "helola"
    print(myStr.__doc__)
    repChar = findFirstRepeatedChar(myStr)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
