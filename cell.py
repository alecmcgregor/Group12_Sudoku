import sudoku_generator as sg
import pygame

class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen #for now I'm going to imagine this little cell as it's own screen
    def set_cell_value(self,value):
        self.value=value
    def set_sketched_value(self,value):
        self.value=value
    def draw(self):
        #Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected. (I feel like this should be implemented elsewhere like in the events for the game)
        board=sg.OBJECT.get_board() #OBJECT will be what ever I name my first sudoku_generator object
        if board[self.row][self.col]>0:
            value_font=pygame.font.Font(None,11)
            value_surface=value_font.render(f'{self.value}', 0, "black")
            value_rectangle=value_surface.get_rect(center=(((WIDTH//9)//2)*self.col,((HEIGHT//9)//2)*self.row))#change WIDTH and HEIGHT to proper variables once implemented
            self.screen.blit(value_surface,value_rectangle)
        else:
            pygame.draw.rect(self.screen,'light blue',pygame.Rect((WIDTH//9)*self.col,(HEIGHT//9)*self.row,(WIDTH//9)*(self.col+1),(HEIGHT//9)*(self.row+1))) #this only works if row and col start from 0 and go to 8