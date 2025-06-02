screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo")
manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()

while True:
    time_delta = clock.tick(60) / 1000.0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        manager.process_events(evento)

    screen.fill((0, 0, 0))  # Fundo preto
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()
