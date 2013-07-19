# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import uvclight
import zope.interface
from cromlech.browser.interfaces import ITypedRequest

class ITBSkinLayer(ITypedRequest):
    pass


class Layout(uvclight.Layout):
    uvclight.context(zope.interface.Interface)
    uvclight.layer(ITBSkinLayer)
    uvclight.name('uvc.layout')

    template = uvclight.get_template('layout.cpt', __file__)
