#!/usr/bin/python3
# FFabric script (based on the file 3-deploy_web_static.py) that deletes
#  out-of-date archives,using the function do_clean.

import os
from fabric.api import *

env.hosts = ['54.160.117.237', '100.25.31.84']  # <IP web-01>, <IP web-02>


def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    nbr = 1 if int(number) == 0 else int(nbr)

    archive = sorted(os.listdir("versions"))
    [archive.pop() for i in range(nbr)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archive]

    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [a for a in archives if "web_static_" in a]
        [archive.pop() for i in range(nbr)]
        [run("rm -rf ./{}".format(a)) for a in archive]
