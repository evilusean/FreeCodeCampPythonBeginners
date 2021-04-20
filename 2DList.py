number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#print(number_grid[0][2])
# lists within lists [0]=row [2]= grid [0][2] =3

for row in number_grid:
    for col in row:
        print(col)

#print(row) prints rows [1,2,3], etc.
# print column individual
