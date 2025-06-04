import pygame
pygame.init()
screen_width, screen_height = 400, 200
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("welcome message")
light_pink=(255, 182, 193)
background_color = (0,0,0)
font=pygame.font.SysFont(None, 50) 
text=font.render("Welcome to this game!",True,light_pink)
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
running=True
while running:
    screen.fill(background_color)
    screen.blit(text, text_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()