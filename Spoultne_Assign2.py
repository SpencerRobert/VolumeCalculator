#Spencer Poultney, October 23rd 2017
#'''This program allows the user to select a specified shape, provide certain measurements for it, and have its volume calculated for it'''

#Creating the main function
def main():
    #Importing time to add the delays
    import time
    #Creating lists of volumes
    cubeVolumes = []
    pyramidVolumes = []
    ellipsoidVolumes = []
    #Creating sentinel value for exiting
    quitting = "FALSE"
    #Creating sentinel value for errors
    isError = "FALSE"

    while quitting == "FALSE":
        if isError == "FALSE":
            #Getting shape user wants to find volume of
            shapeSelection = input("Please enter what shape you would like the volume calculated for (Cube, Pyramid, Ellipsoid, or Quit to exit): ").upper()
            #Allows user to enter Cube or C with any variation of capital letters to select cube
        if shapeSelection == "CUBE" or shapeSelection == "C":
            #Gets side length of cube from user
            sideLength = float(input("Please enter a side length of the cube: "))
            cubeVolumes.append(volumeOfCube(sideLength))
            #No errors
            isError = "FALSE"

        #Similar process to cube except more input variables are required
        elif shapeSelection == "PYRAMID" or shapeSelection == "P":
            baseLength = float(input("Please enter the length of the base of the pyramid: "))
            pyramidHeight = float(input("Please enter the height of the pyramid: "))
            pyramidVolumes.append(volumeOfPyramid(baseLength, pyramidHeight))
            isError = "FALSE"

        #Again, same process except with even more input variables.
        elif shapeSelection == "ELLIPSOID" or shapeSelection == "E":
            radius_1 = float(input("Please enter the first radius of the ellipsoid: "))
            radius_2 = float(input("Please enter the second radius of the ellipsoid: "))
            radius_3 = float(input("Please enter the third radius of the ellipsoid: "))
            ellipsoidVolumes.append(volumeOfEllipsoid(radius_1, radius_2, radius_3))
            isError = "FALSE"

        #If sentinel value is chosen
        elif shapeSelection == "QUIT":
            quitting = "TRUE"

        else:
            #If an invalid option is entered
            shapeSelection = input("Sorry, that selection is not supported in this program. Please choose either (Cube, Pyramid, Ellipsoid, or Quit to exit): ").upper()
            #There then is an error
            isError = "TRUE"

    if quitting == "TRUE":
        #Prints calculation message and loading dots
        print("Now making your calculations")
        import sys
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.8)

        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.8)

        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.8)

        #If user enters input for all three shapes
        if cubeVolumes != [] and pyramidVolumes != [] and ellipsoidVolumes != []:
            #\n prints the line below my 3 dot loading 'annimation'
            print("\nThe values you have chosen to calculate are below:")
            print("Cube", end=": ")
            cubeVolumes.sort()
            noBracketList(cubeVolumes)
            print("Pyramid", end=": ")
            pyramidVolumes.sort()
            noBracketList(pyramidVolumes)
            print("Ellipsoid", end=": ")
            ellipsoidVolumes.sort()
            noBracketList(ellipsoidVolumes)
            #ALL TIME DELAYS ALLOW FOR USER TO VIEW CALCULATIONS FOR SPECIFIED TIME IN SECONDS
            time.sleep(8)

        #If user enters input for pyramids and ellipsoids
        elif cubeVolumes == [] and pyramidVolumes != [] and ellipsoidVolumes != []:
            print("\nThe values you have chosen to calculate are below:")
            print("Cube: No computations for this shape")
            print("Pyramid", end=": ")
            pyramidVolumes.sort()
            noBracketList(pyramidVolumes)
            print("Ellipsoid:", sorted(ellipsoidVolumes))
            ellipsoidVolumes.sort()
            noBracketList(ellipsoidVolumes)
            time.sleep(8)

        #If user enters input for cubes and ellipsoids
        elif cubeVolumes != [] and pyramidVolumes == [] and ellipsoidVolumes != []:
            print("\nThe values you have chosen to calculate are below:")
            print("Cube", end=": ")
            cubeVolumes.sort()
            noBracketList(cubeVolumes)
            print("Pyramid: No computations for this shape")
            print("Ellipsoid", end=": ")
            ellipsoidVolumes.sort()
            noBracketList(ellipsoidVolumes)
            time.sleep(8)

        #If user enters input for cubes and pyramids
        elif cubeVolumes != [] and pyramidVolumes != [] and ellipsoidVolumes == []:
            print("\nThe values you have chosen to calculate are below:")
            print("Cube", end=": ")
            cubeVolumes.sort()
            noBracketList(cubeVolumes)
            print("Pyramid", end=": ")
            pyramidVolumes.sort()
            noBracketList(pyramidVolumes)
            print("Ellipsoid: No computations for this shape")
            time.sleep(8)

        #If user enters input for only pyramids
        elif cubeVolumes == [] and pyramidVolumes != [] and ellipsoidVolumes == []:
            print("\nThe values you have chosen to calculate are below:")
            print("Cube: No computations for this shape")
            print("Pyramid", end=": ")
            pyramidVolumes.sort()
            noBracketList(pyramidVolumes)
            print("Ellipsoid: No computations for this shape")
            time.sleep(8)

        #If user enters input for only ellipsoids
        elif cubeVolumes == [] and pyramidVolumes == [] and ellipsoidVolumes != []:
            print("\nThe values you have chosen to calculate are below:")
            print("Cube: No computations for this shape")
            print("Pyramid: No computations for this shape")
            print("Ellipsoid ", end=": ")
            ellipsoidVolumes.sort()
            noBracketList(ellipsoidVolumes)
            time.sleep(8)

        #If user enters input for only cubes
        elif cubeVolumes != [] and pyramidVolumes == [] and ellipsoidVolumes == []:
            print("\nThe values you have chosen to calculate are below:")
            print("Cube", end=": ")
            cubeVolumes.sort()
            noBracketList(cubeVolumes)
            print("Pyramid: No computations for this shape")
            print("Ellipsoid: No computations for this shape")
            time.sleep(8)

        else:
            #If user enters no input for any shapes
            print("\nYou did not choose to do any volume calculations.")
            time.sleep(8)

#Creating function that calculates volume a cube
def volumeOfCube(sideLength):
    while True:
        if sideLength > 0:
            volume = round(sideLength**3, 1)
            print("The volume of a cube with a side length of {} is: {}".format(round(sideLength, 1), round(volume, 1)))
            break
        else:
            sideLength = float(input("Please enter a length greater than 0: "))

    return float(volume)

#Creating function that calculates volume of a pyramid
def volumeOfPyramid(baseLength, pyramidHeight):
    while True:
        if baseLength <= 0:
            baseLength = float(input("Please enter a base length greater than 0: "))
            continue
        elif pyramidHeight <= 0:
            pyramidHeight = float(input("Please enter a pyramid height greater than 0: "))
            continue
        else:
            volume = round(((baseLength**2)*pyramidHeight)/3, 1)
            print("The volume of the pyramid with the base length of {} and the height of {} is: {}".format(round(baseLength, 1), round(pyramidHeight, 1), round(volume, 1)))
            break
    return float(volume)

#Creating function that calculates volume of a ellipsoid
def volumeOfEllipsoid(radius_1, radius_2, radius_3):
    from math import pi
    while True:
        if radius_1 <= 0:
            radius_1 = float(input("Please enter a radius that's greater than 0: "))
            continue
        elif radius_2 <= 0:
            radius_2 = float(input("Please enter another radius that's greater than 0: "))
            continue
        elif radius_3 <= 0:
            radius_3 = float(input("Please enter one more radius that is greater than 0: "))
        else:
            volume = round((4*pi*radius_1*radius_2*radius_3)/3, 1)
            print("The volume of the ellipsoid with a radius of {} and {} and {} is: {}".format(round(radius_1, 1), round(radius_2, 2), round(radius_3 , 1), volume))
            break
    return float(volume)

#Creates function
def noBracketList(listElements):
    for l in range(len(listElements)):
        if listElements[l] == listElements[len(listElements) - 1]:
            print(listElements[l])
        else:
            print(listElements[l], end=", ")


#Calling main function to allow the whole program to actually run
main()









