from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os
import sys
import yaml

from dictns import Namespace
from dictns import _appendToParent

from squirrel.common.i18n import _
from squirrel.common.singleton import singleton


log = logging.getLogger(__name__)


def _dumpFlat(n, parent=None):
    s = ""
    for k, v in n.items():
        me = _appendToParent(parent, k)

        def do_item(me, v):
            t = type(v).__name__
            if t == "Namespace":
                t = "dict"
            if isinstance(v, dict):
                v = Namespace(v)
                s = _dumpFlat(v, me)
            elif type(v) == list:
                s = me + " = " + str(v) + "\n"
                if len(v) > 0:
                    v = v[0]
                    s += do_item(me + "[i]", v)
            else:
                s = me + " = " + str(v) + "\n"
            return s
        s += do_item(me, v)
    return s


@singleton
class Config(object):

    def __init__(self, *args, **kwargs):
        self.cfg = Namespace(*args, **kwargs)

    def dumpFlat(self, parent=None):
        return _dumpFlat(self)

    def __getattr__(self, name):
        return getattr(self.cfg, name)


def _loadYaml(yamlpath):
    with open(yamlpath) as f:
        return yaml.load(f)


def _loadConfig(configPath):
    log.debug(_("Loading configuration: {}").format(configPath))
    cfg = _loadYaml(configPath)
    Config().unload()
    Config(cfg)


def _makeFullPath(relPath):
    if os.path.isabs(relPath):
        return relPath
    if sys.platform.startswith("win32"):
        relPath = os.path.normpath(relPath)
    backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                os.pardir,
                                                os.pardir))
    return os.path.abspath(os.path.join(backend_root, relPath))


def _makeSqlLitePath(url):
    sqlite_proto = "sqlite:///"
    if url.startswith(sqlite_proto):
        return sqlite_proto + _makeFullPath(url[len(sqlite_proto):])
    return url


def updateFullPaths():
    c = Config()
    c.frontend.root_full_path = _makeFullPath(c.frontend.root_path)
    c.frontend.doc_full_path = _makeFullPath(c.frontend.doc_path)
    c.frontend.logging_conf_full_path = _makeFullPath(c.frontend.logging_conf_path)
    c.backend.db.full_url = _makeSqlLitePath(c.backend.db.url)
    c.backend.db.full_workdir = _makeFullPath(c.backend.db.workdir)
    if sys.platform.startswith("win32"):
        c.backend.db.full_url = c.backend.db.full_url.replace("\\", "\\\\")
    c.plugins.full_default_path = _makeFullPath(c.plugins.default_path)


def dumpConfigToLogger(level="info"):
    """
    Args:
        level (str, optional): log level. info/debug/warning
    """
    assert level in {'info', 'debug', 'warning'}
    c = Config()
    getattr(log, level)("")
    getattr(log, level)(_("Listing all available keys:"))
    getattr(log, level)(c.dumpFlat())


def initializeConfig():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               os.pardir,
                                               "config.yaml"))
    log.debug("Loading configuration: {}".format(config_path))
    _loadConfig(config_path)
    updateFullPaths()
    dumpConfigToLogger()


def unloadConfig():
    Config().unload()