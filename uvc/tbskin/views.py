# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok
import megrok.pagetemplate as pt


from dolmen.forms.base import ApplicationForm
from skin import ITBSkin
from urllib import urlencode
from uvc.layout.forms.components import GroupForm, SubForm, Wizard
from uvc.layout.layout import IUVCSkin
from z3c.table.batch import BatchProvider
from z3c.table.interfaces import ITable
from zope.interface import Interface
from zope.traversing.browser import absoluteURL
from grokcore.chameleon.components import ChameleonPageTemplateFile


grok.templatedir('templates')


class FormMacros(grok.View):
    grok.context(Interface)
    template = ChameleonPageTemplateFile('templates/formtemplate.cpt')


class FormTemplate(pt.PageTemplate):
    grok.layer(ITBSkin)
    grok.view(ApplicationForm)


class SubFormTemplate(pt.PageTemplate):
    grok.layer(ITBSkin)
    pt.view(SubForm)


class GroupFormTemplate(pt.PageTemplate):
    grok.layer(ITBSkin)
    pt.view(GroupForm)


class WizardTemplate(pt.PageTemplate):
    grok.layer(ITBSkin)
    pt.view(Wizard)


class CustomBatch(BatchProvider, grok.MultiAdapter):
    grok.adapts(Interface, IUVCSkin, ITable)
    grok.name('batch')

    def renderBatchLink(self, batch, cssClass=None):
        args = self.getQueryStringArgs()
        args[self.table.prefix + '-batchStart'] = batch.start
        args[self.table.prefix + '-batchSize'] = batch.size
        query = urlencode(sorted(args.items()))
        tableURL = absoluteURL(self.table, self.request)
        idx = batch.index + 1
        css = ' class="%s"' % cssClass
        cssClass = cssClass and css or u''
        return '<li %s><a href="%s?%s"%s>%s</a><li>' % (
            cssClass, tableURL, query, cssClass, idx)

    def render(self):
        self.update()
        res = []
        append = res.append
        idx = 0
        lastIdx = len(self.batchItems)
        for batch in self.batchItems:
            idx += 1
            # build css class
            cssClasses = []
            if batch and batch == self.batch:
                cssClasses.append('active')
            if idx == 1:
                cssClasses.append('first')
            if idx == lastIdx:
                cssClasses.append('last')

            if cssClasses:
                css = ' '.join(cssClasses)
            else:
                css = None

            # render spaces
            if batch is None:
                append(self.batchSpacer)
            elif idx == 1:
                # render first
                append(self.renderBatchLink(batch, css))
            elif batch == self.batch:
                # render current
                append(self.renderBatchLink(batch, css))
            elif idx == lastIdx:
                # render last
                append(self.renderBatchLink(batch, css))
            else:
                append(self.renderBatchLink(batch))
        return u'<ul>%s</ul>' % (''.join(res))
