#!/usr/bin/env python

from subprocess import *
from node import node
from pal import *

class identifyNode(node):
    def __init__(self, name, info = None, actions = None):
        self.name = name

        if info == None:
            self.info = {}
        else:
            self.info = info
        if actions == None:
            self.actions = []
        else:
            self.actions = actions

    def getInformation(self):
        identify_status=""
        data = Popen('cat /mnt/data/kv_store/system_identify', \
                            shell=True, stdout=PIPE).stdout.read()
        identify_status = data.strip('\n')
        info = {
                "Status of identify LED": identify_status
        }
               
        return info

    def doAction(self, data):
        if data["action"] == "on":
            cmd = '/usr/bin/fpc-util --identify on'
            data = Popen(cmd, shell=True, stdout=PIPE).stdout.read()
            if data.startswith( 'Usage' ):
                res = 'failure'
            else:
                res = 'success'
        elif data["action"] == "off":
            cmd = '/usr/bin/fpc-util --identify off'
            data = Popen(cmd, shell=True, stdout=PIPE).stdout.read()
            if data.startswith( 'Usage' ):
                res = 'failure'
            else:
                res = 'success'
        else:
            res = 'not support this action'

        result = { "result": res }

        return result
    
def get_node_identify(name):
    actions = [ "on", "off" ]
    return identifyNode(name = name, actions = actions)
