import pygame   #pygame basic settings
width = 550
white = (251,247,245)
black = (0,0,0)
blue = (52,31,151)
pygame.init()
font = pygame.font.SysFont('timesnewroman', 35)
buffer = 5

def main():     #pygame window initialization
    window = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    window.fill(white)

    grid_draw(window)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                insert(window, (position[0]//50, position[1]//50))

            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
def grid_draw(window):
    for i in range(0, 10):
        if (i%3==0):            #defining line width for the different lines
            line_width = 4
        else: line_width = 2
        pygame.draw.line(window, black, (50+50*i, 50), (50+50*i, 500), line_width)   #Vertical lines drawing
        pygame.draw.line(window, black, (50, 50+50*i), (500, 50+50*i), line_width)   #Horizontal lines drawing

def insert(window, position):
    i, j = position[0], position[1]
    while True:     #probar con pygame.event.wait
        for event in pygame.evemt.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid[i-1][j-1] != 0):
                    return
                if (event.key == 48):
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(window, white, position[0]*50 + 5, position[1] + 5, 40, 40)
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(window, white, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = font.render(str(event.key-48), True, (0,0,0))
                    window.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return#mejorar esta parte, un solo if es y otro ramificado
                    
                    
                    
                    
main()
grid = []