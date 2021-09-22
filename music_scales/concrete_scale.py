"""Concrete scale on a fretboard"""
from math import pi as M_PI
from typing import List, Tuple

import cairo

from .note import Note


class ConcreteScale:
    """A representation of a scale on a fretboard with
    actual string and frets"""

    def __init__(self, name: str, scale_def: List[Tuple[int, int, Note]]):
        """
        Args:
            name: name of the scale
            scale_def: definition of a scale with format
                       List[Tuple[<guitar-string>, <fret>, Note]]
        """
        self.name = name
        self.scale_def = scale_def

    def as_image(self, width=800, height=800):
        """Return image of scale on a fretboard"""

        def add_note_to_fretboard(string: int, fret: int, first_fret: int):
            note_gap = 1 / 6.0
            string_depth = abs(string - 5)
            context.arc(
                note_gap * 2 + (note_gap * (fret - first_fret)),
                string_gap / 2 + string_gap * string_depth,
                0.05,
                0.0,
                2.0 * M_PI
            )
            context.fill()
            context.stroke()

        with cairo.SVGSurface("concrete_scale.svg", width, height) as surface:
            context = cairo.Context(surface)
            context.scale(width, height)

            # set background color
            context.rectangle(0, 0, width, height)
            context.set_source_rgb(1, 1, 1)
            context.fill()

            # draw guitar strings
            context.set_source_rgb(0, 0, 0)
            context.set_line_width(0.02)
            string_gap = 1 / 6.0
            for line_idx in range(6):
                y_value = string_gap * line_idx + string_gap / 2
                context.move_to(0, y_value)
                context.line_to(1, y_value)
            context.stroke()

            # draw guitar frets
            fret_gap = 1 / 6.0
            for fret_idx in range(6):
                x_value = fret_gap * fret_idx + fret_gap / 2
                context.move_to(x_value, fret_gap / 2)
                context.line_to(x_value, 1 - fret_gap / 2)
            context.stroke()

            # show dots on strings for scale
            first_fret = self.scale_def[0][1]
            for note in self.scale_def:
                add_note_to_fretboard(note[0], note[1], first_fret)

            # save image
            surface.write_to_png(f'/images/{self.name}.png')
