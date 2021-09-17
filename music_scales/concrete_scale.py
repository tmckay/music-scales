"""Concrete scale on a fretboard"""
from typing import List, Tuple

import cairo

from .note import Note


class ConcreteScale:
    """A representation of a scale on a fretboard with
    actual string and frets"""

    def __init__(self, scale_def: List[Tuple[int, int, Note]]):
        """
        Args:
            scale_def: definition of a scale with format
                       List[Tuple[<guitar-string>, <fret>, Note]]
        """
        self.scale_def = scale_def

    def as_image(self, width=200, height=200):
        """Return image of scale on a fretboard"""
        print('creating a fretboard image')
        with cairo.SVGSurface("concrete_scale.svg", width, height) as surface:
            context = cairo.Context(surface)
            context.scale(width, height)
            context.move_to(0, 0.1)
            context.line_to(1, 0.1)
            surface.write_to_png('/images/example.png')
            """
            x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
            x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
            context.scale(width, height)
            context.set_line_width(0.04)
            context.move_to(x, y)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()
            context.set_source_rgba(1, 0.2, 0.2, 0.6)
            context.set_line_width(0.02)
            context.move_to(x, y)
            context.line_to(x1, y1)
            context.move_to(x2, y2)
            context.line_to(x3, y3)
            context.stroke()
            """
