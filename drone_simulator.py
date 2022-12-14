import numpy as np
import matplotlib.pyplot as plt

guessed_days = {1: [(1,1), (1,2), (1,3), (1,4), (1,5), (12,12), (16,20), (17,20), (18,20), (19,20), (20,20)], 
                2: [(2,1), (2,2), (2,3), (2,4), (2,5)], 
                3:[], 
                4:[(19,1), (19,2), (19,3), (19,4), (19,5), (19,16), (19,17), (19,18), (19,19), (19,20)], 
                5:[(6,17), (2,1), (2,2), (2,3), (8,5)], # (6,17) 
                6:[(8,2), (8,6), (12,6), (8,8), (8,14)], 
                7:[(8,11), (8,7), (6,9), (6,11), (8,9), (8,13), (8, 19), (15,7), (15,11), (15,19), (19,7), (19,11), (8,15), (11,7), (15,5)],
                8:[(1,12), (9,12), (13,12), (1,8), (1,16), (1,18), (1,20), (5,12), (9,8), (17,12)],
                9:[(15,10), (15,14), (15,18), (3,14), (7,10), (7,14), (3,18), (7,14), (8,14), (11,14)],
                10:[(1,2), (2,4), (12,5), (12,15), (8,9), (8,19), (12,9), (12,19), (16,9)], #(2,4)
                11:[(17,9), (17,19), (1,7), (1,9), (1,17), (1,19), (5,7), (5,17), (9,7), (9,17), (17,7), (17,17), (5,1), (5,3), (5,5), (5,9), (5,11), (5,13), (5,15), (5,19)],
                12:[(17,9), (19,3), (17,1), (17,2), (17,3), (17,5), (17,7)],
                13:[],
                14:[],
                15:[],
                16:[],
                17:[],
                18:[],
                19:[]}

def plus_one_day(v_speed, h_speed, x_pos, y_pos):
    x = (x_pos + h_speed) % 20
    y = (y_pos + v_speed) % 20
    return x, y

def run_red_simulator(v_speed, h_speed, x_pos, y_pos, day, grid):
    # clue 1
    if v_speed != 1:
        pass
    # clues 2 and 6
    elif h_speed not in {1,2,3,4,5,6,7,8,10,12,14,15,20}:
        pass
    # clue 11
    elif h_speed not in {7,8,9}:
        pass
    else:
        is_valid = True
        for i in range(1, day):
            if i == 5 and (x_pos, y_pos) != (6, 17):
                is_valid = False
                break
            if (x_pos, y_pos) in guessed_days[i] and i < 4:
                is_valid = False
                break
            # clue 4
            if i == 2 and x_pos != 5:
                is_valid = False
                break
            if i == 4 and (x_pos, y_pos) != (19, 16):
                is_valid = False
                break

            # clue 10 is red
            if i == 8 and y_pos != 0:
                is_valid = False
                break

            # clue 17 is not red
            # if i == 14 and x_pos != 4:
            #     is_valid = False
            #     break

            # clue 13 is not red
            # if i == 6 and y_pos != 4: 
            #     is_valid = False
            #     break

            # clue 18 is not red
            # if i == 15 and x_pos != 7:
            #     is_valid = False
            #     break

            # clue 19 is not red
            # if i == 16 and x_pos != 8:
            #     is_valid = False
            #     break
            x_pos, y_pos = plus_one_day(v_speed, h_speed, x_pos, y_pos)

        if (x_pos, y_pos) in guessed_days[day]:
            is_valid = False   
        if is_valid:
            grid = update_grid(grid, x_pos, y_pos)
    return grid

def run_blue_simulator(v_speed, h_speed, x_pos, y_pos, day, grid):
    # clue 3
    if h_speed in {3,6,9}:
        pass
    # clue 5
    elif v_speed in {1,3,5}:
        pass
    # clue 7
    elif v_speed in {4,7,6}:
        pass
    # clue 8
    elif v_speed not in {1,2,3,4,5,6,7,8,10,12,14,15,20}:
        pass
    # clue 15
    elif v_speed % 2 == 0:
        pass
    else:
        is_valid = True
        for i in range(1, day):
            if i == 10 and (x_pos, y_pos) != (2, 4):
                is_valid = False
                break
            if (x_pos, y_pos) in guessed_days[i] and i < 10:
                is_valid = False
                break
            # clue 14
            if i == 4 and y_pos != 14:
                is_valid = False
                break

            #clue 13 is blue
            if i == 6 and y_pos != 4:
                is_valid = False
                break

            # clue 17 is not blue
            # if i == 14 and x_pos != 4:
            #     is_valid = False
            #     break

            # clue 10 is not blue
            # if i == 8 and y_pos != 0:
            #     is_valid = False
            #     break

            # test clue 18 can not be blue as it is orange. invert
            if i == 15 and x_pos == 7:
                is_valid = False
                break
            # clue 19 is blue
            if i == 16 and x_pos != 8:
                is_valid = False
                break

            x_pos, y_pos = plus_one_day(v_speed, h_speed, x_pos, y_pos)
        if (x_pos, y_pos) in guessed_days[day]:
            is_valid = False
        if is_valid:
            grid = update_grid(grid, x_pos, y_pos)
    return grid

def run_orange_simulator(v_speed, h_speed, x_pos, y_pos, day, grid):
    # clue 12
    if h_speed not in {1,3,4}:
        pass
    # clue 16
    if h_speed not in {3,2,4}:
        pass
    else:
        is_valid = True
        for i in range(1, day):
            if i == 13 and (x_pos, y_pos) != (1,0):
                is_valid=False
                break
            if (x_pos, y_pos) in guessed_days[i] and i < 13:
                is_valid = False
                break
            # clue 9
            if i == 7 and y_pos == 6:
                is_valid = False
                break
            # clue 10 is orange
            if i == 8 and y_pos != 0:
                is_valid = False
                break
            # clue 13 is orange
            if i == 6 and y_pos != 4:
                is_valid = False
                break
            # test clue 17
            if i == 14 and x_pos != 4:
                is_valid = False
                break
            # test clue 18 must be orange
            if i == 15 and x_pos != 7:
                is_valid = False
                break
            # clue 19 is not orange
            # if i == 16 and x_pos == 8:
            #     is_valid = False
            #     break
            x_pos, y_pos = plus_one_day(v_speed, h_speed, x_pos, y_pos)
        if is_valid:
            grid = update_grid(grid, x_pos, y_pos)
    return grid

def update_grid(grid, x_pos, y_pos):
    if x_pos == 0:
        x_pos = 20
    if y_pos == 0:
        y_pos = 20
    grid[y_pos-1][x_pos-1] += 1
    return grid


if __name__ == '__main__':
    day = 20
    for i in range(35):
        print(i**2)
    grid = np.array([[0] * 20] * 20)
    for a in range(1,21):
        print(a)
        for b in range(1,21):
            for c in range(1,21):
                for d in range(1,21):
                    test = (a,b,c,d)
                    grid = run_red_simulator(*test, day, grid) #clue 13 is not red
                    grid = run_orange_simulator(*test, day, grid)
                    grid = run_blue_simulator(*test, day, grid)

    ranked_list = sorted([(i, j) for i in range(1, 21) for j in range(1,21)], key=lambda x: grid[x[1]-1][x[0]-1], reverse=True)
    print("Shoot at :")
    for i in range(15):
        print(ranked_list[i])

    plt.imshow(grid, origin='lower', extent=[1,20,1,20], aspect='auto')
    plt.colorbar()
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title(f"Red drone on day {day}")
    plt.show()

    # for n in range(729):
    #     if n % 2 == 1:
    #         counter = 0
    #         for i in range(n, 729):
    #             if i % 2 == 0:
    #                 counter += 1
    #         if counter == n:
    #             print(n)
