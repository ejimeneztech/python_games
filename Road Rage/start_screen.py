import pygame
import sys
# Add music to title screen

def menu_screen():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [400, 600]
    bg = "black"

    screen = pygame.display.set_mode(size)

    color = "white"

    start_button = pygame.Rect(100, 100, 200, 50)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom

    quit_button = pygame.Rect(100, 200, 200, 50)

    # defining a font 
    smallfont = pygame.font.SysFont('Corbel',35) 
  
    # rendering a text written in 
    # this font 
    start_text = smallfont.render('Start' , True , color) 
    quit_text = smallfont.render('Quit', True, color)

    at_start_screen = True
    
    while at_start_screen:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if start_button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    #print('button was pressed at {0}'.format(mouse_pos))
                    at_start_screen = False
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.fill(bg)

        # draw buttons (Work on centering text: https://stackoverflow.com/questions/23982907/how-to-center-text-in-pygame)
        pygame.draw.rect(screen, [0, 255, 0], start_button)  
        screen.blit(start_text, start_button)

        pygame.draw.rect(screen, [255,0,0], quit_button)
        screen.blit(quit_text,quit_button)


        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    menu_screen()