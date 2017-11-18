# Created by : James Lee
# Created on : 13 Nov. 2017
# Created for : ICS3UR
# This program shows the largest number in an array

def find_highest_value(arrays = []):
    # Finds the highst value in am array

    value_number_in_array = 0

    for value in arrays:
         if value_number_in_array < value:
            value_number_in_array = value
         else: 
            value_number_in_array = value_number_in_array
                            
    return value_number_in_array                                 

array = [5,4,7,9,3,10]
find_highest_value(array)

max_value = find_highest_value(array)
print("The max value of the array is: " + str(max_value))
