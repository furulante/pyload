# -*- coding: utf-8 -*-

from pyload.plugin.internal.DeadHoster import DeadHoster


class BayfilesCom(DeadHoster):
    __name__    = "BayfilesCom"
    __type__    = "hoster"
    __version__ = "0.09"

    __pattern__ = r'https?://(?:www\.)?bayfiles\.(com|net)/file/(?P<ID>\w+/\w+/[^/]+)'
    __config__  = []

    __description__ = """Bayfiles.com hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Walter Purcaro", "vuolter@gmail.com")]