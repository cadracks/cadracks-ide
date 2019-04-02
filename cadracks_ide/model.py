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

r"""Model of the CadRacks IDE app"""

import sys
import logging

from atom.api import Atom
from atom.scalars import Str

logger = logging.getLogger(__name__)


class Model(Atom):
    r"""Model for the CadRacks IDE app"""
    root_folder = Str()
    selected = Str()
    code = Str()

    def set_root_folder(self, root_folder):
        r"""Set the root folder
        
        Parameters
        ----------
        root_folder : str

        """
        logger.debug("Setting the root folder")
        self.root_folder = root_folder
        sys.path.append(root_folder)
        logger.debug("Notify that root folder changed")
        self.notify("root_folder_changed", None)

    def set_selected(self, selected):
        r"""Defines which item is selected in the tree view

        Parameters
        ----------
        selected

        """
        logger.debug("Setting the selected item")
        self.selected = selected
        logger.debug("Notify that selected item changed")
        self.notify("selected_changed", None)
