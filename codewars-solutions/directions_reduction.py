# https://www.codewars.com/kata/directions-reduction/python

def dirReduc(arr):
    reducibles = {
        'EAST': 'WEST',
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'WEST': 'EAST',
    }
    finished = False
    while finished == False:
        finished = True
        for i in range(len(arr)):
            if i < len(arr)-1:
                if arr[i] == reducibles[arr[i+1]]:
                    del arr[i+1]
                    del arr[i]
                    finished = False
            else: break
    return arr