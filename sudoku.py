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
def draw_winner_screen(screen):
    font = pygame.font.Font(None, 64)
    text = font.render("You Win!", True, (0, 255, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text, text_rect)

# def draw_loser_screen(screen):
def draw_loser_screen(screen):
    font = pygame.font.Font(None, 64)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text, text_rect)



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
        # The dimensions of each cell
        cell_width = width // 9
        cell_height = (height - 64) // 9
        margin = 2

        # Draw the confirmed value in the cell
        if self.value > 0:
            value_font = pygame.font.Font(None, 36)
            value_text = value_font.render(f'{self.value}', 0, "black")
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
            sketch_font = pygame.font.Font(None, 20)
            sketch_text = sketch_font.render(f'{self.sketched_value}', 0, "grey")
            sketch_box = sketch_text.get_rect(topleft=(self.col * cell_width + 5, self.row * cell_height + 5))
            self.screen.blit(sketch_text, sketch_box)

        # Highlight the selected cell
        if self.selected:
            pygame.draw.rect(self.screen, 'red',
                             (self.col * cell_width, self.row * cell_height, cell_width, cell_height), width=3)


class Board:
    def __init__(self, width, height, screen, difficulty, board, generator):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = board
        self.generator = generator
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
        self.cells[row][col].sketched_value = value

    def place_number(self, value):
        row, col = self.selected
        if self.generator.is_valid(row, col, value):
            self.cells[row][col].set_cell_value(value)
            self.update_board()
        else:
            print("Invalid move!")

    # check if the board is full
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:  # If any cell is empty (0)
                    return False
        return True

    # update the  the values from the cells
    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    # find an empty cell and return its row and column (x, y)
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:  # An empty cell is denoted by 0
                    return (row, col)
        return None  # If no empty cell is found

    # check whether the board is correctly solved
    def check_board(self):
        solved_board = solution  # Access the solved board from the generator
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != solved_board[row][col]:
                    return False
        return True

def main():
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Sudoku")

    difficulty=draw_game_start(screen)
    game = sudoku_generator.SudokuGenerator(9, difficulty)
    game.fill_values()
    solution = game.get_solved_board()
    game.remove_cells()
    board = game.get_board()
    game_board = Board(width, height - 64, screen, difficulty, board, game)

    #pygame.display.update()

    # define buttons with the position and sizes
    reset_button = pygame.Rect(50, height - 60, 100, 40)
    restart_button = pygame.Rect(200, height - 60, 100, 40)
    exit_button = pygame.Rect(350, height - 60, 100, 40)

    # ESHA- i changed this a little
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                game_board.click(x, y)
            # Check button clicks
                if reset_button.collidepoint(event.pos):
                    game_board = Board(width, height - 64, screen, difficulty, game.get_board())
                elif restart_button.collidepoint(event.pos):
                    return
                elif exit_button.collidepoint(event.pos):
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
                    game_board.place_number(event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:  # Confirm placement
                    row, col = game_board.selected
                    # Additional logic to confirm input can be added here.


        # Check for win or lose
        if game_board.is_full():
            if game_board.check_board():  # Check if the board is solved correctly
                draw_winner_screen(screen)
            else:
                draw_loser_screen(screen)

        screen.fill("light blue")
        game_board.draw()
            # Draw buttons with orange background and white text
        button_font = pygame.font.Font(None, 36)

        # Draw Reset button
        pygame.draw.rect(screen, (255, 165, 0), reset_button)  # Orange color
        reset_text = button_font.render("Reset", True, (255, 255, 255))  # White font
        screen.blit(reset_text, reset_button.move(30, 10))

        # Draw Restart button
        pygame.draw.rect(screen, (255, 165, 0), restart_button)  # Orange color
        restart_text = button_font.render("Restart", True, (255, 255, 255))  # White font
        screen.blit(restart_text, restart_button.move(20, 10))

        # Draw Exit button
        pygame.draw.rect(screen, (255, 165, 0), exit_button)  # Orange color
        exit_text = button_font.render("Exit", True, (255, 255, 255))  # White font
        screen.blit(exit_text, exit_button.move(30, 10))




        pygame.display.update()

if __name__=="__main__":
    main()