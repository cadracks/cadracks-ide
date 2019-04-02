# coding: utf-8

# Copyright 2018-2019 Guillaume Florent

# This file is part of cadracks-ide.
#
# cadracks-ide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# cadracks-ide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cadracks-ide.  If not, see <https://www.gnu.org/licenses/>.

r"""Sequences used for visualization"""

import sys

colors = ((34, 45, 90),  # dark blue
          (255, 136, 64),  # light orange
          (0, 184, 255),  # light blue
          (204, 63, 20),  # orange
          (255, 0, 0),  # red
          (0, 255, 0),  # green
          (61, 79, 153),  # medium blue
          (233, 90, 154),  # pink
          (170, 143, 104),  # brown
          (180, 212, 79),  # lime
          (169, 169, 169),  # gray
          (81, 179, 157))  # light green


def color_from_sequence(index, sequence_name=colors):
    r"""Get a color from a color sequence
    
    Parameters
    ----------
    index : int
    sequence_name : str
        Sequence name

    Returns
    -------
    tuple of 3 ints (RGB)

    """
    sequence = getattr(sys.modules[__name__], sequence_name)
    return sequence[index % len(sequence)]
