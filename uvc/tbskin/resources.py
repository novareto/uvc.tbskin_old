# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import grokcore.component as grok

from zope.interface import Interface
from dolmen.viewlet import Viewlet
from fanstatic import Library, Resource
from js.bootstrap import bootstrap_js, bootstrap_responsive_css


library = Library('nva.tbskin', 'static')
main_css = Resource(library, 'main.css', depends=[bootstrap_responsive_css])
main_js = Resource(library, 'main.js', depends=[bootstrap_js,])


class TBSkinViewlet(Viewlet):
    grok.context(Interface)
    resources = [main_css, main_js]

    def update(self):
        [x.need() for x in self.resources]
