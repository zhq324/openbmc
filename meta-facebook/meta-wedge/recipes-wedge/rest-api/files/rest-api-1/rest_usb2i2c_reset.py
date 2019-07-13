#!/usr/bin/env python
#
# Copyright 2014-present Facebook. All Rights Reserved.
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

import subprocess

# Endpoint for resetting usb-to-i2c device t9591420
def set_usb2i2c():
    p = subprocess.Popen('source /usr/local/fbpackages/utils/ast-functions;'
                         'gpio_set USB_BRDG_RST 0 && usleep 50000 && \
                         gpio_set USB_BRDG_RST 1',
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    rc = p.returncode

    if rc < 0:
        status = ' failed with returncode = ' + str(rc) + ' and error ' + err
    else:
        status = ' done '

    return { "status" : 'usb to i2c device reset' + status }
