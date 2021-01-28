import numpy as np
from collections import deque
from matplotlib import pyplot as plt

# Assignment - Movie Theater Seating Challenge:
# Check ReadMe for more information



def findZeros(array):
    #Helper code was assisted by stackoverflow implementation
    #This code helps find the continuous Zeros in each row (Called by Main)
    iszero = np.concatenate(([0], np.equal(array, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    a = []
    range_int = []
    for i in ranges:
        a.append(i[1]-i[0])
        range_int.append(i[0])
    return [a, range_int]

def getReservations():
    #Code will export the information in the file - to be extracted
    reservations_input = deque() 
    reservation_id = []
    with open('test1.txt', 'r') as input_file:
        input_content = input_file.read().split('\n')
        for row in input_content:
            reservations_input.append(row.split(" ", 1))
            reservation_id.append(row.split(" ", 1)[0])
        
    input_file.close()
    return [reservations_input, reservation_id]

def updateFrequency(movie_theater, row):
    #Checks the current frequency of the called on row, and updates the movie theater
    # 0 - empty, 1 - Take, 2 - Buffer
    zero = 0
    one = 0
    two = 0
    for i in movie_theater[row]:
        if i == 0:
            zero+=1
        elif i == 1:
            one+=1
        else:
            two+=1
        
    return [zero, one, two]

def addBuffers(movie_theater, row, first_seat, seats_needed, seats_row):
    #This helper function adds additional buffers in the case others have been missed (Does the infront and back buffers)

    #If we are in rows 2-9
    if(row < movie_theater.shape[0]-1 and row >0):
        #next row update
        if first_seat == 0:
            movie_theater[row+1][first_seat: first_seat + seats_needed + 1] = 2
            movie_theater[row-1][np.nonzero(movie_theater[row-1][first_seat: first_seat + seats_needed + 1] == 0)[0] + first_seat] = 2
        else:
            movie_theater[row+1][first_seat-1: first_seat + seats_needed + 1] = 2
            movie_theater[row-1][np.nonzero(movie_theater[row-1][first_seat-1: first_seat + seats_needed + 1] == 0)[0] + first_seat-1] = 2
        
        seats_row[row] = updateFrequency(movie_theater, row)
        seats_row[row + 1] = updateFrequency(movie_theater, row+1)
        seats_row[row - 1] = updateFrequency(movie_theater, row-1)
    #Row 1
    elif (row == 0):
        if first_seat == 0:
            movie_theater[row+1][first_seat: first_seat + seats_needed + 1] = 2
        else:
            movie_theater[row+1][first_seat-1: first_seat + seats_needed + 1] = 2
        
        seats_row[row] = updateFrequency(movie_theater, row)
        seats_row[row + 1] = updateFrequency(movie_theater, row+1)
    #Row 10
    else:
        if first_seat == 0:
            movie_theater[row-1][np.nonzero(movie_theater[row-1][first_seat: first_seat + seats_needed + 1] == 0)[0] + first_seat] = 2
        else:
            movie_theater[row-1][np.nonzero(movie_theater[row-1][first_seat-1: first_seat + seats_needed + 1] == 0)[0] + first_seat-1] = 2
        
        seats_row[row] = updateFrequency(movie_theater, row)
        seats_row[row - 1] = updateFrequency(movie_theater, row-1)
    
    return [movie_theater, seats_row]

def returnResults(return_res):
    #final method to return the results of the program
    file_object  = open("results.txt", "w+") 

    for i in range(len(return_res)):
        file_object.write(return_res[i] + '\n')
    file_object.close() 

def main():
    #Main
    reservations_input, reservation_id = getReservations()
    seats_row = np.repeat(np.array([[20, 0, 0]]), 10, axis=0)
    return_res = []

    #Setting up movie theater
    movie_theater = np.zeros((10,20), dtype=int)

    counter = 0
    for reservation in reservation_id:
        res_num, seats_needed  = reservations_input.popleft()
        seats_needed = int(seats_needed)
        rows_seating = seats_row[:, 0]
    
        found_seats = 0
        row = -1
        first_seat = -1

        #Finds the best row with adequate space (backmost first)
        for row_check in range(0,10):
            runs, range_int = findZeros(movie_theater[row_check])
            for i in range(len(runs)):
                if runs[i] >= seats_needed:
                    found_seats = 1
                    first_seat = range_int[i]
                    row = row_check
                    break
        if(row == -1):
            return_res.append(res_num + " CANCELLED")
            continue
            
        
        #seats taken = 1
        movie_theater[row][first_seat: first_seat + seats_needed] = 1
        #seats buffered = 2
        movie_theater[row][first_seat + seats_needed:first_seat + seats_needed + 3] = 2

        movie_theater, seats_row = addBuffers(movie_theater, row, first_seat, seats_needed, seats_row)
        
        row_char = chr(65+row)
    
        ticket_seats = []
        
        #Concatenates string
        for i in range(first_seat, first_seat + seats_needed):
            ticket_seats.append(row_char + str(i+1))
        s = ','
        s = s.join(ticket_seats)
        return_res.append(res_num + " " + s)
        counter+=1
        
    
    returnResults(return_res)
    
    # plt.imshow(movie_theater, interpolation='nearest', extent=[-1,1,-10,10],aspect='auto')
    # plt.savefig('movie_seating.png')
    


        


    # print("Hello World!")

if __name__ == "__main__":
    main()