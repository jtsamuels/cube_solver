from functions import cube_setup, search_funcs

# TEST IF TOP FACE ROTATION IS WORKING FOR TOP_ROW_LEFT() AND TOP_ROW_RIGHT()
state_list = []
size = 2
cube = cube_setup.solved_cube(size)
cube = cube_setup.top_row_right(cube, size)[0]
cube = cube_setup.bottom_row_right(cube, size)[0]
#cube = cube_setup.top_row_right(cube, size)[0]
#cube = cube_setup.randomize_cube(size)

cube, moves = search_funcs.bfs(size, cube)

#cube_setup.print_cube(cube,size)
print(moves)