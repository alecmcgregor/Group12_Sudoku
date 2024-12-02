import pygame, sys
import sudoku_generator

#THESE GLOBAL VARIABLES ARE NEEDED FOR THE CODE TO FUNCTION
width = 576
height = 640 #additional 64 pixels of height for 3 buttons

def draw_game_start(screen):
    title_font=pygame.font.Font(None,64)
    button_font=pygame.font.Font(None,32)
    screen.fill("light blue")
    title_surface=title_font.render("Welcome to Sudoku",0,"black")
    title_box=title_surface.get_rect(center=(width//2,(height-64)//2-150))
    screen.blit(title_surface,title_box)
    game_mode_font=pygame.font.Font(None, 42)
    game_mode_surface=game_mode_font.render("Select game mode:",0,"black")
    game_mode_box=game_mode_surface.get_rect(center=(width//2,(height-64)//2))
    screen.blit(game_mode_surface,game_mode_box)
    easy_text=button_font.render("Easy",0,(0,0,0))
    normal_text=button_font.render("Normal",0,(0,0,0,))
    hard_text=button_font.render("Hard",0,(0,0,0))
    easy_surface=pygame.Surface((easy_text.get_size()[0]+20,easy_text.get_size()[1]+20))
    easy_surface.fill("orange")
    easy_surface.blit(easy_text,(10,10))
    normal_surface=pygame.Surface((normal_text.get_size()[0]+20,normal_text.get_size()[1]+20))
    normal_surface.fill("orange")
    normal_surface.blit(normal_text,(10,10))
    hard_surface=pygame.Surface((hard_text.get_size()[0]+20,hard_text.get_size()[1]+20))
    hard_surface.fill("orange")
    hard_surface.blit(hard_text,(10,10))
    easy_box=easy_surface.get_rect(center=(width//4,(height-64)//2+150))
    normal_box=normal_surface.get_rect(center=(width//2,(height-64)//2+150))
    hard_box=hard_surface.get_rect(center=((width//4)*3,(height-64)//2+150))
    screen.blit(easy_surface,easy_box)
    screen.blit(normal_surface,normal_box)
    screen.blit(hard_surface,hard_box)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if easy_box.collidepoint(event.pos):
                    return 30
                elif normal_box.collidepoint(event.pos):
                    return 40
                elif hard_box.collidepoint(event.pos):
                    return 50
        pygame.display.update()

# def draw_winner_screen(screen):
#
#
# def draw_loser_screen(screen):

class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.selected = False

    def set_cell_value(self,value):
        self.value=value
    def set_sketched_value(self,value):
        self.value=value
    def draw(self):
        # The cell is outlined red if it is currently selected. (I feel like this should be implemented elsewhere like in the events for the game)
        cell_width=width//9
        cell_height=(height-64)//9
        margin=2
        if self.value>0:
            value_font=pygame.font.Font(None,36)
            value_text=value_font.render(f'{self.value}',0,"black")
            value_box=value_text.get_rect(center=(self.col*cell_width+cell_width//2,self.row*cell_height+cell_height//2))
            self.screen.blit(value_text,value_box)
        else:
            pygame.draw.rect(self.screen,'light blue',(self.col*cell_width+margin,self.row*cell_height+margin,cell_width-2*margin,cell_height-2*margin))

        # Highlight the selected cell
        if self.selected:
            pygame.draw.rect(self.screen, 'red',
                             (self.col * cell_width,
                              self.row * cell_height,
                              cell_width, cell_height), width=3)

class Board:
    def __init__(self,width,height,screen,difficulty,board):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.board=board
        self.cells = [[Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)]
        self.selected = (0, 0)

    def draw(self):
        # Draw thin grid lines for all cells (9x9 grid)
        for i in range(0, self.width + 1, int(self.width / 9)):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height))
        for i in range(0, self.height + 1, int(self.height / 9)):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i))

        # Draw thick grid lines for the 3x3 sub-boxes
        for i in range(0, self.width + 1, int(self.width / 3)):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height), width=3)
        for i in range(0, self.height + 1, int(self.height / 3)):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i), width=3)

        # Iterate over the pre-initialized self.cells to draw each cell
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    def select(self, row, col):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].selected = False

        self.cells[row][col].selected = True
        self.selected = (row, col)

    def click(self, x, y):
        cell_width = self.width // 9
        cell_height = self.height // 9
        row, col = y // cell_height, x // cell_width
        if 0 <= row < 9 and 0 <= col < 9:
            self.select(row, col)

    def sketch(self, value):
        row, col = self.selected
        self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        row, col = self.selected
        self.cells[row][col].set_cell_value(value)



def main():
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Sudoku")
    difficulty=draw_game_start(screen)
    game=sudoku_generator.SudokuGenerator(9,difficulty)
    game.fill_values()
    solution=game.get_board()
    game.remove_cells()
    board=game.get_board()
    game_board=Board(width,(height-64),screen,difficulty,board)
    screen.fill("light blue")
    game_board.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                game_board.click(x, y)

            # Handle key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    row, col = game_board.selected
                    if row > 0:
                        game_board.select(row - 1, col)
                elif event.key == pygame.K_DOWN:
                    row, col = game_board.selected
                    if row < 8:
                        game_board.select(row + 1, col)
                elif event.key == pygame.K_LEFT:
                    row, col = game_board.selected
                    if col > 0:
                        game_board.select(row, col - 1)
                elif event.key == pygame.K_RIGHT:
                    row, col = game_board.selected
                    if col < 8:
                        game_board.select(row, col + 1)
                elif pygame.K_1 <= event.key <= pygame.K_9:  # Numbers 1-9
                    game_board.place_number(event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:  # Confirm placement
                    row, col = game_board.selected
                    # Additional logic to confirm input can be added here.

        screen.fill("light blue")
        game_board.draw()
        pygame.display.update()

if __name__=="__main__":
    main()