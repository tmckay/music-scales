"""Draws a fretboard image for adding notes"""
from math import pi as M_PI

import cairo

class FretboardDrawer:
    """Draws a base fretboard image on which notes can be added"""

    def __init__(self,
                 width=800, height=800,
                 bgcolor=(1,1,1), fgcolor=(0,0,0),
                 num_strings=6, num_frets=6):
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.num_strings = num_strings
        self.num_frets = num_frets

        self._draw_blank_fretboard()

    def _draw_blank_fretboard(self):
        """Draws an image with an empty fretboard"""
        surface = cairo.SVGSurface(
            'fretboard.svg',
            self.width,
            self.height
        )
        context = cairo.Context(surface)
        context.scale(self.width, self.height)

        # set background color
        context.rectangle(0, 0, self.width, self.height)
        context.set_source_rgb(*self.bgcolor)
        context.fill()

        # draw guitar strings
        context.set_source_rgb(*self.fgcolor)
        context.set_line_width(0.02)
        string_gap = 1 / self.num_strings
        for line_idx in range(self.num_strings):
            y_value = string_gap * line_idx + string_gap / 2
            context.move_to(0, y_value)
            context.line_to(1, y_value)
        context.stroke()

        # draw guitar frets
        fret_gap = 1 / self.num_frets
        for fret_idx in range(self.num_frets):
            x_value = fret_gap * fret_idx + fret_gap / 2
            context.move_to(x_value, fret_gap / 2)
            context.line_to(x_value, 1 - fret_gap / 2)
        context.stroke()

        self.context = context
        self.surface = surface

    def add_note(self, string: int, fret: int,
                 first_fret: int, root: bool = False):
        """
        Args:
            string: string number to draw note on
            fret: fret number to draw note on
            first fret: first fret of scale
            root: whether it's a root note of scale
        """
        # calculate the left to right spacing
        note_gap = 1 / self.num_frets


        # determine the x coordinate of dot
        # note_gap * 2 <-- starts us two frets in
        # (note_gap * (fret - first_fret)) <-- difference between first
        #                                      fret and this fret
        x_coord = note_gap * 2 + (note_gap * (fret - first_fret))

        # calculate the gap between strings
        string_gap = 1 / self.num_strings

        # calculate the top to bottom spacing
        string_depth = abs(string - self.num_strings + 1)

        # determine y coordinate
        # string_gap / 2 <-- we start a half a string gap from the top
        # string_gap * string_depth <-- how far down is our string
        y_coord = string_gap / 2 + string_gap * string_depth

        # draw solid circle on string and in the middle of fret
        self.context.arc(
            x_coord,
            y_coord,
            0.05,
            0.0,
            2.0 * M_PI
        )
        self.context.fill()

        # draw circle around root notes
        if root:
            self.context.set_line_width(0.01)
            self.context.arc(
                x_coord,
                y_coord,
                0.07,
                0.0,
                2.0 * M_PI
            )
        self.context.stroke()

    def add_label(self, text):
        self.context.select_font_face('Sans')
        self.context.set_font_size(0.05)
        self.context.move_to(1 / self.num_frets * 1.75, 0.06)
        self.context.show_text(text)

    def save(self, path):
        # save image
        self.surface.write_to_png(path)
