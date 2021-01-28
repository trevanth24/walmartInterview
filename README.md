# Walmart Interview

Hello welcome to my implementation of the assignment - "Movie Theater Seating Challenge". Below you will find my thoughts on the current implementation of my code, and 
commented code that will walk through the ideas of this project.

This project was worked in with Python 3 and requires a few libraries to be installed:
  1. Python 3
  2. NumPy
  3. (OPTIONALLY) matplotlib
    -You can view the movie theater as an image (uncomment the last 2 lines of the main function). The Purple is the empty space, yellow is the buffer and green is the taken seats
  

Assignment - Movie Theater Seating Challenge:

Fulfill reservation requests with the arrangement of 10 rows x 20 seats. 
Design and write a seat assignment program to maximize safety and satisfaction

    When you think about safety:
    1. Being distanced away from others (3 seat distance or the end of the seating row)
    2. Buffer is one row in front and three seats to the side (even one diagonal)
    3. Row in front is important since a cough or sneeze is affected more in front of you
    4. Safety of customers is number one, and cancellations may occur with insufficient seating
    
    When you think about satisfaction:
    1. If you reserved first, you want good seats (back and middle is the best)
    2. Being seated together (at least close)
    
    Considerations
    1.Splitting people would be a suboptimal solution, however, needed.
    
    Things to consider in the future:
    1. Back seats are not the BEST, a few rows in front are the best.
    2. Optimally placing people for maximizing seats.
    3. Large groups may have to sacrifice being in a higher row, be able to place them in a close area.
    4. Groups larger than 20 will be cancelled and not split.
