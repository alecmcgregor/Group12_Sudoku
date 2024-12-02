import sudoku_generator as sg
import pygame

class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
    def set_cell_value(self,value):
        self.value=value
    def set_sketched_value(self,value):
        self.value=value
    #def draw(self):
        #Draws this cell, along with the value inside it.
        #If this cell has a nonzero value, that value is displayed.
        #Otherwise, no value is displayed in the cell.
        #The cell is outlined red if it is currently selected.

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width=576
        self.height=576
        self.screen=None #confused as to why this is helpful?
        self.difficulty=difficulty
    def draw(self):
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.screen.fill("light blue")
        for i in range(0,self.width+1,64):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height))
            #would need different for loop for these lines if height was different from width
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i))
        for i in range(0,self.width+1,192):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height),width=3)
            #would need different for loop for these lines if height was different from width
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i),width=3)


#for now this is just me testing that the classes are working properly, will likely not be implemented exactly like so into the final code
def main():
    try:
        pygame.init()
        board=Board(288,288,"Name","hard")
        clock = pygame.time.Clock()
        board.draw()
        running=True
        while running:
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__=="__main__":
    main()