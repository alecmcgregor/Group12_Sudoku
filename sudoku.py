import sudoku_generator as sg




#for now this is just me testing that the classes are working properly, will likely not be implemented exactly like so into the final code
def main():
    try:
        pygame.init()
        board=Board(576,576,"Name","hard")
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