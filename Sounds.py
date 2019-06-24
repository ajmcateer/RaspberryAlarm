import pygame
import settings

pygame.mixer.init()


def play_alarm():
    pygame.mixer.music.load(settings.root_path + "\\resources\\sounds\\alarm.wav")
    pygame.mixer.music.play(-1)  # note -1 for playing in loops
    pygame.mixer.music.set_volume(1)


def stop():
    pygame.mixer.music.set_volume(0)
    pygame.mixer.stop()
