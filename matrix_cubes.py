import random

class helper:
    # Visualize cube more accurately 
    # (front, back, left, right, top, bottom)
    def print_cube(matrix):
        for i in matrix:
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
        matrix = helper.solved_cube(size)
        # random.seed(0)
        x = random.randrange(101) # ~ 0-100
        #print('\n# of random operations = ', x, '\n')
        for i in range(x):
            operation_flag = random.randrange(12)
            matrix = moves.get_operations(matrix)[operation_flag] #rub.operations[operation_flag]
        return matrix

    # This functions copies the cube matrix without dependancies
    # copy() works on lists but not nested lists
    def copy_cube(matrix):
        size = len(matrix[0][0])
        new_matrix = helper.solved_cube(size)
        for i in range(6):
            for ii in range(size):
                new_matrix[i][ii] = matrix[i][ii].copy()
        return new_matrix

class moves:
    def get_actions(matrix):
        actions =      { '000' : { 'trl' : matrix[3][1].copy()[0],
                                   'trr' : matrix[2][0].copy()[1],
                                   'lcd' : matrix[4][0].copy()[0],
                                   'lcu' : matrix[5][1].copy()[1],
                                   'ffcl': matrix[0][1].copy()[0],
                                   'ffcc': matrix[0][0].copy()[1]
                                 },
                         '001' : { 'trl' : matrix[3][0].copy()[0],
                                   'trr' : matrix[2][1].copy()[1],
                                   'rcd' : matrix[4][0].copy()[1],
                                   'rcu' : matrix[5][1].copy()[0],
                                   'ffcl': matrix[0][0].copy()[0],
                                   'ffcc': matrix[0][1].copy()[1]                                                
                                 },
                         '010' : { 'brl' : matrix[3][1].copy()[1],
                                   'brr' : matrix[2][0].copy()[0],
                                   'lcd' : matrix[4][1].copy()[0],
                                   'lcu' : matrix[5][0].copy()[1],
                                   'ffcl': matrix[0][1].copy()[1],
                                   'ffcc': matrix[0][0].copy()[0]
                                 },
                         '011' : { 'brl' : matrix[3][0].copy()[1],
                                   'brr' : matrix[2][1].copy()[0],
                                   'rcd' : matrix[4][1].copy()[1],
                                   'rcu' : matrix[5][0].copy()[0],
                                   'ffcl': matrix[0][0].copy()[1],
                                   'ffcc': matrix[0][1].copy()[0]                                                 
                                 },
                         '100' : { 'trl' : matrix[2][1].copy()[1],
                                   'trr' : matrix[3][0].copy()[0],
                                   'rcd' : matrix[5][1].copy()[0],
                                   'rcu' : matrix[4][0].copy()[1],
                                   'bfcl': matrix[1][0].copy()[1],
                                   'bfcc': matrix[1][1].copy()[0]
                                 },
                         '101' : { 'trl' : matrix[2][0].copy()[1],
                                   'trr' : matrix[3][1].copy()[0],
                                   'lcd' : matrix[5][1].copy()[1],
                                   'lcu' : matrix[4][0].copy()[0],
                                   'bfcl': matrix[1][1].copy()[1],
                                   'bfcc': matrix[1][0].copy()[0]
                                 },
                         '110' : { 'brl' : matrix[2][1].copy()[0],
                                   'brr' : matrix[3][0].copy()[1],
                                   'rcd' : matrix[5][0].copy()[0],
                                   'rcu' : matrix[4][1].copy()[1],
                                   'bfcl': matrix[1][0].copy()[0],
                                   'bfcc': matrix[1][1].copy()[1]
                                 },
                         '111' : { 'brl' : matrix[2][0].copy()[0],
                                   'brr' : matrix[3][1].copy()[1],
                                   'lcd' : matrix[5][0].copy()[1],
                                   'lcu' : matrix[4][1].copy()[0],
                                   'bfcl': matrix[1][1].copy()[0],
                                   'bfcc': matrix[1][0].copy()[1]
                                 },
                         '200' : { 'brl' : matrix[0][1].copy()[0],
                                   'brr' : matrix[1][1].copy()[1],
                                   'lcd' : matrix[2][1].copy()[0],
                                   'lcu' : matrix[2][0].copy()[1],
                                   'bfcl': matrix[5][0].copy()[0],
                                   'bfcc': matrix[4][0].copy()[0]
                                 },
                         '201' : { 'trl' : matrix[0][0].copy()[0],
                                   'trr' : matrix[1][0].copy()[1],
                                   'lcd' : matrix[2][0].copy()[0],
                                   'lcu' : matrix[2][1].copy()[1],
                                   'bfcl': matrix[5][0].copy()[1],
                                   'bfcc': matrix[4][0].copy()[1]
                                 },
                         '210' : { 'brl' : matrix[0][1].copy()[1],
                                   'brr' : matrix[1][1].copy()[0],
                                   'lcd' : matrix[2][1].copy()[1],
                                   'lcu' : matrix[2][0].copy()[0],
                                   'ffcl': matrix[5][1].copy()[0],
                                   'ffcc': matrix[4][1].copy()[0]
                                 },
                         '211' : { 'trl' : matrix[0][0].copy()[1],
                                   'trr' : matrix[1][0].copy()[0],
                                   'lcd' : matrix[2][0].copy()[1],
                                   'lcu' : matrix[2][1].copy()[0],
                                   'ffcl': matrix[5][1].copy()[1],
                                   'ffcc': matrix[4][1].copy()[1]
                                 },
                         '300' : { 'trl' : matrix[1][0].copy()[0],
                                   'trr' : matrix[0][0].copy()[1],
                                   'rcd' : matrix[3][0].copy()[1],
                                   'rcu' : matrix[3][1].copy()[0],
                                   'bfcl': matrix[4][0].copy()[0],
                                   'bfcc': matrix[5][0].copy()[0]
                                 },
                         '301' : { 'brl' : matrix[1][1].copy()[0],
                                   'brr' : matrix[0][1].copy()[1],
                                   'rcd' : matrix[3][1].copy()[1],
                                   'rcu' : matrix[3][0].copy()[0],
                                   'bfcl': matrix[4][0].copy()[1],
                                   'bfcc': matrix[5][0].copy()[1]
                                 },
                         '310' : { 'trl' : matrix[1][0].copy()[1],
                                   'trr' : matrix[0][0].copy()[0],
                                   'rcd' : matrix[3][0].copy()[0],
                                   'rcu' : matrix[3][1].copy()[1],
                                   'ffcl': matrix[4][1].copy()[0],
                                   'ffcc': matrix[5][1].copy()[0]
                                 },
                         '311' : { 'brl' : matrix[1][1].copy()[1],
                                   'brr' : matrix[0][1].copy()[0],
                                   'rcd' : matrix[3][0].copy()[1],
                                   'rcu' : matrix[3][1].copy()[0],
                                   'ffcl': matrix[4][1].copy()[1],
                                   'ffcc': matrix[5][1].copy()[1]
                                 },
                         '400' : { 'trl' : matrix[4][1].copy()[0],
                                   'trr' : matrix[4][0].copy()[1],
                                   'lcd' : matrix[1][0].copy()[1],
                                   'lcu' : matrix[0][0].copy()[0],
                                   'bfcl': matrix[2][0].copy()[0],
                                   'bfcc': matrix[3][0].copy()[0]
                                 },
                         '401' : { 'trl' : matrix[4][0].copy()[0],
                                   'trr' : matrix[4][0].copy()[1],
                                   'rcd' : matrix[1][0].copy()[0],
                                   'rcu' : matrix[0][0].copy()[1],
                                   'bfcl': matrix[2][0].copy()[1],
                                   'bfcc': matrix[3][0].copy()[1]
                                 },
                         '410' : { 'trl' : matrix[4][1].copy()[1],
                                   'trr' : matrix[4][0].copy()[0],
                                   'lcd' : matrix[1][1].copy()[1],
                                   'lcu' : matrix[0][1].copy()[0],
                                   'ffcl': matrix[2][1].copy()[0],
                                   'ffcc': matrix[3][1].copy()[0]
                                 },
                         '411' : { 'trl' : matrix[4][0].copy()[1],
                                   'trr' : matrix[4][1].copy()[0],
                                   'rcd' : matrix[1][1].copy()[0],
                                   'rcu' : matrix[0][1].copy()[1],
                                   'ffcl': matrix[2][1].copy()[1],
                                   'ffcc': matrix[3][1].copy()[1]
                                 },
                         '500' : { 'brl' : matrix[5][0].copy()[1],
                                   'brr' : matrix[5][1].copy()[0],
                                   'rcd' : matrix[0][1].copy()[1],
                                   'rcu' : matrix[1][1].copy()[0],
                                   'bfcl': matrix[3][0].copy()[0],
                                   'bfcc': matrix[2][0].copy()[0]
                                 },
                         '501' : { 'brl' : matrix[5][1].copy()[1],
                                   'brr' : matrix[5][0].copy()[0],
                                   'lcd' : matrix[0][1].copy()[0],
                                   'lcu' : matrix[1][1].copy()[1],
                                   'bfcl': matrix[3][0].copy()[1],
                                   'bfcc': matrix[2][0].copy()[1]
                                 },
                         '510' : { 'brl' : matrix[5][0].copy()[0],
                                   'brr' : matrix[5][1].copy()[1],
                                   'rcd' : matrix[0][0].copy()[1],
                                   'rcu' : matrix[1][0].copy()[0],
                                   'ffcl': matrix[3][1].copy()[0],
                                   'ffcc': matrix[2][1].copy()[0]
                                 },
                         '511' : { 'brl' : matrix[5][1].copy()[0],
                                   'brr' : matrix[5][1].copy()[1],
                                   'lcd' : matrix[0][0].copy()[0],
                                   'lcu' : matrix[1][0].copy()[1],
                                   'ffcl': matrix[3][1].copy()[1],
                                   'ffcc': matrix[2][1].copy()[1]
                                 }}
        return actions
    
    # TopRowLeft
    def trl(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'trl'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # TopRowRight
    def trr(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'trr'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # BottomRowLeft
    def brl(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'brl'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # BottomRowRight
    def brr(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'brr'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # LeftColumnDown
    def lcd(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'lcd'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # LeftColumnUp
    def lcu(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'lcu'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # RightColumnDown
    def rcd(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'rcd'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # RightColumnUp
    def rcu(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'rcu'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # FrontFaceCLockwise
    def ffcl(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'ffcl'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)

    # FrontFaceCounterClockwise
    def ffcc(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'ffcc'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)
    
    # BackFaceCLockwise
    def bfcl(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'bfcl'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)
    
    # BackFaceCounterClockwise
    def bfcc(matrix):
        size = len(matrix[0][0])
        actions = moves.get_actions(matrix)
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
        new_matrix = helper.copy_cube(matrix)
        act = 'bfcc'
        for i in range(6):
            for ii in range(size):
                for iii in range(size):
                    str_i = str(i)+str(ii)+str(iii)
                    if act in actions[str_i].keys():
                        new_matrix[i][ii][iii] = actions[str_i][act]
        return (new_matrix, matrix)
    
    def get_operations(matrix):
        operations = [ moves.trl(matrix)[0],
                       moves.trr(matrix)[0],
                       moves.brl(matrix)[0],
                       moves.brr(matrix)[0],
                       moves.lcd(matrix)[0],
                       moves.lcu(matrix)[0],
                       moves.rcd(matrix)[0],
                       moves.rcu(matrix)[0],
                       moves.ffcl(matrix)[0],
                       moves.ffcc(matrix)[0],
                       moves.bfcc(matrix)[0],
                       moves.bfcl(matrix)[0] ]
        return operations
    
class tests:
    def asserts():
        matrix = helper.solved_cube(2)
        assert moves.trl(matrix)[0]  == [[['b', 'b'], ['y', 'y']],
                                         [['g', 'g'], ['w', 'w']],
                                         [['g', 'y'], ['g', 'y']],
                                         [['w', 'b'], ['w', 'b']],
                                         [['r', 'r'], ['r', 'r']],
                                         [['o', 'o'], ['o', 'o']]]
        assert moves.trr(matrix)[0]  == [[['g', 'g'], ['y', 'y']],
                                         [['b', 'b'], ['w', 'w']],
                                         [['g', 'w'], ['g', 'w']],
                                         [['y', 'b'], ['y', 'b']],
                                         [['r', 'r'], ['r', 'r']],
                                         [['o', 'o'], ['o', 'o']]]

        assert moves.brl(matrix)[0]  == [[['y', 'y'], ['b', 'b']],  # Front
                                         [['w', 'w'], ['g', 'g']],  # Back
                                         [['y', 'g'], ['y', 'g']],  # Left
                                         [['b', 'w'], ['b', 'w']],  # Right
                                         [['r', 'r'], ['r', 'r']],  # Top
                                         [['o', 'o'], ['o', 'o']]]  # Bottom

        assert moves.brr(matrix)[0]  == [[['y', 'y'], ['g', 'g']],  # Front
                                         [['w', 'w'], ['b', 'b']],  # Back
                                         [['w', 'g'], ['w', 'g']],  # Left
                                         [['b', 'y'], ['b', 'y']],  # Right
                                         [['r', 'r'], ['r', 'r']],  # Top
                                         [['o', 'o'], ['o', 'o']]]  # Bottom

        assert moves.lcd(matrix)[0]  == [[['r', 'y'], ['r', 'y']],  # Front
                                         [['w', 'o'], ['w', 'o']],  # Back
                                         [['g', 'g'], ['g', 'g']],  # Left
                                         [['b', 'b'], ['b', 'b']],  # Right
                                         [['w', 'r'], ['w', 'r']],  # Top
                                         [['o', 'y'], ['o', 'y']]]  # Bottom

        assert moves.lcu(matrix)[0]  == [[['o', 'y'], ['o', 'y']],  # Front
                                         [['w', 'r'], ['w', 'r']],  # Back
                                         [['g', 'g'], ['g', 'g']],  # Left
                                         [['b', 'b'], ['b', 'b']],  # Right
                                         [['y', 'r'], ['y', 'r']],  # Top
                                         [['o', 'w'], ['o', 'w']]]  # Bottom
 
        assert moves.rcd(matrix)[0][0] == [['y', 'r'], ['y', 'r']]  # Front
        assert moves.rcd(matrix)[0][1] == [['o', 'w'], ['o', 'w']]  # Back
        assert moves.rcd(matrix)[0][2] == [['g', 'g'], ['g', 'g']]  # Left
        assert moves.rcd(matrix)[0][3] == [['b', 'b'], ['b', 'b']]  # Right
        assert moves.rcd(matrix)[0][4] == [['r', 'w'], ['r', 'w']]  # Top
        assert moves.rcd(matrix)[0][5] == [['y', 'o'], ['y', 'o']]  # Bottom

        assert moves.rcu(matrix)[0]  == [[['y', 'o'], ['y', 'o']],  # Front
                                         [['r', 'w'], ['r', 'w']],  # Back
                                         [['g', 'g'], ['g', 'g']],  # Left
                                         [['b', 'b'], ['b', 'b']],  # Right
                                         [['r', 'y'], ['r', 'y']],  # Top
                                         [['w', 'o'], ['w', 'o']]]  # Bottom

        assert moves.ffcl(matrix)[0] == [[['y', 'y'], ['y', 'y']],  # Front
                                         [['w', 'w'], ['w', 'w']],  # Back
                                         [['g', 'g'], ['o', 'o']],  # Left
                                         [['b', 'b'], ['r', 'r']],  # Right
                                         [['r', 'r'], ['g', 'g']],  # Top
                                         [['o', 'o'], ['b', 'b']]]  # Bottom

        assert moves.ffcc(matrix)[0][0] == [['y', 'y'], ['y', 'y']]  # Front
        assert moves.ffcc(matrix)[0][1] == [['w', 'w'], ['w', 'w']]  # Back
        assert moves.ffcc(matrix)[0][2] == [['g', 'g'], ['r', 'r']]  # Left
        assert moves.ffcc(matrix)[0][3] == [['b', 'b'], ['o', 'o']]  # Right
        assert moves.ffcc(matrix)[0][4] == [['r', 'r'], ['b', 'b']]  # Top
        assert moves.ffcc(matrix)[0][5] == [['o', 'o'], ['g', 'g']]  # Bottom

        assert moves.bfcl(matrix)[0][0] == [['y', 'y'], ['y', 'y']]  # Front
        assert moves.bfcl(matrix)[0][1] == [['w', 'w'], ['w', 'w']]  # Back
        assert moves.bfcl(matrix)[0][2] == [['o', 'o'], ['g', 'g']]  # Left
        assert moves.bfcl(matrix)[0][3] == [['r', 'r'], ['b', 'b']]  # Right
        assert moves.bfcl(matrix)[0][4] == [['g', 'g'], ['r', 'r']]  # Top
        assert moves.bfcl(matrix)[0][5] == [['b', 'b'], ['o', 'o']]  # Bottom

        assert moves.bfcc(matrix)[0][0] == [['y', 'y'], ['y', 'y']]  # Front
        assert moves.bfcc(matrix)[0][1] == [['w', 'w'], ['w', 'w']]  # Back
        assert moves.bfcc(matrix)[0][2] == [['r', 'r'], ['g', 'g']]  # Left
        assert moves.bfcc(matrix)[0][3] == [['o', 'o'], ['b', 'b']]  # Right
        assert moves.bfcc(matrix)[0][4] == [['b', 'b'], ['r', 'r']]  # Top
        assert moves.bfcc(matrix)[0][5] == [['g', 'g'], ['o', 'o']]  # Bottom
    

# SEARCH FUNCTIONS
class search_funcs:   
    def dfs(matrix):
        steps = 0
        state_list = [matrix]
        matrix, steps, state_list = search_funcs.dfs_loop(matrix, state_list, steps)
        return (matrix, steps)

    def dfs_loop(matrix, state_list, steps):
        #print('# of moves = ', steps)
        #print('state_list len = ', len(state_list))
        solved = helper.solved_cube(2)
        if matrix != solved:
            operations = moves.get_operations(matrix)
            for move in operations:
                new_matrix = move #cube.operations[move][0]
                #helper.print_cube(new_matrix)
                if new_matrix not in state_list:
                    state_list.append(new_matrix)
                    steps += 1
                    result = search_funcs.dfs_loop(new_matrix, state_list, steps)
                    if result[0] == solved:
                        return result
                    steps -= 1
                    state_list.pop()
        else:
            return (matrix, steps, state_list)

    def bfs(matrix):
        size = len(matrix[0][0])
        count = 0
        solved = helper.solved_cube(size)
        steps = 0
        state_list = [matrix]
        queue = [(matrix, steps, state_list)]
        while queue:
            matrix, steps, state_list = queue.pop(0)
            #print('# of moves = ', steps)
            #print('state_list len = ', len(state_list))
            if matrix == solved:
                return (matrix, steps)
            operations = moves.get_operations(matrix)
            #helper.print_cube(matrix)
            for move in operations:
                new_matrix = move
                if new_matrix not in state_list:
                    new_state_list = state_list + [new_matrix]
                    queue.append((new_matrix, steps + 1, new_state_list))
        return "BFS - COULD NOT SOLVE"