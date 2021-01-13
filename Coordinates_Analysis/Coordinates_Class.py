################################################
# File: Coordinates_Class.py
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
class Coordinates:
    def __init__(self, X, Y):
        self.X_coord = X
        self.Y_coord = Y
    def __str__(self):
        return str(self.X_coord) + ", " + str(self.Y_coord)
