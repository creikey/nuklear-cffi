#!/usr/bin/env python

"""
A demo of the nuklear-cffi binding.
"""

import pygame
from overview import Overview

import pynk
import pynk.nkpygame

#from overview import Overview

if __name__ == '__main__':

    # Initialise pygame.
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    # Some state for the GUI.
    EASY = 0
    HARD = 1
    op = EASY
    prop = pynk.ffi.new("int*", 0)
    winflags = 0
    running = True
    flags = [ (pynk.lib.NK_WINDOW_BORDER, "Border".encode('utf-8')),
              (pynk.lib.NK_WINDOW_MOVABLE, "Movable".encode('utf-8')),
              (pynk.lib.NK_WINDOW_SCALABLE, "Scalable".encode('utf-8')),
              (pynk.lib.NK_WINDOW_CLOSABLE, "Scrollable".encode('utf-8')),
              (pynk.lib.NK_WINDOW_MINIMIZABLE, "Minimizable".encode('utf-8')),
              (pynk.lib.NK_WINDOW_TITLE, "Title".encode('utf-8')) ]

    # Initialise nuklear
    font = pynk.nkpygame.NkPygameFont(pygame.font.SysFont("Consolas", 14))
    with pynk.nkpygame.NkPygame(font) as nkpy:
        overview = Overview()

        while running:

            # Handle input.
            events = []
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                else:
                    events.append(e)
            nkpy.handle_events(events)

            # Show the demo GUI.
            if pynk.lib.nk_begin(nkpy.ctx, "Demo".encode('utf-8'), pynk.lib.nk_rect(50, 50, 300, 300), winflags):
                pynk.lib.nk_layout_row_static(nkpy.ctx, 30, 80, 1)
                if pynk.lib.nk_button_label(nkpy.ctx, "quit".encode('utf-8')):
                    running = False
                pynk.lib.nk_layout_row_dynamic(nkpy.ctx, 30, 2)
                if pynk.lib.nk_option_label(nkpy.ctx, "easy".encode('utf-8'), op == EASY): 
                    op = EASY
                if pynk.lib.nk_option_label(nkpy.ctx, "hard".encode('utf-8'), op == HARD): 
                    op = HARD
                pynk.lib.nk_layout_row_dynamic(nkpy.ctx, 22, 1)
                pynk.lib.nk_property_int(nkpy.ctx, "Compression:".encode('utf-8'), 0, prop, 100, 10, 1)
                for flag in flags:
                    pynk.lib.nk_layout_row_dynamic(nkpy.ctx, 22, 1)
                    if pynk.lib.nk_check_label(nkpy.ctx, flag[1], winflags & flag[0]): 
                        winflags |= flag[0]
                    else:
                        winflags &= ~flag[0]
            pynk.lib.nk_end(nkpy.ctx)

            # Show the built-in overview GUI.
            pynk.lib.pynk_overview(nkpy.ctx)

            # Show our version written in Python.
            overview.overview(nkpy.ctx)

            # Draw
            screen.fill((0, 0, 0))
            nkpy.render_to_surface(screen)
            pygame.display.update()

            # Clear the context for the next pass.
            pynk.lib.nk_clear(nkpy.ctx)

    # Shutdown.
    pygame.quit()
