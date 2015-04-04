from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import zope.interface


__all__ = ['IPlugin']


class IPlugin(zope.interface.Interface):

    def activate(self):
        """
        Called at plugin activation.
        """

    def deactivate(self):
        """
        Called when the plugin is disabled.
        """
