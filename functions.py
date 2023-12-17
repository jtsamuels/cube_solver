import random

# SETUP FUNCTIONS
class cube_setup:
    # Visualize cube more accurately (front, back, left, right, top, bottom)
    def print_cube(cube,size):
        for i in cube:
            for ii in i:
                print(ii,'\n')
            print('\n')
        return None

    # This function just returns a solved cube based on given cube size
    def solved_cube(size):
        y_insert = ['y'] * size
        w_insert = ['w'] * size
        g_insert = ['g'] * size
        b_insert = ['b'] * size
        r_insert = ['r'] * size
        o_insert = ['o'] * size
        matrix = [[],[],[],[],[],[]]
        for ii in range(size):
            matrix[0].append(y_insert)
            matrix[1].append(w_insert)
            matrix[2].append(g_insert)
            matrix[3].append(b_insert)
            matrix[4].append(r_insert)
            matrix[5].append(o_insert)
        #print_cube(matrix,size)
        return matrix

    # This functions copies the cube matrix without dependancies
    # CLARIFICATION... .copy() works on lists but not nested lists (aka matrices)
    def copy_cube(cube,size):
        new_cube = cube_setup.solved_cube(size)
        for i in range(6):
            for ii in range(size):
                new_cube[i][ii] = cube[i][ii].copy()
        return new_cube

    # OPERATIONS...

    # TOP ROW
    def top_row_left(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # top rows: front- cube[0][0][0] & cube[0][0][1], back- cube[1][0][1] & cube[1][0][0], 
        #           left- cube[2][0][1] & cube[2][1][1], right- cube[3][1][0] & cube[3][0][0]
        #           left <- front
        new_cube[2][0][1] = cube[0][0].copy()[0]
        new_cube[2][1][1] = cube[0][0].copy()[1]
        #           back <- left
        new_cube[1][0][1] = cube[2][0].copy()[1]
        new_cube[1][0][0] = cube[2][1].copy()[1]
        #          right <- back
        new_cube[3][1][0] = cube[1][0].copy()[1]
        new_cube[3][0][0] = cube[1][0].copy()[0]
        #          front <- right
        new_cube[0][0][0] = cube[3][1].copy()[0]
        new_cube[0][0][1] = cube[3][0].copy()[0]
        # rotate top face clockwise: 
        # cube[4][0][0] -> cube[4][0][1] -> cube[4][1][1] -> cube[4][1][0] -> cube[4][0][0]
        new_cube[4][0][1] = cube[4][0].copy()[0]
        new_cube[4][1][1] = cube[4][0].copy()[1]
        new_cube[4][1][0] = cube[4][1].copy()[1]
        new_cube[4][0][0] = cube[4][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    def top_row_right(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # top rows: front- cube[0][0][0] & cube[0][0][1], back- cube[1][0][1] & cube[1][0][0], 
        #           left- cube[2][0][1] & cube[2][1][1], right- cube[3][1][0] & cube[3][0][0]
        #           front <- left
        new_cube[0][0][0] = cube[2][0].copy()[1]
        new_cube[0][0][1] = cube[2][1].copy()[1]
        #           right <- front
        new_cube[3][1][0] = cube[0][0].copy()[0]
        new_cube[3][0][0] = cube[0][0].copy()[1]
        #            back <- right
        new_cube[1][0][1] = cube[3][1].copy()[0]
        new_cube[1][0][0] = cube[3][0].copy()[0]
        #           left <- back
        new_cube[2][0][1] = cube[1][0].copy()[1]
        new_cube[2][1][1] = cube[1][0].copy()[0]
        # rotate top face counterclockwise: 
        # cube[4][0][0] <- cube[4][0][1] <- cube[4][1][1] <- cube[4][1][0] <- cube[4][0][0]
        new_cube[4][0][0] = cube[4][0].copy()[1]
        new_cube[4][0][1] = cube[4][1].copy()[1]
        new_cube[4][1][1] = cube[4][1].copy()[0]
        new_cube[4][1][0] = cube[4][0].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    # BOTTOM ROW
    def bottom_row_left(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # bottom rows: front- cube[0][1][0] & cube[0][1][1], back- cube[1][1][1] & cube[1][1][0], 
        #           left- cube[2][0][0] & cube[2][1][0], right- cube[3][1][1] & cube[3][0][1]
        #           left <- front
        new_cube[2][0][0] = cube[0][1].copy()[0]
        new_cube[2][1][0] = cube[0][1].copy()[1]
        #           back <- left
        new_cube[1][1][1] = cube[2][0].copy()[0]
        new_cube[1][1][0] = cube[2][1].copy()[0]
        #          right <- back
        new_cube[3][1][1] = cube[1][1].copy()[1]
        new_cube[3][0][1] = cube[1][1].copy()[0]
        #          front <- right
        new_cube[0][1][0] = cube[3][1].copy()[1]
        new_cube[0][1][1] = cube[3][0].copy()[1]
        # rotate bottom face counterclockwise: 
        # cube[5][0][0] -> cube[5][1][0] -> cube[5][1][1] -> cube[5][0][1] -> cube[5][0][0]
        new_cube[5][1][0] = cube[5][0].copy()[0]
        new_cube[5][1][1] = cube[5][1].copy()[0]
        new_cube[5][0][1] = cube[5][1].copy()[1]
        new_cube[5][0][0] = cube[5][0].copy()[1]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    def bottom_row_right(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # bottom rows: front- cube[0][1][0] & cube[0][1][1], back- cube[1][1][1] & cube[1][1][0], 
        #           left- cube[2][0][0] & cube[2][1][0], right- cube[3][1][1] & cube[3][0][1]
        #           front <- left
        new_cube[0][1][0] = cube[2][0].copy()[0]
        new_cube[0][1][1] = cube[2][1].copy()[0]
        #           right <- front
        new_cube[3][1][1] = cube[0][1].copy()[0]
        new_cube[3][0][1] = cube[0][1].copy()[1]
        #          back <- right
        new_cube[1][1][1] = cube[3][1].copy()[1]
        new_cube[1][1][0] = cube[3][0].copy()[1]
        #          left <- back
        new_cube[2][0][0] = cube[1][1].copy()[1]
        new_cube[2][1][0] = cube[1][1].copy()[0]
        # rotate bottom face clockwise: 
        # cube[5][0][0] <- cube[5][1][0] <- cube[5][1][1] <- cube[5][0][1] <- cube[5][0][0]
        new_cube[5][0][1] = cube[5][0].copy()[0]
        new_cube[5][1][1] = cube[5][0].copy()[1]
        new_cube[5][1][0] = cube[5][1].copy()[1]
        new_cube[5][0][0] = cube[5][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    # LEFT COLUMN
    def left_col_down(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # left cols: front- cube[0][0][0] & cube[0][1][0], back- cube[1][0][1] & cube[1][1][1], 
        #            top- cube[4][0][0] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][0][1]
        #            bot <- front
        new_cube[5][1][1] = cube[0][0].copy()[0]
        new_cube[5][0][1] = cube[0][1].copy()[0]
        #           back <- bot
        new_cube[1][0][1] = cube[5][1].copy()[1]
        new_cube[1][1][1] = cube[5][0].copy()[1]
        #            top <- back
        new_cube[4][0][0] = cube[1][0].copy()[1]
        new_cube[4][1][0] = cube[1][1].copy()[1]
        #          front <- top
        new_cube[0][0][0] = cube[4][0].copy()[0]
        new_cube[0][1][0] = cube[4][1].copy()[0]
        # rotate left face clockwise: 
        # cube[2][0][0] <- cube[2][1][0] <- cube[2][1][1] <- cube[2][0][1] <- cube[2][0][0]
        new_cube[2][0][1] = cube[2][0].copy()[0]
        new_cube[2][1][1] = cube[2][0].copy()[1]
        new_cube[2][1][0] = cube[2][1].copy()[1]
        new_cube[2][0][0] = cube[2][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    def left_col_up(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # left cols: front- cube[0][0][0] & cube[0][1][0], back- cube[1][0][1] & cube[1][1][1], 
        #            top- cube[4][0][0] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][0][1]
        #          front <- bot
        new_cube[0][0][0] = cube[5][1].copy()[1]
        new_cube[0][1][0] = cube[5][0].copy()[1]
        #            top <- front
        new_cube[4][0][0] = cube[0][0].copy()[0]
        new_cube[4][1][0] = cube[0][1].copy()[0]
        #           back <- top
        new_cube[1][0][1] = cube[4][0].copy()[0]
        new_cube[1][1][1] = cube[4][1].copy()[0]
        #            bot <- back
        new_cube[5][1][1] = cube[1][0].copy()[1]
        new_cube[5][0][1] = cube[1][1].copy()[1]
        # rotate left face counterclockwise: 
        # cube[2][0][0] -> cube[2][1][0] -> cube[2][1][1] -> cube[2][0][1] -> cube[2][0][0]
        new_cube[2][1][0] = cube[2][0].copy()[0]
        new_cube[2][1][1] = cube[2][1].copy()[0]
        new_cube[2][0][1] = cube[2][1].copy()[1]
        new_cube[2][0][0] = cube[2][0].copy()[1]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    # RIGHT COLUMN
    def right_col_down(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # right cols: front- cube[0][0][1] & cube[0][1][1], back- cube[1][0][0] & cube[1][1][0], 
        #            top- cube[4][0][1] & cube[4][1][1], bottom- cube[5][1][0] & cube[5][0][0]
        #            bot <- front
        new_cube[5][1][0] = cube[0][0].copy()[1]
        new_cube[5][0][0] = cube[0][1].copy()[1]
        #           back <- bot
        new_cube[1][0][0] = cube[5][1].copy()[0]
        new_cube[1][1][0] = cube[5][0].copy()[0]
        #            top <- back
        new_cube[4][0][1] = cube[1][0].copy()[0]
        new_cube[4][1][1] = cube[1][1].copy()[0]
        #          front <- top
        new_cube[0][0][1] = cube[4][0].copy()[1]
        new_cube[0][1][1] = cube[4][1].copy()[1]
        # rotate right face counterclockwise: 
        # cube[3][0][0] -> cube[3][1][0] -> cube[3][1][1] -> cube[3][0][1] -> cube[3][0][0]
        new_cube[3][1][0] = cube[3][0].copy()[0]
        new_cube[3][1][1] = cube[3][1].copy()[0]
        new_cube[3][0][1] = cube[3][1].copy()[1]
        new_cube[3][0][0] = cube[3][0].copy()[1]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    def right_col_up(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # right cols: front- cube[0][0][1] & cube[0][1][1], back- cube[1][0][0] & cube[1][1][0], 
        #            top- cube[4][0][1] & cube[4][1][1], bottom- cube[5][1][0] & cube[5][0][0]
        #          front <- bot
        new_cube[0][0][1] = cube[5][1].copy()[0]
        new_cube[0][1][1] = cube[5][0].copy()[0]
        #            top <- front
        new_cube[4][0][1] = cube[0][0].copy()[1]
        new_cube[4][1][1] = cube[0][1].copy()[1]
        #           back <- top
        new_cube[1][0][0] = cube[4][0].copy()[1]
        new_cube[1][1][0] = cube[4][1].copy()[1]
        #            bot <- back
        new_cube[5][1][0] = cube[1][0].copy()[0]
        new_cube[5][0][0] = cube[1][1].copy()[0]
        # rotate right face clockwise: 
        # cube[3][0][0] <- cube[3][1][0] <- cube[3][1][1] <- cube[3][0][1] <- cube[3][0][0]
        new_cube[3][0][1] = cube[3][0].copy()[0]
        new_cube[3][1][1] = cube[3][0].copy()[1]
        new_cube[3][1][0] = cube[3][1].copy()[1]
        new_cube[3][0][0] = cube[3][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    # FRONT FACE
    def front_face_clockwise(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # front face surrounding cols: left- cube[2][1][1] & cube[2][1][0], right- cube[3][1][1] & cube[3][1][0], 
        #                              top- cube[4][1][1] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][1][0]
        #          right <- top
        new_cube[3][1][1] = cube[4][1].copy()[1]
        new_cube[3][1][0] = cube[4][1].copy()[0]
        #            bot <- right
        new_cube[5][1][1] = cube[3][1].copy()[1]
        new_cube[5][1][0] = cube[3][1].copy()[0]
        #           left <- bot
        new_cube[2][1][1] = cube[5][1].copy()[1]
        new_cube[2][1][0] = cube[5][1].copy()[0]
        #            top <- left
        new_cube[4][1][1] = cube[2][1].copy()[1]
        new_cube[4][1][0] = cube[2][1].copy()[0]
        # rotate front face clockwise: 
        # cube[0][0][0] <- cube[0][1][0] <- cube[0][1][1] <- cube[0][0][1] <- cube[0][0][0]
        new_cube[0][0][1] = cube[0][0].copy()[0]
        new_cube[0][1][1] = cube[0][0].copy()[1]
        new_cube[0][1][0] = cube[0][1].copy()[1]
        new_cube[0][0][0] = cube[0][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    def front_face_counterclockwise(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # front face surrounding cols: left- cube[2][1][1] & cube[2][1][0], right- cube[3][1][1] & cube[3][1][0], 
        #                              top- cube[4][1][1] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][1][0]
        #            top <- right
        new_cube[4][1][1] = cube[3][1].copy()[1]
        new_cube[4][1][0] = cube[3][1].copy()[0]
        #           left <- top
        new_cube[2][1][1] = cube[4][1].copy()[1]
        new_cube[2][1][0] = cube[4][1].copy()[0]
        #            bot <- left
        new_cube[5][1][1] = cube[2][1].copy()[1]
        new_cube[5][1][0] = cube[2][1].copy()[0]
        #          right <- bot
        new_cube[3][1][1] = cube[5][1].copy()[1]
        new_cube[3][1][0] = cube[5][1].copy()[0]
        # rotate fron face counterclockwise: 
        # cube[0][0][0] -> cube[0][1][0] -> cube[0][1][1] -> cube[0][0][1] -> cube[0][0][0]
        new_cube[0][1][0] = cube[0][0].copy()[0]
        new_cube[0][1][1] = cube[0][1].copy()[0]
        new_cube[0][0][1] = cube[0][1].copy()[1]
        new_cube[0][0][0] = cube[0][0].copy()[1]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    # BACK FACE
    def back_face_clockwise(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # back face surrounding cols: left- cube[2][0][1] & cube[2][0][0], right- cube[3][0][1] & cube[3][0][0], 
        #                              top- cube[4][0][1] & cube[4][0][0], bottom- cube[5][0][1] & cube[5][0][0]
        #          right <- top
        new_cube[3][0][1] = cube[4][0].copy()[1]
        new_cube[3][0][0] = cube[4][0].copy()[0]
        #            bot <- right
        new_cube[5][0][1] = cube[3][0].copy()[1]
        new_cube[5][0][0] = cube[3][0].copy()[0]
        #           left <- bot
        new_cube[2][0][1] = cube[5][0].copy()[1]
        new_cube[2][0][0] = cube[5][0].copy()[0]
        #            top <- left
        new_cube[4][0][1] = cube[2][0].copy()[1]
        new_cube[4][0][0] = cube[2][0].copy()[0]
        # rotate back face clockwise: 
        # cube[1][0][0] <- cube[1][0][1] <- cube[1][1][1] <- cube[1][1][0] <- cube[1][0][0]
        new_cube[1][1][0] = cube[1][0].copy()[0]
        new_cube[1][1][1] = cube[1][1].copy()[0]
        new_cube[1][0][1] = cube[1][1].copy()[1]
        new_cube[1][0][0] = cube[1][0].copy()[1]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    def back_face_counterclockwise(cube,size):
        new_cube = cube_setup.copy_cube(cube,size)
        # JUST FOR 2X2 CUBE FOR NOW
        # back face surrounding cols: left- cube[2][0][1] & cube[2][0][0], right- cube[3][0][1] & cube[3][0][0], 
        #                              top- cube[4][0][1] & cube[4][0][0], bottom- cube[5][0][1] & cube[5][0][0]
        #            top <- right
        new_cube[4][0][1] = cube[3][0].copy()[1]
        new_cube[4][0][0] = cube[3][0].copy()[0]
        #           left <- top
        new_cube[2][0][1] = cube[4][0].copy()[1]
        new_cube[2][0][0] = cube[4][0].copy()[0]
        #            bot <- left
        new_cube[5][0][1] = cube[2][0].copy()[1]
        new_cube[5][0][0] = cube[2][0].copy()[0]
        #          right <- bot
        new_cube[3][0][1] = cube[5][0].copy()[1]
        new_cube[3][0][0] = cube[5][0].copy()[0]
        # rotate back face counterclockwise: 
        # cube[0][0][0] -> cube[0][0][1] -> cube[0][1][1] -> cube[0][1][0] -> cube[0][0][0]
        new_cube[0][0][1] = cube[0][0].copy()[0]
        new_cube[0][1][1] = cube[0][0].copy()[1]
        new_cube[0][1][0] = cube[0][1].copy()[1]
        new_cube[0][0][0] = cube[0][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

    # This function takes in the size of the cube and returns a randomized yet plausible matrix representation of a cube
    def randomize_cube(size):
        cube = cube_setup.solved_cube(size)
        x = random.randrange(101) # ~ 0-100
        print('\n# of random operations = ', x, '\n')
        for i in range(x):
            operation_flag = random.randrange(12)
            if operation_flag == 0:
                temp = cube_setup.top_row_left(cube,size)
                cube = temp[0]
            elif operation_flag == 1:
                temp = cube_setup.top_row_right(cube,size)
                cube = temp[0]
            elif operation_flag == 2:
                temp = cube_setup.bottom_row_left(cube,size)
                cube = temp[0]
            elif operation_flag == 3:
                temp = cube_setup.bottom_row_right(cube,size)
                cube = temp[0]
            elif operation_flag == 4:
                temp = cube_setup.left_col_down(cube,size)
                cube = temp[0]
            elif operation_flag == 5:
                temp = cube_setup.left_col_up(cube,size)
                cube = temp[0]
            elif operation_flag == 6:
                temp = cube_setup.right_col_down(cube,size)
                cube = temp[0]
            elif operation_flag == 7:
                temp = cube_setup.right_col_up(cube,size)
                cube = temp[0]
            elif operation_flag == 8:
                temp = cube_setup.front_face_clockwise(cube,size)
                cube = temp[0]
            elif operation_flag == 9:
                temp = cube_setup.front_face_counterclockwise(cube,size)
                cube = temp[0]
            elif operation_flag == 10:
                temp = cube_setup.back_face_clockwise(cube,size)
                cube = temp[0]
            elif operation_flag == 11:
                temp = cube_setup.back_face_counterclockwise(cube,size)
                cube = temp[0]
        return cube

# SEARCH FUNCTIONS
class search_funcs:
    def dfs(size, cube):
        moves = 0
        state_list = [cube]
        cube, moves, state_list = search_funcs.dfs_loop(size, cube, state_list, moves)
        return (cube, moves)

    def dfs_loop(size, cube, state_list, moves):
        print('# of moves = ', moves)
        print('state_list len = ', len(state_list))
        solved = cube_setup.solved_cube(size)
        moves_list = [  cube_setup.top_row_left, cube_setup.top_row_right, 
                        cube_setup.bottom_row_left, cube_setup.bottom_row_right, 
                        cube_setup.left_col_down, cube_setup.left_col_up, 
                        cube_setup.right_col_down, cube_setup.right_col_up, 
                        cube_setup.front_face_clockwise, cube_setup.front_face_counterclockwise, 
                        cube_setup.back_face_clockwise, cube_setup.back_face_counterclockwise ]
        if cube != solved:
            for move in moves_list:
                new_cube = move(cube, size)[0]
                if new_cube not in state_list:
                    state_list.append(new_cube)
                    moves += 1
                    result = search_funcs.dfs_loop(size, new_cube, state_list, moves)
                    if result:
                        return result
                    moves -= 1
                    state_list.pop()
        else:
            return (cube, moves, state_list)

    def bfs(size, cube):
        count = 0
        solved = cube_setup.solved_cube(size)
        moves = 0
        state_list = [cube]
        queue = [(cube, moves, state_list)]
        while queue:
            cube, moves, state_list = queue.pop(0)
            print('# of moves = ', moves)
            print('state_list len = ', len(state_list))
            moves_list = [  cube_setup.top_row_left, cube_setup.top_row_right, 
                            cube_setup.bottom_row_left, cube_setup.bottom_row_right, 
                            cube_setup.left_col_down, cube_setup.left_col_up, 
                            cube_setup.right_col_down, cube_setup.right_col_up, 
                            cube_setup.front_face_clockwise,cube_setup.front_face_counterclockwise, 
                            cube_setup.back_face_clockwise, cube_setup.back_face_counterclockwise ]
            if cube == solved:
                return (cube, moves)
            for move in moves_list:
                new_cube = move(cube, size)[0]
                if new_cube not in state_list:
                    new_state_list = state_list + [new_cube]
                    queue.append((new_cube, moves + 1, new_state_list))
        return "BFS - COULD NOT SOLVE"