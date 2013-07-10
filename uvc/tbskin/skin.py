# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok
import zope.security.management


from grokcore.traverser import Traverser
from megrok import layout
from uvc.layout.layout import IUVCSkin
from zope.component.hooks import setSite, getSite
from zope.container.interfaces import IContainer
from zope.interface import Interface
from zope.publisher.interfaces import browser
from zope.publisher.skinnable import setDefaultSkin
from zope.traversing.browser import absoluteURL


grok.templatedir('templates')


class ITBSkinLayer(grok.IDefaultBrowserLayer):
    pass


class ITBSkin(ITBSkinLayer, IUVCSkin):
    grok.skin('tbskin')


class Layout(layout.Layout):
    grok.context(Interface)
    grok.layer(ITBSkinLayer)
    grok.name('uvc.layout')

    def update(self):
        self.base = absoluteURL(self.context, self.request)
        if IContainer.providedBy(self.context) and self.base[:-1] != '/':
            self.base = self.base + '/'


### Needed For Baseregisty
#@grok.subscribe(grok.IApplication, grok.IBeforeTraverseEvent)
#def setSkin(app, event=None):
#    if getSite() != app:
#        setSite(app)
#    request = zope.security.management.getInteraction().participations[0]
#    setDefaultSkin(request)
#
#
#class appTraverser(Traverser):
#    grok.context(grok.IApplication)
#
#    def traverse(self, name):
#        setSkin(self.context)
#        return self.context.get(name)

