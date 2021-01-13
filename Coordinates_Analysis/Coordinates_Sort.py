################################################
# File: Coordinates_Sort.py
# Author: Jonathan Troy Hunt
# Date: 4/26/2017
# Email: jthunt92@gmail.com
# Class: CSC 231 Data Structures -- Universtiy of North Carolina Wilmington
# Description:
#
#   Importing a list a digits, find the following:
#   The Number of points
#   Closest points to the origin
#   The two closest points
#
################################################

from Coordinates_Class import *
import math
file_name = input("What is the name of the input file?")
file = open(file_name, "r")

coord_list = []
for line in file:
    tokens = line.split()
    X_coord = tokens [0]
    Y_coord = tokens [1]
    X_coord = float(X_coord)
    Y_coord = float(Y_coord)
    coord_pair = Coordinates(X_coord, Y_coord)
    coord_list.append(coord_pair)


def numOfPoints(coord_list):
    """
    Simple method, only goes through th list and creates a counter for each loop
    Big"O" = O(n)
    """
    pairs = 0
    for i in coord_list:
        pairs += 1
    return pairs


def get_distance_origin(x, y):
    """
    uses distance formula, assumes that the origin is 0,0
    Big"O" = O(1)
    """
    X_value = x**2
    Y_value = y**2
    distance_var = X_value + Y_value
    dist_from_origin = math.sqrt(distance_var)
    return dist_from_origin


def dist_from_zero(coord_list):
    """
    Goes through each value to see its value from the origin
    Big"O" = O(n)
    """
    start = coord_list[0]
    start1 = get_distance_origin(start.X_coord, start.Y_coord)
    for r in coord_list:
        distance = get_distance_origin(r.X_coord, r.Y_coord)
        if distance == None:
            return start1
        if distance <= start1:
            start1 = distance
            coordinates = r.X_coord , r.Y_coord
    return coordinates


def distance_between_point(first_set,second_set):
    """
    takes the points and breaks them down into x1, x2, y1, y2
    the following formula is then used :
    distanceFormula = sqrt(((x1+x2)**2)+(y1+y2)**2)
    Big"O" = O(1)
    """
    if second_set == None:
        return
    f_point = first_set
    s_point = second_set
    x1 = first_set.X_coord
    x2 = second_set.X_coord
    y1 = first_set.Y_coord
    y2 = second_set.Y_coord
    x3 = x1 - x2
    y3 = y1 - y2
    x4 = x3**2
    y4 = y3**2
    xy_var = x4 + y4
    dist = math.sqrt(xy_var)
    return dist


def sorter(some_list):
    """
    The purpose of this function is to got through every possible combination of
    coordinates in order to find the correct one.
    Big"O" = O(n^2)
    """
    o = 0
    n = 1
    dist = 0
    min_dist = distance_between_point(coord_list[0], coord_list[1])
    for r in coord_list:
        n=1
        for i in coord_list:
            if n == len(coord_list):
                break
            if n != o:
                dist = distance_between_point(coord_list[o], coord_list[n])
            if dist < min_dist:
                min_dist = dist
                coord_A = coord_list[o]
                coord_B = coord_list[n]
            n += 1
        o += 1
        if o == len(coord_list):
            break
    print("The two closest points are (" + str(coord_A)+') and (' + str(coord_B)+ ')')


print("The number of points is",numOfPoints(coord_list) )
print("The closest point to the origin is",dist_from_zero(coord_list))
sorter(coord_list)
