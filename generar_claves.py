# -*- coding: utf-8 -*-

import os
import binascii


def generar():
    return binascii.hexlify(os.urandom(8))

x = generar()
print(x)