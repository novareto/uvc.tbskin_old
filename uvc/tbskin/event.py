# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

from zope.interface import alsoProvides
from grokcore.component import subscribe
from cromlech.browser.interfaces import IPublicationBeginsEvent
from uvc.tbskin.skin import ITBSkinLayer


@subscribe(IPublicationBeginsEvent)
def markRequest(event):
    alsoProvides(event.request, ITBSkinLayer)
