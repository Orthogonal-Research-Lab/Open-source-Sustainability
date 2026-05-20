"""


"""

import logging
import os
import sys
from multiprocessing import Process

# print(sys.path)


import pynetlogo
from pynetlogo import NetLogoLink

# Created on 1 Nov 2016
#
# .. codeauthor::jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>

__all__ = []

# logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stderr)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(" %(levelname)s - %(message)s")
ch.setFormatter(formatter)
root.addHandler(ch)


# on mac there is a stupid issue with getting the default jvm path
# this is related to some mac bug in java 8
jvm_path = '/Library/Java/JavaVirtualMachines/jdk-18.0.1.1.jdk/Contents/Home/lib/server/libjvm.dylib'
link = NetLogoLink(jvm_path=jvm_path)
# link = pynetlogo.NetLogoLink(jvm_home=jvm_home)


def run_61():
    print("trying 6.1")
    link = pynetlogo.NetLogoLink()
    model_file = os.path.join(
        link.netlogo_home, "models/Sample Models/Biology/Wolf Sheep Predation.nlogo"
    )
    print(os.path.exists(model_file))
    link.load_model(model_file)


def run_60():
    print("trying 6.0")
    link = pynetlogo.NetLogoLink(netlogo_home="/Applications/Netlogo 6.0.4")

    model_file = os.path.join(
        link.netlogo_home, "models/Sample Models/Biology/Wolf Sheep Predation.nlogo"
    )
    print(os.path.exists(model_file))
    link.load_model(model_file)


def run_63():
    print("trying 6.3")
    link = pynetlogo.NetLogoLink(netlogo_home="/Applications/NetLogo 6.3.0/NetLogo 6.3.0.app")

    model_file = os.path.join(
        link.netlogo_home, "models/Sample Models/Biology/Wolf Sheep Predation.nlogo"
    )
    print(os.path.exists(model_file))
    link.load_model(model_file)


if __name__ == "__main__":
    # p = Process(target=run_61)
    # p.start()
    # p.join()

    # p = Process(target=run_60)
    # p.start()
    # p.join()

    p = Process(target=run_63)
    p.start()
    p.join()