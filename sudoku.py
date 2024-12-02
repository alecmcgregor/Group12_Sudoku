import sudoku_generator as sg
import pygame
class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
    def set_cell_value(self,value):

def main():
    try:
        pygame.init()
    finally:
        pygame.quit()

if __name__=="__main__":
    main()