#!/usr/bin/env python
#
# Copyright 2015-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#

from ctypes import *

lpal_hndl = CDLL("libpal.so")

def pal_get_fru_list():
    frulist = create_string_buffer(128)
    ret = lpal_hndl.pal_get_fru_list(frulist)
    if ret:
        return None
    else:
        return frulist.value

def pal_set_key_value(key):
    value = '1'
    lpal_hndl.pal_set_key_value(key, value)
