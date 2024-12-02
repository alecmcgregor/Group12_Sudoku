import sudoku_generator as sg
import board
import pygame

class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=None #confused as to why this is helpful
    def set_cell_value(self,value):
        self.value=value
    def set_sketched_value(self,value):
        self.value=value
    def draw(self):
        #Draws this cell, along with the value inside it.

        #If this cell has a nonzero value, that value is displayed.
        #Otherwise, no value is displayed in the cell.
        #The cell is outlined red if it is currently selected.