import pygame
from pygame.draw import *

def fill(display, *args, **kw):
    display.fill(*args, **kw)

    
set_mode = pygame.display.set_mode

_font_cache = {}
def get_font(name, size):
    global _font_cache
    f = _font_cache.get((name,size), None)
    if not f:
        f = pygame.font.Font(name, size)
        _font_cache[(name,size)] = f
    return f


def draw_font(surface, font_rendered_surface, pos):
    surface.blit(font_rendered_surface, pos)

def lock(surface):
    surface.lock()

def unlock(surface):
    surface.unlock()