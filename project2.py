import pygame
pygame.init()
screen_width, screen_height = 600, 300
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("welcome screen")
white=(255, 255, 255)
light_pink=(255, 182, 193)
light_blue=(173, 216, 230)
font=pygame.font.SysFont(None, 36)
text=font.render("Hello! Welcome to this game", True, light_pink)
text_rect=text.get_rect(center=(screen_width // 2, screen_height // 4))
rect_x, rect_y=150, 150
rect_width,rect_height=300, 100
running = True
while running:
    screen.fill(white)  
    screen.blit(text,text_rect)
    pygame.draw.rect(screen,light_blue,(rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()