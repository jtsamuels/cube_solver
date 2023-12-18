import random

# SETUP FUNCTIONS
class cube2(solved=True):
    def __init__():
        self.size = 2
        self.solved = solved
        self.cube = self.solved_cube()
        if self.solved == False:
            self.cube = self.randomize_cube()
        self.ff  = self.cube[0]
        self.baf = self.cube[1]
        self.rf  = self.cube[3]
        self.lf  = self.cube[2]
        self.tf  = self.cube[4]
        self.bof = self.cube[5]
        self.operations= {    0: self.trl(self.cube)[0],
                              1: self.trr(self.cube)[0],
                              2: self.brl(self.cube)[0],
                              3: self.brr(self.cube)[0],
                              4: self.lcd(self.cube)[0],
                              5: self.lcu(self.cube)[0],
                              6: self.rcd(self.cube)[0],
                              7: self.rcu(self.cube)[0],
                              8: self.ffcl(self.cube)[0],
                              9: self.ffcc(self.cube)[0],
                              10: self.bfcc(self.cube)[0],
                              11: self.bfcl(self.cube)[0]
                         }
        # read this as, 
        # if action==top-row-left: new_cube[0][0][0]=self.cube[3][1].copy()[0]
        self.actions = { new_cube[0][0][0] : { trl : self.cube[3][1].copy()[0],
                                               trr : self.cube[2][0].copy()[1],
                                               lcd : self.cube[4][0].copy()[0],
                                               lcu : self.cube[5][1].copy()[1],
                                               ffcl: self.cube[0][1].copy()[0],
                                               ffcc: self.cube[0][0].copy()[1],
                                             },
                         new_cube[0][0][1] : { trl : self.cube[3][0].copy()[0],
                                               trr : self.cube[2][1].copy()[1],
                                               rcd : self.cube[4][0].copy()[1],
                                               rcu : self.cube[5][1].copy()[0],
                                               ffcl: self.cube[0][0].copy()[0],
                                               ffcc: self.cube[0][1].copy()[1],                                                 
                                             },
                         new_cube[0][1][0] : { brl :
                                               brr :
                                               lcd :
                                               lcu :
                                               ffcl:
                                               ffcc:
                                             },
                         new_cube[0][1][1] : { trl : ,
                                               trr : ,
                                               rcd : ,
                                               rcu : ,
                                               ffcl: ,
                                               ffcc: ,                                                 
                                             },
             new_cube[1][0][0] : {},
             new_cube[1][0][1] : {},
             new_cube[1][1][0] : {},
             new_cube[1][1][1] : {},
            
             new_cube[2][0][0] : {},
             new_cube[2][0][1] : {},
             new_cube[2][1][0] : {},
             new_cube[2][1][1] : {},
            
             new_cube[3][0][0] : {},
             new_cube[3][0][1] : {},
             new_cube[3][1][0] : {},
             new_cube[3][1][1] : {},
            
             new_cube[4][0][0] : {},
             new_cube[4][0][1] : {},
             new_cube[4][1][0] : {},
             new_cube[4][1][1] : {},
            
             new_cube[5][0][0] : {},
             new_cube[5][0][1] : {},
             new_cube[5][1][0] : {},
             new_cube[5][1][1] : {}
           }
    
    # Visualize cube more accurately 
    # (front, back, left, right, top, bottom)
    def print_cube(self):
        for i in self.cube():
            for ii in i:
                print(ii,'\n')
            print('\n')
        return None

    # This function returns a solved cube
    def solved_cube(self):
        y_insert = ['y'] * self.size
        w_insert = ['w'] * self.size
        g_insert = ['g'] * self.size
        b_insert = ['b'] * self.size
        r_insert = ['r'] * self.size
        o_insert = ['o'] * self.size
        matrix = [[],[],[],[],[],[]]
        for ii in range(self.size):
            matrix[0].append(y_insert)
            matrix[1].append(w_insert)
            matrix[2].append(g_insert)
            matrix[3].append(b_insert)
            matrix[4].append(r_insert)
            matrix[5].append(o_insert)
        return matrix
    
    # This function takes in the size of the cube 
    # and returns a randomized yet plausible matrix 
    # representation of a cube
    def randomize_cube(self):
        # random.seed(0)
        x = random.randrange(101) # ~ 0-100
        #print('\n# of random operations = ', x, '\n')
        for i in range(x):
            operation_flag = random.randrange(12)
            self.cube = self.operations[operation_flag]
        return cube

    # This functions copies the cube matrix without dependancies
    # copy() works on lists but not nested lists
    def copy_cube(self):
        new_cube = self.solved_cube()
        for i in range(6):
            for ii in range(self.size):
                new_cube[i][ii] = self.cube[i][ii].copy()
        return new_cube
                                   
    
    # TOP ROW
    def top_row_left(self):
        new_cube = self.copy_cube()
        # JUST FOR 2X2 CUBE FOR NOW
        # top rows: front- cube[0][0][0] & cube[0][0][1], back- cube[1][0][1] & cube[1][0][0], 
        #           left- cube[2][0][1] & cube[2][1][1], right- cube[3][1][0] & cube[3][0][0]
        #           left <- front
        new_cube[2][0][1] = self.cube[0][0].copy()[0]
        new_cube[2][1][1] = self.cube[0][0].copy()[1]
        #           back <- left
        new_cube[1][0][1] = self.cube[2][0].copy()[1]
        new_cube[1][0][0] = self.cube[2][1].copy()[1]
        #          right <- back
        new_cube[3][1][0] = self.cube[1][0].copy()[1]
        new_cube[3][0][0] = self.cube[1][0].copy()[0]
        #          front <- right
        new_cube[0][0][0] = self.cube[3][1].copy()[0]
        new_cube[0][0][1] = self.cube[3][0].copy()[0]
        # rotate top face clockwise: 
        # cube[4][0][0] -> cube[4][0][1] -> cube[4][1][1] -> cube[4][1][0] -> cube[4][0][0]
        new_cube[4][0][1] = self.cube[4][0].copy()[0]
        new_cube[4][1][1] = self.cube[4][0].copy()[1]
        new_cube[4][1][0] = self.cube[4][1].copy()[1]
        new_cube[4][0][0] = self.cube[4][1].copy()[0]
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
        # cube[1][0][0] -> cube[1][0][1] -> cube[1][1][1] -> cube[1][1][0] -> cube[1][0][0]
        new_cube[1][0][1] = cube[0][0].copy()[0]
        new_cube[1][1][1] = cube[0][0].copy()[1]
        new_cube[1][1][0] = cube[0][1].copy()[1]
        new_cube[1][0][0] = cube[0][1].copy()[0]
        # now pass on the new cube and the appended list of reached states
        return (new_cube,cube)

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