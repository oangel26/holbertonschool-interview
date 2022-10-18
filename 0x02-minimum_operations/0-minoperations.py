#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
     """
     In a text file, there is a single character H. Your text editor can
     execute only two operations in this file: Copy All and Paste. Given
     a number n, write a method that calculates the fewest number of
     operations needed to result in exactly n H characters in the file.
     """
     s_file = 'H'
     num_operation = 1
     def copy_all(new_file):
         s_file = new_file
         num_operation += 1
         return s_file

     def paste(s_file):
         tmp = s_file
         s_file = tmp * 2
         num_operation += 1
         return s_file

     if (n == 0):
         return 0
     elif (n == 1):
         return num_operation
     elif (n % 3 == 0):
         for i in range(int(n/3) - 1):
             paste(s_file)
             copy_all(s_file)
             paste(s_file)
             paste(s_file)
     elif (n % 2 == 0):
         for i in range(int(n/2) - 1):
             paste(s_file)
             copy_all(s_file)
             paste(s_file)

     return num_operation
