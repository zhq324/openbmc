#!/usr/bin/env python

from ctypes import *
import json
import ssl
import socket
import os
from node_api import get_node_api
from node_fcb import get_node_fcb
from node_pdpb import get_node_pdpb
from node_peb import get_node_peb
from node_fans import get_node_fans
from node_fruid import get_node_fruid
from node_sensors import get_node_sensors
from node_logs import get_node_logs
from node_flash import get_node_flash
from node_bmc import get_node_bmc
from node_health import get_node_health
from node_identify import get_node_identify
from tree import tree
from pal import *

# Initialize Platform specific Resource Tree
def init_plat_tree():

    # Create /api end point as root node
    r_api = tree("api", data = get_node_api())

    # Add /api/fcb to represent fan control board
    r_fcb = tree("fcb", data = get_node_fcb())
    r_api.addChild(r_fcb)
    # Add /api/pdpb to represent fan control board
    r_pdpb = tree("pdpb", data = get_node_pdpb())
    r_api.addChild(r_pdpb)
    # Add /api/peb to represent fan control board
    r_peb = tree("peb", data = get_node_peb())
    r_api.addChild(r_peb)

    #Add /api/fcb/fans end point
    r_temp = tree("fans", data = get_node_fans())
    r_fcb.addChild(r_temp)
    #Add /api/fcb/fruid end point
    r_temp = tree("fruid", data = get_node_fruid("fcb"))
    r_fcb.addChild(r_temp)
    #Add /api/fcb/sensors end point
    r_temp = tree("sensors", data = get_node_sensors("fcb"))
    r_fcb.addChild(r_temp)
    #Add /api/fcb/logs end point
    r_temp = tree("logs", data = get_node_logs("fcb"))
    r_fcb.addChild(r_temp)

    #Add /api/pdpb/sensors end point
    r_temp = tree("sensors", data = get_node_sensors("pdpb"))
    r_pdpb.addChild(r_temp)
    #Add /api/pdpb/flash end point
    r_temp = tree("flash", data = get_node_flash())
    r_pdpb.addChild(r_temp)
    #Add /api/pdpb/fruid end point
    r_temp = tree("fruid", data = get_node_fruid("pdpb"))
    r_pdpb.addChild(r_temp)
    #Add /api/pdpb/logs end point
    r_temp = tree("logs", data = get_node_logs("pdpb"))
    r_pdpb.addChild(r_temp)

    #Add /api/peb/fruid end point
    r_temp = tree("fruid", data = get_node_fruid("peb"))
    r_peb.addChild(r_temp)
    #Add /api/peb/sensors end point
    r_temp = tree("sensors", data = get_node_sensors("peb"))
    r_peb.addChild(r_temp)
    #Add /api/peb/bmc end point
    r_temp = tree("bmc", data = get_node_bmc())
    r_peb.addChild(r_temp)
    #Add /api/peb/health end point
    r_temp = tree("health", data = get_node_health())
    r_peb.addChild(r_temp)
    #Add /api/peb/identify end point
    r_temp = tree("identify", data = get_node_identify("peb"))
    r_peb.addChild(r_temp)
    #Add /api/peb/logs end point
    r_temp = tree("logs", data = get_node_logs("peb"))
    r_peb.addChild(r_temp)

    return r_api

