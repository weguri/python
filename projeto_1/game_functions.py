import sys

import pygame


def checar_events(ship):
    """Rende a eventos de pressionamento de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                # Move a espaçonave para a direita
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para nova tela"""

    # Redesenha a tela a cadda passagem pelo laço
    screen.fill(ai_settings.bg_color)

    # Redesenha a tela a cada passagem pela laço
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
