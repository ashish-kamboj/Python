## Given two arbitary and axes-aligned rectangles, write a function to compute the area of overlap between the recangles.
## The function should return 0 if there is no overlap.
## Otherwise, the function should return the area of overlap as shown in the examples below.


## Function for calculating the overlap between two lines
def linOverlap(line1, line2):

    coord_1, coord_2 = line1
    coord_3, coord_4 = line2

    if(coord_1 > coord_2):
        coord_1, coord_2 = coord_2, coord_1

    if(coord_3 > coord_4):
        coord_3, coord_4 = coord_4, coord_3


    """[Scenario 1]
    |------------|
            |------------|
    """
    if(coord_1 < coord_3 and coord_2 < coord_4):
        print('Scenario 1')
        return abs(coord_2 - coord_3)


    """[Scenario 2]
            |------------|
    |------------|
    """
    if(coord_1 > coord_3 and coord_2 > coord_4):
        print('Scenario 2')
        return abs(coord_4 - coord_1)


    """[Scenario 3]
        |------------|
    |--------------------|
    """
    if(coord_1 >= coord_3 and coord_2 <= coord_4):
        print('Scenario 3')
        return abs(coord_2 - coord_1)


    """[Scenario 4]
    |--------------------|
        |------------|
    """
    if(coord_1 <= coord_3 and coord_2 >= coord_4):
        print('Scenario 4')
        return abs(coord_4 - coord_3)


    """[Scenario 5]
    |------------|  |------------|
    """
    if(coord_2 <= coord_3 and coord_2 < coord_4):
        print('Scenario 5')
        return 0


    """[Scenario 6]
    |------------|------------|  
    """
    if(coord_1 >= coord_4 and coord_1 < coord_3):
        print('Scenario 6')
        return 0



## Function for calculating the area of overlap between two rectangles
def recOverlap(rect1, rect2):

    (x1,y1),(x2,y2) = rect1
    (x3,y3),(x4,y4) = rect2
	
    x_overlap = linOverlap((x1,x2), (x3,x4))
    y_overlap = linOverlap((y1,y2), (y3,y4))
	
    return x_overlap * y_overlap
	


## Need to pass the diagonal coordinates of both the rectangles (those are sufficent to calculate the area of overlap)
# rect1 = [(1,3), (5,10)]
# rect2 = [(4,5), (10,3)]

# rect1 = [(2,2), (6,4)]
# rect2 = [(5,1), (9,5)]

rect1 = [(2,4), (6,2)]
rect2 = [(5,5), (9,1)]

## Calculating area of overlap
print("Overlapped Area is :: ", str(recOverlap(rect1, rect2)))


