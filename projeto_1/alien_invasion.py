import pygame
from projeto_1.settings import Settings
from projeto_1.ship import Ship
import projeto_1.game_functions as gf


def run_game():
    # Inicializa o jogo e cria um obejto para a tela
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasão")

    # Cria uma espaçonave
    ship = Ship(screen)

    # inicia o lalo principal do jogo
    while True:
        # Monitorar os eventos do teclado
        gf.checar_events(ship)

        # Atualização da tela
        gf.update_screen(ai_settings, screen, ship)


run_game()
