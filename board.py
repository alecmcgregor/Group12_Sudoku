import sudoku_generator as sg
import pygame
import cell
class Board(cell.Cell):
    def __init__(self,width,height,screen,difficulty):
        self.width=width
        self.height=height
        self.screen=None #confused as to why this is helpful?
        self.difficulty=difficulty
    def draw(self):
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.screen.fill("light blue")
        for i in range(0,self.width+1,int(self.width/9)):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height))
        for i in range(0,self.height+1,int(self.height/9)):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i))
        for i in range(0,self.width+1,int(self.width/3)):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height),width=3)
        for i in range(0,self.height+1,int(self.height/3)):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i),width=3)
        board=sg.OBJECT.get_board() #OBJECT will be name of object initialized in sudoku_generator
        row_counter=0
        col_counter=0
        for num in range(81):
            num=cell.Cell(board[row_counter][col_counter],)