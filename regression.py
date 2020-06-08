#This program was created by Suryanuj Gupta. He created to practice python coding and how it can be used in statistics. 
import statistics
import matplotlib.pyplot as plt
import numpy as np

#This functions takes user input and asks them to enter the number of coordinates they have and what those coordinates are.
def data_collection_xy()->[list]:
    numberList = []
    n = int(input("Enter the # of Coordinates Values: "))
    for i in range(0, n):
        print("Enter coordinate #", i+1, ":")
        item = input()
        numberList.append(item)
    #print("Coordinates are: ", numberList)
    return numberList

#This functions spilts the coordinates by commas, helpful for taking the only x and y values
def split_coordinates (numberList:[list])->[list]:
    split_list=[]
    for a_item in numberList:
        split_list.append(a_item.split(','))
    #print("New List: ", split_list)
    return(split_list)

def main (split_list:[list])->[list]:
    #Adds all X cooridnates to the x_split list
    x_split=[]
    for a_x in split_list:
        x_split.append(float(a_x[0]))
    #print("X Values: ", x_split)

    # Adds all Y coordinates to the y_split list
    y_split=[]
    for a_y in split_list:
        y_split.append(float(a_y[1]))
    #print("Y Values: ", y_split)

    #Gets the mean of the x coordinates
    x_avg=statistics.mean(x_split)
    #print("The X values average is: ", x_avg)

    #Gets the mean of the y cooridnates
    y_avg=statistics.mean(y_split)
    #print("The Y values average is: ", y_avg)

    #Gets the mean of both the x and y cooridnates, combined
    bothxy=[x*y for x,y in zip(x_split,y_split)]
    bothxy=statistics.mean(bothxy)
    #print("Combined X and Y's mean is: ", bothxy)

    #Squares the x cooridantes' average
    squared_x_avg=x_avg**2
    #print("Squared mean of X: ", squared_x_avg)

    #Squares each X cooridnate in the list, makes a new list
    x_coordinate_sq=[]
    for a_x in split_list:
        x_coordinate_sq.append((float(a_x[0])**2))
    #print("X Values squared in list: ", x_coordinate_sq)

    #Gets the mean of this new list
    listsquare = statistics.mean(x_coordinate_sq)
    #print("x squared mean: ", listsquare)

    m=(((x_avg)*(y_avg))-(bothxy))/((x_avg**2)-(listsquare))
    #print("M (Slope) is: ", m)

    b=(y_avg)-((m)*(x_avg))
    #print("B (Y-Intercept) is: ", b)

    #X Axis Range
    x_range=sorted(x_split)[-1]
    x_range=round(x_range)
    x = np.array(range(x_range+5))

    #Y Formula Equation
    y=m*x + b

    print("\nRegression Formula is: y = "+ str(round(m,2)) +"x + " +str(round(b,2)))
    
    plt.title("Line of Best Fit")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(x, y)
    plt.scatter(x_split, y_split)
    plt.show()

if __name__ == "__main__":
    main(split_coordinates(data_collection_xy()))