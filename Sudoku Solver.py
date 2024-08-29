#in this project I will use the backtracking algorithm
#steps of backtraking for this project:
#   1.)pick a starting point
#   2.)try all numbers until conditions are satisfied
#   3.)if a number works, move to the next square. else, backtrack
#   4.)repeat to step 2 until board is solved

#***things to watch for***
#everything is denoted as y, x
#0 means an empty space

board = [[0,5,6,9,0,7,4,0,0],
         [0,8,1,0,4,0,0,0,0],
         [0,0,0,0,1,5,0,9,0],
         [0,0,0,0,0,3,8,5,7],
         [8,4,0,0,6,0,0,2,3],
         [7,3,9,2,0,0,0,0,0],
         [0,6,0,5,8,0,0,0,0],
         [0,0,0,0,7,0,3,6,0],
         [0,0,8,3,0,6,5,7,0]
        ]



#print_board(board)
#prints board
def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            print(bo[i][j], end = ' ')
            if (j+1) % 3 == 0:
                print('|', end = ' ')
        print('')
        if (i+1)% 3 == 0:
            print('-'*22)
#finds an open cell(step 1)
#I want the algorithm to start in the top left of the cell, prioritize top row
def find_cell(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return i, j#it returns row, column. That means y,x.
    return False
    
#checks which numbers work for a specific cell
#it will return bool
def valid(bo, num, pos): #pos will be a tuple in (y, x) form
    #checks rows
    if num in bo[pos[0]]:
        return False
    
    #check columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[1] != 1:#*** may cause error
            return False
    
    #find the box it is in. cont using (y, x) format
    box_pos = [0, 0]

    box_pos[0] = pos[0] // 3
    box_pos[1] = pos[1] // 3

    #check boxes
    for i in range(box_pos[0]*3, box_pos[0]*3 + 3):
        for j in range(box_pos[1]*3, box_pos[1]*3 + 3):
            if bo[i][j] == num:
                return False
    
    
    #if all of them work
    return True

def solve(model):
    #base case
    find = find_cell(model)
    if find == False:
        return True#this is b/c puzzle is solved already
    else:
        row, column = find
        
    #check a solution for a cell
    for i in range(1, 10):
            
        if valid(model, i, (row, column)):
            model[row][column] = i#adds the new box to our board

                
            if solve(model):#tries to solve new board
                return True

            model[row][column] = 0#if it cant solve the new board, it backtracks and turns the value to 0
    return False
'''def solve(bo):
    #base case
    find = find_cell(board)
    if find == False:
        return True#this is b/c puzzle is solved already
    else:
        row, column = find

    #check a solution for a cell
    for i in range(1, 10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i#adds the new box to our board

            
            if solve(bo):#tries to solve new board
                return True

            bo[row][column] = 0#if it cant solve the new board, it backtracks and turns the value to 0
    return False'''

#gui part of the project

import pygame
import time


pygame.init()

black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
gray = (100, 100, 100)

screen_x, screen_y = 600, 600
screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
    
class Cube:
    
    def __init__(self, val, row, column, width, height):#(pos is int (y, x)#if error, put width and height back in
        self.val = val
        self.temp_val = 0
        self.row = row
        self.colm = column
        self.width = width
        self.height = height
        self.selected = False
    def draw(self):
        #defines stuff
        x = (self.colm*self.width)
        y = (self.row*self.height)

        #decides if it is drawing permanent script or penciled script
        if self.temp_val != 0 and self.val == 0:
            myfont = pygame.font.SysFont("Arial", 20)
            text = myfont.render(str(self.temp_val), 1, gray)
            screen.blit(text, (x + 5, y + 5))
        elif self.val != 0:
            myfont = pygame.font.SysFont("Arial", 40)
            text = myfont.render(str(self.val), 1, black)
            screen.blit(text, (x +(self.width - text.get_width())/2, y +(self.height - text.get_height())/2))

        #highlights the box if selected
        if self.selected:
            pygame.draw.rect(screen, red,(x ,y, self.width, self.height), 3)###may cause error
    def set_val(self, val):
        self.val = val
    def set_temp_val(self, temp_val):
        self.temp_val = temp_val

class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    '''board = [
         [0,5,6,9,0,7,4,0,0],
         [0,8,1,0,4,0,0,0,0],
         [0,0,0,0,1,5,0,9,0],
         [0,0,0,0,0,3,8,5,7],
         [8,4,0,0,6,0,0,2,3],
         [7,3,9,2,0,0,0,0,0],
         [0,6,0,5,8,0,0,0,0],
         [0,0,0,0,7,0,3,6,0],
         [0,0,8,3,0,6,5,7,0]
        ]'''
    solved_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    solve(solved_board)
    print(solved_board)
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width/9, height/9) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = self.board#None
        self.selected = None
    def draw(self):
        #draw gridlines
        for i in range(self.rows + 1):#is from 0 to 9 inclusive
            if i % 3 == 0 or i == 0 or i == self.rows:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(screen, black, (0, (self.height/9)*i), (self.width, (self.height/9)*i), thick)
            pygame.draw.line(screen, black, ((self.width/9)*i, 0), ((self.width/9)*i, self.height), thick)

        #draw cubes
        for i in range(len(self.cubes)):
            for j in range(len(self.cubes[i])):
                self.cubes[i][j].draw()
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp_val(val)
    def update_model(self):
        #updates the models matrix of values
        self.model = [[self.cubes[i][j].val for j in range(self.cols)] for i in range(self.rows)]
    def place(self, num):
        row, colm = self.selected
        if self.cubes[row][colm].val == 0:
            self.cubes[row][colm].set_val(num)
            self.update_model()
            if self.cubes[row][colm].val == self.solved_board[row][colm]:#if the new value works, its a part of the board valid(self.board, num, (row, colm))
                return True
            else:#if it doesn't work it resets
                self.cubes[row][colm].set_val(0)
                self.update_model()
                return False
    def select(self, row, colm):
        #reset all selected pieces
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        #selectes piece cursor is over
        self.cubes[row][colm].selected = True
        self.selected = (row, colm)
        
    def click(self, mouse_pos):
        X, Y = mouse_pos
        if X < self.width and Y < self.height:
            row = int(Y//(self.height/9))
            colm = int(X//(self.width/9))
            return (int(row), int(colm))
        else:
            return None
    def clear_selected_cube(self):
        row, colm = self.selected
        if self.cubes[row][colm].temp_val != 0:
            self.cubes[row][colm].set_temp_val(0)
    def clear_all(self):
        for row in range(len(self.cubes)):
            for colm in range(len(self.cubes[row])):
                if self.cubes[row][colm].temp_val != 0:
                    self.cubes[row][colm].set_temp_val(0)
    def pretty_solve(self):
        c_vals = [[self.cubes[row][colm].val for colm in range(self.cols)] for row in range(self.rows)]
        #base case
        find = find_cell(c_vals)
        if find == False:
            return True#this is b/c puzzle is solved already
        else:
            row, colm = find
            self.select(row, colm)
        redraw_screen()
        #check a solution for a cell
        for i in range(1, 10):
            
            if valid(c_vals, i, (row, colm)):
                self.cubes[row][colm].val = i#adds the new box to our board

                
                if self.pretty_solve():#tries to solve new board
                    return True

                self.cubes[row][colm].val = 0#if it cant solve the new board, it backtracks and turns the value to 0
        return False
        '''for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].val = self.solved_board[i][j]'''
        
def redraw_screen():
    screen.fill(white)
    g.draw()
    pygame.display.update()
    
g = Grid(9, 9, 600, 600)
key = None
run = True
while run:
    
    for event in pygame.event.get():
        #print(event.type)
        #print(pygame.MOUSEBUTTONDOWN)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9
            if event.key == pygame.K_BACKSPACE:
                g.clear_selected_cube()
                key = None
            if event.key == pygame.K_DELETE:
                g.clear_all()
                key = None
            if event.key == pygame.K_s:
                g.pretty_solve()
                
            if event.key == pygame.K_RETURN:
                i, j = g.selected
                if g.cubes[i][j].temp_val != 0:
                    if g.place(g.cubes[i][j].temp_val):
                        print('good')
                    else:
                        myfont = pygame.font.SysFont("Arial", 50)
                        text = myfont.render('Try Again', 1, red)
                        screen.blit(text, ((screen_x - text.get_width())/2, (screen_y - text.get_height())/2))
                        pygame.display.update()
                        time.sleep(.5)
                    key = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X, mouse_Y = pygame.mouse.get_pos()
            clicked = g.click((mouse_X, mouse_Y))
            if clicked:
                g.select(clicked[0], clicked[1])
                key = None
    if g.selected and key != None:
        g.sketch(key)
        

    redraw_screen()
     
      
                
            
