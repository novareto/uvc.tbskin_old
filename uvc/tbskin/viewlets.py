# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok
import uvc.layout 

from skin import ITBSkinLayer
from dolmen.app.breadcrumbs import crumbs
from uvc.layout.viewlets.flashmessages import FlashMessages

grok.templatedir('templates')


class Breadcrumbs(crumbs.Breadcrumbs):
    grok.layer(ITBSkinLayer)
    grok.viewletmanager(uvc.layout.interfaces.IAboveContent)
    grok.order(20)


class FlashMessages(FlashMessages):
    grok.layer(ITBSkinLayer)
    grok.viewletmanager(uvc.layout.interfaces.IAboveContent)
    grok.order(30)
