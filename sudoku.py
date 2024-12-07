import pygame, sys
import sudoku_generator

width = 576
height = 640 #additional 64 pixels of height for 3 buttons

def draw_game_start(screen):
    #create fonts being used
    title_font=pygame.font.Font(None,64)
    button_font=pygame.font.Font(None,32)
    screen.fill("light blue")

    #create title
    title_surface=title_font.render("Welcome to Sudoku",True,"black")
    title_box=title_surface.get_rect(center=(width//2,(height-64)//2-150))
    screen.blit(title_surface,title_box)

    #create game mode message
    game_mode_font=pygame.font.Font(None, 42)
    game_mode_surface=game_mode_font.render("Select game mode:",True,"black")
    game_mode_box=game_mode_surface.get_rect(center=(width//2,(height-64)//2))
    screen.blit(game_mode_surface,game_mode_box)

    #create easy, normal and hard buttons
    easy_text=button_font.render("Easy",True,(0,0,0))
    normal_text=button_font.render("Normal",True,(0,0,0,))
    hard_text=button_font.render("Hard",True,(0,0,0))
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
            if event.type==pygame.QUIT: #if the screen is exited with x in top right corner
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN: #if any of the difficulty boxes are selected
                if easy_box.collidepoint(event.pos):
                    return 30
                elif normal_box.collidepoint(event.pos):
                    return 40
                elif hard_box.collidepoint(event.pos):
                    return 50
        pygame.display.update()

def draw_in_game_buttons(screen):
    #font used for buttons
    button_font = pygame.font.Font(None, 32)

    # reset button generation
    reset_text = button_font.render("Reset", True, (255, 255, 255))
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill("orange")
    reset_surface.blit(reset_text, (10, 10))
    reset_box = reset_surface.get_rect(center=(width // 4, height - 32))
    screen.blit(reset_surface, reset_box)

    # restart button generation
    restart_text = button_font.render("Restart", True, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("orange")
    restart_surface.blit(restart_text, (10, 10))
    restart_box = restart_surface.get_rect(center=(width // 2, height - 32))
    screen.blit(restart_surface, restart_box)

    # exit button generation
    exit_text = button_font.render("Exit", True, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill("orange")
    exit_surface.blit(exit_text, (10, 10))
    exit_box = exit_surface.get_rect(center=((width // 4) * 3, height - 32))
    screen.blit(exit_surface, exit_box)

    #returning the boxes for collision purposes in the main code
    return reset_box, restart_box, exit_box

# def draw_winner_screen(screen):
def draw_winner_screen(screen):
    font = pygame.font.Font(None, 64)
    screen.fill("light blue")
    text = font.render("You Win!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(text, text_rect)
    button_font=pygame.font.Font(None,32)
    exit_text = button_font.render("Exit", True, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill("orange")
    exit_surface.blit(exit_text, (10, 10))
    exit_box = exit_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(exit_surface, exit_box)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if exit_box.collidepoint(event.pos):
                    sys.exit()

# def draw_loser_screen(screen):
def draw_loser_screen(screen):
    font = pygame.font.Font(None, 64)
    screen.fill("light blue")
    text = font.render("Game Over :(", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(text, text_rect)
    button_font = pygame.font.Font(None, 32)
    restart_text = button_font.render("Restart", True, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("orange")
    restart_surface.blit(restart_text, (10, 10))
    restart_box = restart_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(restart_surface, restart_box)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if restart_box.collidepoint(event.pos):
                    #use return to break out of the for and while loop and resume the next line in the main code
                    return


class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.selected = False

    #will change the instance attribute value to the value passed into this function
    def set_cell_value(self,value):
        self.value=value

    #will change the instance attribute sketched_value to the value passed into this function
    def set_sketched_value(self,value):
        self.sketched_value=value

    #will draw the value of the cell if it has one, and it will outline a cell if it is selected
    def draw(self):
        # The dimensions of each cell
        cell_width = width // 9
        cell_height = (height - 64) // 9
        margin = 2

        # Draw the confirmed value in the cell
        if self.value > 0:
            value_font = pygame.font.Font(None, 36)
            value_text = value_font.render(f'{self.value}', True, "black")
            value_box = value_text.get_rect(
                center=(self.col * cell_width + cell_width // 2, self.row * cell_height + cell_height // 2))
            self.screen.blit(value_text, value_box)

        # Draw the cell's background
        else:
            pygame.draw.rect(self.screen, 'light blue', (
            self.col * cell_width + margin, self.row * cell_height + margin, cell_width - 2 * margin,
            cell_height - 2 * margin))

        # Display sketched values in a smaller font
        if hasattr(self, 'sketched_value') and self.sketched_value > 0:
            sketch_font = pygame.font.Font(None, 30)
            sketch_text = sketch_font.render(f'{self.sketched_value}', True, (105, 105, 105))
            sketch_box = sketch_text.get_rect(topleft=(self.col * cell_width + 5, self.row * cell_height + 5))
            self.screen.blit(sketch_text, sketch_box)

        # Highlight the selected cell
        if self.selected:
            pygame.draw.rect(self.screen, 'red',
                             (self.col * cell_width, self.row * cell_height, cell_width, cell_height), width=3)


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        #generate sudoku board
        self.game = sudoku_generator.SudokuGenerator(9, difficulty)
        self.game.fill_values()
        self.game.remove_cells()
        self.solution = self.game.get_solved_board()  # save the solved board
        self.board = self.game.get_board() #board of play

        #generate cells
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]
        self.selected = (0, 0)

    def draw(self):
        # Draw thin grid lines for all cells (9x9 grid)
        for i in range(0, self.width + 1, int(self.width / 9)):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height))
        for i in range(0, self.height + 1, int(self.height / 9)):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i))

        # Draw thick grid lines for the 3x3 sub-boxes
        for i in range(int(self.width / 3), self.width, int(self.width / 3)):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height), width=3)
        for i in range(int(self.height / 3), self.height + 1, int(self.height / 3)):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i), width=3)

        #Draw all cells
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    #used to designate what cell is selected and should be highlighted
    def select(self, row, col):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].selected = False
        self.cells[row][col].selected = True
        self.selected = (row, col)

    #used to click on a cell with the mouse and pass the row and col into the select function
    def click(self, x, y):
        cell_width = self.width // 9
        cell_height = self.height // 9
        row, col = y // cell_height, x // cell_width
        if 0 <= row < 9 and 0 <= col < 9:
            return row, col
        return None

    # clears the value of a cell
    def clear(self):
        row, col = self.selected
        if hasattr(self.cells[row][col], 'sketched_value') and self.cells[row][col].sketched_value > 0:
            self.cells[row][col].set_sketched_value(0)
        elif self.board[row][col] == 0 and self.cells[row][col].value > 0:
            self.cells[row][col].set_cell_value(0)

    #changes the sketched value of a cell
    def sketch(self, value):
        row, col = self.selected
        if self.board[row][col] == 0:
            self.cells[row][col].set_sketched_value(value)

    #changes the value of a cell
    def place_number(self, value):
        row, col = self.selected
        if hasattr(self.cells[row][col], 'sketched_value') and self.cells[row][col].sketched_value > 0:
            self.cells[row][col].set_cell_value(value)
            self.cells[row][col].set_sketched_value(0)

    #will reset all entered values to zero so that the board is in its original state
    def reset_to_original(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]

    # check if the board is full
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:  # An empty cell is denoted by 0
                    return False
        return True

    # update the values from the cells
    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    # find_empty function ended up not being useful for the sake of our code

    # checks whether the board is correctly solved
    def check_board(self):
        if self.board == self.solution:
            return True
        return False


def main():
    #initalizes pygame and brings up the start screen
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Sudoku")
    difficulty=draw_game_start(screen)

    #initializes the board based on the selected difficulty and displays it
    screen.fill("light blue")
    game_board = Board(width, height - 64, screen, difficulty)
    game_board.draw()
    reset_box, restart_box, exit_box = draw_in_game_buttons(screen)
    pygame.display.update()
    print(game_board.solution) #for the purpose of debugging easier so that we have a key to look at

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            # Handle top right exit button
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                result = game_board.click(x, y)
                # For selecting a cell
                if result:
                    row, col = result
                    game_board.select(row, col)
                #event for button to reset the board
                if reset_box.collidepoint(event.pos):
                    game_board.reset_to_original()
                #event for button to restart the game entirely
                if restart_box.collidepoint(event.pos):
                    difficulty = draw_game_start(screen)
                    screen.fill("light blue")
                    game_board = Board(width, height - 64, screen, difficulty)
                    game_board.draw()
                    reset_box, restart_box, exit_box = draw_in_game_buttons(screen)
                    pygame.display.update()
                    print(game_board.solution) #for the purpose of debugging easier so that we have a key to look at
                    continue
                #event for button to exit the program
                if exit_box.collidepoint(event.pos):
                    running = False

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
                    game_board.sketch(event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:  # Confirm placement
                    row, col = game_board.selected
                    if hasattr(game_board.cells[row][col], 'sketched_value') and game_board.cells[row][col].sketched_value > 0:
                        game_board.place_number(game_board.cells[row][col].sketched_value)
                elif event.key == pygame.K_BACKSPACE: #deletes cell value
                    game_board.clear()

        #section to update the screen after each iteration
        screen.fill("light blue")
        game_board.draw()
        reset_box, restart_box, exit_box = draw_in_game_buttons(screen)
        pygame.display.update()

        # checks to see if the board is full so the game ends
        if game_board.is_full():
            game_board.update_board() #updates all cell choices into the board
            if game_board.check_board(): #compares our choices and the save answer key
                draw_winner_screen(screen) #will display winner screen
            else:
                draw_loser_screen(screen) #will display loser screen
                #will initialize a new game without needing to leave the game loop
                difficulty = draw_game_start(screen)
                screen.fill("light blue")
                game_board = Board(width, height - 64, screen, difficulty)
                game_board.draw()
                reset_box, restart_box, exit_box = draw_in_game_buttons(screen)
                pygame.display.update()
                print(game_board.solution) #for the purpose of debugging easier so that we have a key to look at



if __name__=="__main__":
    main()