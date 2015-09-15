from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import errno
import os
import subprocess
import sys

isWindows = sys.platform.startswith('win32')
isLinux = sys.platform.startswith("linux")
isMaxOsX = sys.platform.startswith("darwin")

####################################################################################################
# Utility functions
####################################################################################################


class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOOT = '\033[94m'

    ENDC = '\033[0m'

# Do *not* use color when:
#  - on windows
#  - not in a terminal except if we are in Travis CI
if isWindows or (not os.environ.get("TRAVIS") and not sys.stdout.isatty()):
    bcolors.HEADER = ''
    bcolors.OKBLUE = ''
    bcolors.OKGREEN = ''
    bcolors.WARNING = ''
    bcolors.FAIL = ''
    bcolors.BOLD = ''
    bcolors.UNDERLINE = ''
    bcolors.BOOT = ''
    bcolors.ENDC = ''


def flush():
    sys.stdout.flush()
    sys.stderr.flush()


def printInfo(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.OKBLUE + "[INFO ] " + bcolors.ENDC + line)
    flush()


def printError(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.FAIL + "[ERROR] " + bcolors.ENDC + line, file=sys.stderr)
    flush()


def printSeparator(char="-", color=bcolors.OKGREEN):
    print(color + char * 79 + bcolors.ENDC)
    flush()


def printNote(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.HEADER + "[NOTE ] " + bcolors.ENDC + line)
    flush()


def printBoot(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.BOOT + "[BOOT ] " + bcolors.ENDC + line)
    flush()


def printDebug(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.BOOT + "[DEBUG] " + bcolors.ENDC + line)
    flush()


def printCmd(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.OKGREEN + "[CMD  ] " + bcolors.ENDC + line)
    flush()


def printQuestion(text):
    text = str(text)
    for line in text.split("\n"):
        print(bcolors.OKGREEN + "[???? ] " + bcolors.ENDC + line)
    flush()
    line = sys.stdin.readline()
    return line.strip()


def run(cmd, cwd=None, shell=False, extraPath=None):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    path_bkp = None
    if extraPath and not isWindows:
        # Force use shell to allow PATH environment variable propagation
        shell = True
        path_bkp = os.environ['PATH']
        os.environ['PATH'] = extraPath + ":" + os.environ['PATH']
        cmd = " ".join(cmd)
        print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " PATH set to: {}".format(os.environ['PATH']))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)
    if extraPath and path_bkp:
        os.environ['PATH'] = path_bkp


def run_output(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    s = subprocess.check_output(cmd, shell=shell, cwd=cwd)
    return str(s)


def run_nocheck(cmd, cwd=None, shell=False):
    try:
        print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
        flush()
        subprocess.check_call(cmd, shell=shell, cwd=cwd)
    except Exception as e:
        printError("Exception : {}".format(e))


def call(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD  ]" + bcolors.ENDC + " {}".format(" ".join(cmd)))
    flush()
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def run_background(cmd, cwd=None, shell=False):
    print(bcolors.OKGREEN + "[CMD (background)" + bcolors.ENDC + "] {}".format(" ".join(cmd)))
    flush()
    subprocess.Popen(cmd, cwd=cwd, shell=shell)


def mkdirs(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
