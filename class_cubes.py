import random

class helper:
    # Visualize cube more accurately 
    # (front, back, left, right, top, bottom)
    def print_cube(rub):
        for i in rub.cube:
            for ii in i:
                print(ii,'\n')
            print('\n')
        return None

    # This function returns a solved cube
    def solved_cube(size):
        if size == 2:
            matrix = [[['y', 'y'], ['y', 'y']],  # Front
                      [['w', 'w'], ['w', 'w']],  # Back
                      [['g', 'g'], ['g', 'g']],  # Left
                      [['b', 'b'], ['b', 'b']],  # Right
                      [['r', 'r'], ['r', 'r']],  # Top
                      [['o', 'o'], ['o', 'o']]]  # Bottom
        else:
            print("helper.solved_cube() only setup for size=2")
        """
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
        """
        return matrix
    
    # This function takes in the size of the cube 
    # and returns a randomized yet plausible matrix 
    # representation of a cube
    def randomize_cube(size):
        rub = helper.solved_cube(size)
        # random.seed(0)
        x = random.randrange(101) # ~ 0-100
        #print('\n# of random operations = ', x, '\n')
        for i in range(x):
            operation_flag = random.randrange(12)
            rub = rub.operations[operation_flag]
        return rub

    # This functions copies the cube matrix without dependancies
    # copy() works on lists but not nested lists
    def copy_cube(rub):
        new_matrix = helper.solved_cube(rub)
        for i in range(6):
            for ii in range(rub.size):
                new_matrix[i][ii] = rub.cube[i][ii].copy()
        return new_matrix

class moves:
    # TopRowLeft
    def trl(rub):
        """
        top rows: front- cube[0][0][0] & cube[0][0][1], back- cube[1][0][1] & cube[1][0][0], 
                  left- cube[2][0][1] & cube[2][1][1], right- cube[3][1][0] & cube[3][0][0]
        left <- front
        back <- left
        right <- back
        front <- right
        rotate top face clockwise: 
        cube[4][0][0] -> cube[4][0][1] -> cube[4][1][1] -> cube[4][1][0] -> cube[4][0][0]
        """
        new_matrix = helper.copy_cube(rub.size)
        act = 'trl'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_matrix[i][ii][iii] = rub.actions[str_i][act]
        return (cube2(new_matrix),rub)

    # TopRowRight
    def trr(rub):
        """
        top rows: front- cube[0][0][0] & cube[0][0][1], back- cube[1][0][1] & cube[1][0][0], 
                  left- cube[2][0][1] & cube[2][1][1], right- cube[3][1][0] & cube[3][0][0]
        front <- left
        right <- front
        back <- right
        left <- back
        rotate top face counterclockwise: 
        cube[4][0][0] <- cube[4][0][1] <- cube[4][1][1] <- cube[4][1][0] <- cube[4][0][0]
        """
        new_matrix = helper.copy_cube(rub)
        act = 'trr'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_matrix[i][ii][iii] = rub.actions[str_i][act]
        return (cube2(new_matrix),rub)

    # BottomRowLeft
    def brl(rub):
        """
        bottom rows: front- cube[0][1][0] & cube[0][1][1], back- cube[1][1][1] & cube[1][1][0], 
                     left- cube[2][0][0] & cube[2][1][0], right- cube[3][1][1] & cube[3][0][1]
        left <- front
        back <- left
        right <- back
        front <- right
        rotate bottom face counterclockwise: 
        cube[5][0][0] -> cube[5][1][0] -> cube[5][1][1] -> cube[5][0][1] -> cube[5][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'brl'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # BottomRowRight
    def brr(rub):
        """
        bottom rows: front- cube[0][1][0] & cube[0][1][1], back- cube[1][1][1] & cube[1][1][0], 
                     left- cube[2][0][0] & cube[2][1][0], right- cube[3][1][1] & cube[3][0][1]
        front <- left
        right <- front
        back <- right
        left <- back
        rotate bottom face clockwise: 
        cube[5][0][0] <- cube[5][1][0] <- cube[5][1][1] <- cube[5][0][1] <- cube[5][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'brr'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # LeftColumnDown
    def lcd(rub):
        """
        left cols: front- cube[0][0][0] & cube[0][1][0], back- cube[1][0][1] & cube[1][1][1], 
                   top- cube[4][0][0] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][0][1]
        bot <- front
        back <- bot
        top <- back
        front <- top
        rotate left face clockwise: 
        cube[2][0][0] <- cube[2][1][0] <- cube[2][1][1] <- cube[2][0][1] <- cube[2][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'lcd'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # LeftColumnUp
    def lcu(rub):
        """
        left cols: front- cube[0][0][0] & cube[0][1][0], back- cube[1][0][1] & cube[1][1][1], 
                   top- cube[4][0][0] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][0][1]
        front <- bot
        top <- front
        back <- top
        bot <- back
        rotate left face counterclockwise: 
        cube[2][0][0] -> cube[2][1][0] -> cube[2][1][1] -> cube[2][0][1] -> cube[2][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'lcu'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # RightColumnDown
    def rcd(rub):
        """
        right cols: front- cube[0][0][1] & cube[0][1][1], back- cube[1][0][0] & cube[1][1][0], 
                    top- cube[4][0][1] & cube[4][1][1], bottom- cube[5][1][0] & cube[5][0][0]
        bot <- front
        back <- bot
        top <- back
        front <- top
        rotate right face counterclockwise: 
        cube[3][0][0] -> cube[3][1][0] -> cube[3][1][1] -> cube[3][0][1] -> cube[3][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'rcd'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # RightColumnUp
    def rcu(rub):
        """
        right cols: front- cube[0][0][1] & cube[0][1][1], back- cube[1][0][0] & cube[1][1][0], 
                    top- cube[4][0][1] & cube[4][1][1], bottom- cube[5][1][0] & cube[5][0][0]
        front <- bot
        top <- front
        back <- top
        bot <- back
        rotate right face clockwise: 
        cube[3][0][0] <- cube[3][1][0] <- cube[3][1][1] <- cube[3][0][1] <- cube[3][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'rcu'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # FrontFaceCLockwise
    def ffcl(rub):
        """
        front face surrounding cols: left- cube[2][1][1] & cube[2][1][0], right- cube[3][1][1] & cube[3][1][0], 
                                     top- cube[4][1][1] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][1][0]
        right <- top
        bot <- right
        left <- bot
        top <- left
        rotate front face clockwise: 
        cube[0][0][0] <- cube[0][1][0] <- cube[0][1][1] <- cube[0][0][1] <- cube[0][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'ffcl'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

    # FrontFaceCounterClockwise
    def ffcc(rub):
        """
        front face surrounding cols: left- cube[2][1][1] & cube[2][1][0], right- cube[3][1][1] & cube[3][1][0], 
                                     top- cube[4][1][1] & cube[4][1][0], bottom- cube[5][1][1] & cube[5][1][0]
        top <- right
        left <- top
        bot <- left
        right <- bot
        rotate fron face counterclockwise: 
        cube[0][0][0] -> cube[0][1][0] -> cube[0][1][1] -> cube[0][0][1] -> cube[0][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'ffcc'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)
    
    # BackFaceCLockwise
    def bfcl(rub):
        """
        back face surrounding cols: left- cube[2][0][1] & cube[2][0][0], right- cube[3][0][1] & cube[3][0][0], 
                                    top- cube[4][0][1] & cube[4][0][0], bottom- cube[5][0][1] & cube[5][0][0]
        right <- top
        bot <- right
        left <- bot
        top <- left
        rotate back face clockwise: 
        cube[1][0][0] <- cube[1][0][1] <- cube[1][1][1] <- cube[1][1][0] <- cube[1][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'bfcl'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)
    
    # BackFaceCounterClockwise
    def bfcc(rub):
        """
        back face surrounding cols: left- cube[2][0][1] & cube[2][0][0], right- cube[3][0][1] & cube[3][0][0], 
                                    top- cube[4][0][1] & cube[4][0][0], bottom- cube[5][0][1] & cube[5][0][0]
        top <- right
        left <- top
        bot <- left
        right <- bot
        rotate back face counterclockwise: 
        cube[1][0][0] -> cube[1][0][1] -> cube[1][1][1] -> cube[1][1][0] -> cube[1][0][0]
        """
        new_rub = helper.copy_cube(rub)
        act = 'bfcc'
        for i in range(6):
            for ii in range(rub.size):
                for iii in range(rub.size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in rub.actions[str_i].keys():
                        new_rub[i][ii][iii] = rub.actions[str_i][act]
        return (new_rub,rub)

# SETUP FUNCTIONS
class cube2:
    def __init__(self,matrix):
        self.size = 2
        # if self==helper.solved_cube(self.size):
        #     self.solved = True
        # else:
        #     self.solved = False
        self.cube = matrix
        # read this as, 
        # if action==top-row-left: new_cube[0][0][0]=self.cube[3][1].copy()[0]
        self.actions = { '000' : { 'trl' : self.cube[3][1].copy()[0],
                                   'trr' : self.cube[2][0].copy()[1],
                                   'lcd' : self.cube[4][0].copy()[0],
                                   'lcu' : self.cube[5][1].copy()[1],
                                   'ffcl': self.cube[0][1].copy()[0],
                                   'ffcc': self.cube[0][0].copy()[1]
                                 },
                         '001' : { 'trl' : self.cube[3][0].copy()[0],
                                   'trr' : self.cube[2][1].copy()[1],
                                   'rcd' : self.cube[4][0].copy()[1],
                                   'rcu' : self.cube[5][1].copy()[0],
                                   'ffcl': self.cube[0][0].copy()[0],
                                   'ffcc': self.cube[0][1].copy()[1]                                                
                                 },
                         '010' : { 'brl' : self.cube[3][1].copy()[1],
                                   'brr' : self.cube[2][0].copy()[0],
                                   'lcd' : self.cube[4][1].copy()[0],
                                   'lcu' : self.cube[5][0].copy()[1],
                                   'ffcl': self.cube[0][1].copy()[1],
                                   'ffcc': self.cube[0][0].copy()[0]
                                 },
                         '011' : { 'brl' : self.cube[3][0].copy()[1],
                                   'brr' : self.cube[2][1].copy()[0],
                                   'rcd' : self.cube[4][1].copy()[1],
                                   'rcu' : self.cube[5][0].copy()[0],
                                   'ffcl': self.cube[0][0].copy()[1],
                                   'ffcc': self.cube[0][1].copy()[0]                                                 
                                 },
                         '100' : { 'trl' : self.cube[2][1].copy()[1],
                                   'trr' : self.cube[3][0].copy()[0],
                                   'rcd' : self.cube[5][1].copy()[0],
                                   'rcu' : self.cube[4][0].copy()[1],
                                   'bfcl': self.cube[1][0].copy()[1],
                                   'bfcc': self.cube[1][1].copy()[0]
                                 },
                         '101' : { 'trl' : self.cube[2][0].copy()[1],
                                   'trr' : self.cube[3][1].copy()[0],
                                   'lcd' : self.cube[5][1].copy()[1],
                                   'lcu' : self.cube[4][0].copy()[0],
                                   'bfcl': self.cube[1][1].copy()[1],
                                   'bfcc': self.cube[1][0].copy()[0]
                                 },
                         '110' : { 'brl' : self.cube[2][1].copy()[0],
                                   'brr' : self.cube[3][0].copy()[1],
                                   'rcd' : self.cube[5][0].copy()[0],
                                   'rcu' : self.cube[4][1].copy()[1],
                                   'bfcl': self.cube[1][0].copy()[0],
                                   'bfcc': self.cube[1][1].copy()[1]
                                 },
                         '111' : { 'brl' : self.cube[2][0].copy()[0],
                                   'brr' : self.cube[3][1].copy()[1],
                                   'lcd' : self.cube[5][0].copy()[1],
                                   'lcu' : self.cube[4][1].copy()[0],
                                   'bfcl': self.cube[1][1].copy()[0],
                                   'bfcc': self.cube[1][0].copy()[1]
                                 },
                         '200' : { 'brl' : self.cube[0][1].copy()[0],
                                   'brr' : self.cube[1][1].copy()[1],
                                   'lcd' : self.cube[2][1].copy()[0],
                                   'lcu' : self.cube[2][0].copy()[1],
                                   'bfcl': self.cube[5][0].copy()[0],
                                   'bfcc': self.cube[4][0].copy()[0]
                                 },
                         '201' : { 'trl' : self.cube[0][0].copy()[0],
                                   'trr' : self.cube[1][0].copy()[1],
                                   'lcd' : self.cube[2][0].copy()[0],
                                   'lcu' : self.cube[2][1].copy()[1],
                                   'bfcl': self.cube[5][0].copy()[1],
                                   'bfcc': self.cube[4][0].copy()[1]
                                 },
                         '210' : { 'brl' : self.cube[0][1].copy()[1],
                                   'brr' : self.cube[1][1].copy()[0],
                                   'lcd' : self.cube[2][1].copy()[1],
                                   'lcu' : self.cube[2][0].copy()[0],
                                   'ffcl': self.cube[5][1].copy()[0],
                                   'ffcc': self.cube[4][1].copy()[0]
                                 },
                         '211' : { 'trl': self.cube[0][0].copy()[1],
                                   'trr' : self.cube[1][0].copy()[0],
                                   'lcd' : self.cube[2][0].copy()[1],
                                   'lcu' : self.cube[2][1].copy()[0],
                                   'ffcl': self.cube[5][1].copy()[1],
                                   'ffcc': self.cube[4][1].copy()[1]
                                 },
                         '300' : { 'trl' : self.cube[1][0].copy()[0],
                                   'trr' : self.cube[0][0].copy()[1],
                                   'rcd' : self.cube[3][0].copy()[1],
                                   'rcu' : self.cube[3][1].copy()[0],
                                   'bfcl': self.cube[4][0].copy()[0],
                                   'bfcc': self.cube[5][0].copy()[0]
                                 },
                         '301' : { 'brl' : self.cube[1][1].copy()[0],
                                   'brr' : self.cube[0][1].copy()[1],
                                   'rcd' : self.cube[3][1].copy()[1],
                                   'rcu' : self.cube[3][0].copy()[0],
                                   'bfcl': self.cube[4][0].copy()[1],
                                   'bfcc': self.cube[5][0].copy()[1]
                                 },
                         '310' : { 'trl' : self.cube[1][0].copy()[1],
                                   'trr' : self.cube[0][0].copy()[0],
                                   'rcd' : self.cube[3][0].copy()[0],
                                   'rcu' : self.cube[3][1].copy()[1],
                                   'ffcl': self.cube[4][1].copy()[0],
                                   'ffcc': self.cube[5][1].copy()[0]
                                 },
                         '311' : { 'brl' : self.cube[1][1].copy()[1],
                                   'brr' : self.cube[0][1].copy()[0],
                                   'rcd' : self.cube[3][0].copy()[1],
                                   'rcu' : self.cube[3][1].copy()[0],
                                   'ffcl': self.cube[4][1].copy()[1],
                                   'ffcc': self.cube[5][1].copy()[1]
                                 },
                         '400' : { 'trl' : self.cube[4][1].copy()[0],
                                   'trr' : self.cube[4][0].copy()[1],
                                   'lcd' : self.cube[1][0].copy()[1],
                                   'lcu' : self.cube[0][0].copy()[0],
                                   'bfcl': self.cube[2][0].copy()[0],
                                   'bfcc': self.cube[3][0].copy()[0]
                                 },
                         '401' : { 'trl' : self.cube[4][0].copy()[0],
                                   'trr' : self.cube[4][0].copy()[1],
                                   'rcd' : self.cube[1][0].copy()[0],
                                   'rcu' : self.cube[0][0].copy()[1],
                                   'bfcl': self.cube[2][0].copy()[1],
                                   'bfcc': self.cube[3][0].copy()[1]
                                 },
                         '410' : { 'trl' : self.cube[4][1].copy()[1],
                                   'trr' : self.cube[4][0].copy()[0],
                                   'lcd' : self.cube[1][1].copy()[1],
                                   'lcu' : self.cube[0][1].copy()[0],
                                   'ffcl': self.cube[2][1].copy()[0],
                                   'ffcc': self.cube[3][1].copy()[0]
                                 },
                         '411' : { 'trl' : self.cube[4][0].copy()[1],
                                   'trr' : self.cube[4][1].copy()[0],
                                   'rcd' : self.cube[1][1].copy()[0],
                                   'rcu' : self.cube[0][1].copy()[1],
                                   'ffcl': self.cube[2][1].copy()[1],
                                   'ffcc': self.cube[3][1].copy()[1]
                                 },
                         '500' : { 'brl' : self.cube[5][0].copy()[1],
                                   'brr' : self.cube[5][1].copy()[0],
                                   'rcd' : self.cube[0][1].copy()[1],
                                   'rcu' : self.cube[1][1].copy()[0],
                                   'bfcl': self.cube[3][0].copy()[0],
                                   'bfcc': self.cube[2][0].copy()[0]
                                 },
                         '501' : { 'brl' : self.cube[5][1].copy()[1],
                                   'brr' : self.cube[5][0].copy()[0],
                                   'lcd' : self.cube[0][1].copy()[0],
                                   'lcu' : self.cube[1][1].copy()[1],
                                   'bfcl': self.cube[3][0].copy()[1],
                                   'bfcc': self.cube[2][0].copy()[1]
                                 },
                         '510' : { 'brl' : self.cube[5][0].copy()[0],
                                   'brr' : self.cube[5][1].copy()[1],
                                   'rcd' : self.cube[0][0].copy()[1],
                                   'rcu' : self.cube[1][0].copy()[0],
                                   'ffcl': self.cube[3][1].copy()[0],
                                   'ffcc': self.cube[2][1].copy()[0]
                                 },
                         '511' : { 'brl' : self.cube[5][1].copy()[0],
                                   'brr' : self.cube[5][1].copy()[1],
                                   'lcd' : self.cube[0][0].copy()[0],
                                   'lcu' : self.cube[1][0].copy()[1],
                                   'ffcl': self.cube[3][1].copy()[1],
                                   'ffcc': self.cube[2][1].copy()[1]
                                 }
           }
        self.operations= {    0: moves.trl(self)[0],
                              1: moves.trr(self)[0],
                              2: moves.brl(self)[0],
                              3: moves.brr(self)[0],
                              4: moves.lcd(self)[0],
                              5: moves.lcu(self)[0],
                              6: moves.rcd(self)[0],
                              7: moves.rcu(self)[0],
                              8: moves.ffcl(self)[0],
                              9: moves.ffcc(self)[0],
                              10: moves.bfcc(self)[0],
                              11: moves.bfcl(self)[0]
                         }
        self.ff  = self.cube[0]
        self.baf = self.cube[1]
        self.rf  = self.cube[3]
        self.lf  = self.cube[2]
        self.tf  = self.cube[4]
        self.bof = self.cube[5]
    
class tests:
    def asserts(cube):
        #assert cube.size == 2
        #assert cube.solved == sol
        assert moves.trl(cube)[0]  == [[['b', 'b'], ['y', 'y']],
                                       [['g', 'g'], ['w', 'w']],
                                       [['g', 'y'], ['g', 'y']],
                                       [['w', 'b'], ['w', 'b']],
                                       [['r', 'r'], ['r', 'r']],
                                       [['o', 'o'], ['o', 'o']]]
        assert moves.trr(cube)[0]  == [[['g', 'g'], ['y', 'y']],
                                       [['b', 'b'], ['w', 'w']],
                                       [['g', 'w'], ['g', 'w']],
                                       [['y', 'b'], ['y', 'b']],
                                       [['r', 'r'], ['r', 'r']],
                                       [['o', 'o'], ['o', 'o']]]

        assert moves.brl(cube)[0]  == [[['y', 'y'], ['b', 'b']],  # Front
                                       [['w', 'w'], ['g', 'g']],  # Back
                                       [['y', 'g'], ['y', 'g']],  # Left
                                       [['b', 'w'], ['b', 'w']],  # Right
                                       [['r', 'r'], ['r', 'r']],  # Top
                                       [['o', 'o'], ['o', 'o']]]  # Bottom

        assert moves.brr(cube)[0]  == [[['y', 'y'], ['g', 'g']],  # Front
                                       [['w', 'w'], ['b', 'b']],  # Back
                                       [['w', 'g'], ['w', 'g']],  # Left
                                       [['b', 'y'], ['b', 'y']],  # Right
                                       [['r', 'r'], ['r', 'r']],  # Top
                                       [['o', 'o'], ['o', 'o']]]  # Bottom

        assert moves.lcd(cube)[0]  == [[['r', 'y'], ['r', 'y']],  # Front
                                       [['w', 'o'], ['w', 'o']],  # Back
                                       [['g', 'g'], ['g', 'g']],  # Left
                                       [['b', 'b'], ['b', 'b']],  # Right
                                       [['w', 'r'], ['w', 'r']],  # Top
                                       [['o', 'y'], ['o', 'y']]]  # Bottom

        assert moves.lcu(cube)[0]  == [[['o', 'y'], ['o', 'y']],  # Front
                                       [['w', 'r'], ['w', 'r']],  # Back
                                       [['g', 'g'], ['g', 'g']],  # Left
                                       [['b', 'b'], ['b', 'b']],  # Right
                                       [['y', 'r'], ['y', 'r']],  # Top
                                       [['o', 'w'], ['o', 'w']]]  # Bottom

        assert moves.rcd(cube)[0][0] == [['y', 'r'], ['y', 'r']]  # Front
        assert moves.rcd(cube)[0][1] == [['o', 'w'], ['o', 'w']]  # Back
        assert moves.rcd(cube)[0][2] == [['g', 'g'], ['g', 'g']]  # Left
        assert moves.rcd(cube)[0][3] == [['b', 'b'], ['b', 'b']]  # Right
        assert moves.rcd(cube)[0][4] == [['r', 'w'], ['r', 'w']]  # Top
        assert moves.rcd(cube)[0][5] == [['y', 'o'], ['y', 'o']]  # Bottom

        assert moves.rcu(cube)[0]  == [[['y', 'o'], ['y', 'o']],  # Front
                                       [['r', 'w'], ['r', 'w']],  # Back
                                       [['g', 'g'], ['g', 'g']],  # Left
                                       [['b', 'b'], ['b', 'b']],  # Right
                                       [['r', 'y'], ['r', 'y']],  # Top
                                       [['w', 'o'], ['w', 'o']]]  # Bottom

        assert moves.ffcl(cube)[0] == [[['y', 'y'], ['y', 'y']],  # Front
                                       [['w', 'w'], ['w', 'w']],  # Back
                                       [['g', 'g'], ['o', 'o']],  # Left
                                       [['b', 'b'], ['r', 'r']],  # Right
                                       [['r', 'r'], ['g', 'g']],  # Top
                                       [['o', 'o'], ['b', 'b']]]  # Bottom

        assert moves.ffcc(cube)[0][0] == [['y', 'y'], ['y', 'y']]  # Front
        assert moves.ffcc(cube)[0][1] == [['w', 'w'], ['w', 'w']]  # Back
        assert moves.ffcc(cube)[0][2] == [['g', 'g'], ['r', 'r']]  # Left
        assert moves.ffcc(cube)[0][3] == [['b', 'b'], ['o', 'o']]  # Right
        assert moves.ffcc(cube)[0][4] == [['r', 'r'], ['b', 'b']]  # Top
        assert moves.ffcc(cube)[0][5] == [['o', 'o'], ['g', 'g']]  # Bottom

        assert moves.bfcl(cube)[0][0] == [['y', 'y'], ['y', 'y']]  # Front
        assert moves.bfcl(cube)[0][1] == [['w', 'w'], ['w', 'w']]  # Back
        assert moves.bfcl(cube)[0][2] == [['o', 'o'], ['g', 'g']]  # Left
        assert moves.bfcl(cube)[0][3] == [['r', 'r'], ['b', 'b']]  # Right
        assert moves.bfcl(cube)[0][4] == [['g', 'g'], ['r', 'r']]  # Top
        assert moves.bfcl(cube)[0][5] == [['b', 'b'], ['o', 'o']]  # Bottom

        assert moves.bfcc(cube)[0][0] == [['y', 'y'], ['y', 'y']]  # Front
        assert moves.bfcc(cube)[0][1] == [['w', 'w'], ['w', 'w']]  # Back
        assert moves.bfcc(cube)[0][2] == [['r', 'r'], ['g', 'g']]  # Left
        assert moves.bfcc(cube)[0][3] == [['o', 'o'], ['b', 'b']]  # Right
        assert moves.bfcc(cube)[0][4] == [['b', 'b'], ['r', 'r']]  # Top
        assert moves.bfcc(cube)[0][5] == [['g', 'g'], ['o', 'o']]  # Bottom
    

# SEARCH FUNCTIONS
class search_funcs:
    def dfs(cube):
        moves = 0
        state_list = [cube]
        cube, moves, state_list = search_funcs.dfs_loop(cube, state_list, moves)
        return (cube, moves)

    def dfs_loop(cube, state_list, moves):
        print('# of moves = ', moves)
        print('state_list len = ', len(state_list))
        solved = cube.solved_cube()
        if cube != solved:
            for move in cube.operations.keys():
                new_cube = cube.operations[move][0]
                if new_cube not in state_list:
                    state_list.append(new_cube)
                    moves += 1
                    result = search_funcs.dfs_loop(new_cube, state_list, moves)
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