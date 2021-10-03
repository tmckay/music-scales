"""Concrete scale on a fretboard"""
from math import pi as M_PI
from typing import List, Tuple

import cairo

from .note import Note
from .utils import to_ordinal


class ConcreteScale:
    """A representation of a scale on a fretboard with
    actual string and frets"""

    def __init__(self, name: str, key: str, scale_def: List[Tuple[int, int, Note]]):
        """
        Args:
            name: name of the scale
            scale_def: definition of a scale with format
                       List[Tuple[<guitar-string>, <fret>, Note]]
        """
        self.name = name
        self.key = key
        self.scale_def = scale_def

    @property
    def path_safe_key(self):
        """Returns a key that is path safe for saving images"""
        return str(self.key).split('/')[0]

    def _get_blank_fretboard_image(self, width, height):
        """Draws an image with an empty fretboard"""
        surface = cairo.SVGSurface("concrete_scale.svg", width, height)
        context = cairo.Context(surface)
        context.scale(width, height)

        # set background color
        context.rectangle(0, 0, width, height)
        context.set_source_rgb(1, 1, 1)
        context.fill()

        # draw guitar strings
        context.set_source_rgb(0, 0, 0)
        context.set_line_width(0.02)
        string_gap = 1 / 6.0  # TODO Parametrize num of strings
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

        return context, surface

    def as_image(self, width=800, height=800):
        """Return image of scale on a fretboard"""

        def add_note_to_fretboard(string: int, fret: int, first_fret: int, root: bool = False):
            note_gap = 1 / 6.0
            string_depth = abs(string - 5)
            x_coord = note_gap * 2 + (note_gap * (fret - first_fret))
            string_gap = 1 / 6.0  # TODO Parametrize num of strings
            y_coord = string_gap / 2 + string_gap * string_depth
            context.arc(
                x_coord,
                y_coord,
                0.05,
                0.0,
                2.0 * M_PI
            )
            context.fill()

            # draw circle around root notes
            if root:
                context.set_line_width(0.01)
                context.arc(
                    x_coord,
                    y_coord,
                    0.07,
                    0.0,
                    2.0 * M_PI
                )
            context.stroke()

        context, surface = self._get_blank_fretboard_image(width, height)

        # show dots on strings for scale
        first_fret = self.scale_def[0][1]
        for idx, note in enumerate(self.scale_def):
            # label fret
            if idx == 0:
                context.select_font_face('Sans')
                context.set_font_size(0.05)
                context.move_to(1 / 6.0 * 1.75, 0.06)
                ordinal = to_ordinal(note[1])
                context.show_text(f'{ordinal} fret')
            add_note_to_fretboard(
                note[0],
                note[1],
                first_fret,
                idx in (0, len(self.scale_def)-1)
            )

        # save image
        surface.write_to_png(f'/images/{self.name}_{self.path_safe_key}.png')
