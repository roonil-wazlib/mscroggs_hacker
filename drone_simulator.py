import numpy as np
import matplotlib.pyplot as plt

guessed_days = {1: [(1,1), (1,2), (1,3), (1,4), (1,5), (12,12), (16,20), (17,20), (18,20), (19,20), (20,20)], 
                2: [(2,1), (2,2), (2,3), (2,4), (2,5)], 
                3:[], 
                4:[(19,1), (19,2), (19,3), (19,4), (19,5), (19,17), (19,18), (19,19), (19,20)], 
                5:[], 
                6:[], 
                7:[]}

# 


def plus_one_day(v_speed, h_speed, x_pos, y_pos):
    x = (x_pos + h_speed) % 20
    y = (y_pos + v_speed) % 20
    return x, y

def run_red_simulator(v_speed, h_speed, x_pos, y_pos, day, grid):
    if v_speed != 1:
        pass
    elif h_speed not in {1,2,3,4,5,6,7,8,10,12,14,15,20}:
        pass
    else:
        is_valid = True
        for i in range(1, day):
            if (x_pos, y_pos) in guessed_days[i]:
                is_valid = False
                break
            if i == 2 and x_pos != 5:
                is_valid = False
                break
            if i == 4 and (x_pos, y_pos) != (19, 16):
                is_valid = False
                break
            x_pos, y_pos = plus_one_day(v_speed, h_speed, x_pos, y_pos)
        if (x_pos, y_pos) in guessed_days[day]:
            is_valid = False   
        if is_valid:
            grid = update_grid(grid, x_pos, y_pos)
    return grid

def run_blue_simulator(v_speed, h_speed, x_pos, y_pos, day, grid):
    if h_speed in {3,6,9}:
        pass
    else:
        is_valid = True
        for i in range(1, day):
            if (x_pos, y_pos) in guessed_days[i]:
                is_valid = False
                break
            x_pos, y_pos = plus_one_day(v_speed, h_speed, x_pos, y_pos)
        if (x_pos, y_pos) in guessed_days[day]:
            is_valid = False
        if is_valid:
            grid = update_grid(grid, x_pos, y_pos)
    return grid

def run_green_simulator(v_speed, h_speed, x_pos, y_pos, day, grid):
    is_valid = True
    for i in range(1, day):
        if (x_pos, y_pos) in guessed_days[i]:
            is_valid = False
            break
        x_pos, y_pos = plus_one_day(v_speed, h_speed, x_pos, y_pos)
    if (x_pos, y_pos) in guessed_days[day]:
        is_valid = False
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
    day = 5
    grid = np.array([[0] * 20] * 20)
    for a in range(1,21):
        print(a)
        for b in range(1,21):
            for c in range(1,21):
                for d in range(1,21):
                    test = (a,b,c,d)
                    # grid = run_red_simulator(*test, day, grid)
                    grid = run_green_simulator(*test, day, grid)
                    grid = run_blue_simulator(*test, day, grid)
    plt.imshow(grid, origin='lower', extent=[1,20,1,20], aspect='auto')
    plt.colorbar()
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title(f"Grid location by frequency of drone inhabitation on day {day}")
    plt.show()