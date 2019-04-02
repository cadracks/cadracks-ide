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

r"""Widgets used in various places of the ui"""

import wx
import wx.lib.buttons

from cadracks_ide.utils import path_to_file


class OkBtn(wx.lib.buttons.GenBitmapTextButton):
    r"""A reusable ok button with a bitmap"""
    def __init__(self, parent, label="Ok"):
        img = wx.Bitmap(path_to_file(__file__, "icons/dialog-ok-apply.png"))
        super(OkBtn, self).__init__(parent, wx.ID_OK, img, label)


class CloseBtn(wx.lib.buttons.GenBitmapTextButton):
    r"""A reusable close button with a bitmap"""
    def __init__(self, parent, label="Close"):
        img = wx.Bitmap(path_to_file(__file__, "icons/dialog-cancel.png"))
        super(CloseBtn, self).__init__(parent, wx.ID_CANCEL, img, label=label)
