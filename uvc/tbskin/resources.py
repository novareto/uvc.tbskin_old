# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import uvclight
import uvc.layout.interfaces

from zope.interface import Interface

from fanstatic import Library, Resource
from uvc.tbskin.skin import ITBSkinLayer
from uvc.layout.slots.interfaces import IRenderable
from js.bootstrap import bootstrap_js, bootstrap_responsive_css
from cromlech.browser.directives import request


library = Library('nva.tbskin', 'static')
main_css = Resource(library, 'main.css', depends=[bootstrap_responsive_css])
main_js = Resource(library, 'main.js', depends=[bootstrap_js])


class TBSkinViewlet(uvclight.Viewlet):
    uvclight.implements(IRenderable)
    uvclight.context(Interface)
    uvclight.viewletmanager(uvc.layout.interfaces.IHeaders)
    request(ITBSkinLayer)
    resources = [main_css, main_js]

    def update(self):
        import pdb; pdb.set_trace()
        [x.need() for x in self.resources]

    def render(self):
        return u"HALLO WELT"
