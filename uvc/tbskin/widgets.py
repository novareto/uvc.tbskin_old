# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import grok

from skin import ITBSkin 
from zope.interface import Interface
from zeam.form.base import interfaces
from zeam.form.base.widgets import ActionWidget
from zeam.form.ztk.widgets.choice import RadioFieldWidget, ChoiceSchemaField


grok.templatedir('templates')


class UvcRadioFieldWidget(RadioFieldWidget):
    """ Simple Override for removing <br> between choices
    """
    grok.adapts(ChoiceSchemaField, Interface, ITBSkin)


class ActionWidget(ActionWidget):
    grok.adapts(
        interfaces.IAction,
        interfaces.IFieldExtractionValueSetting,
        ITBSkin)

    def htmlClass(self):
        return 'action btn'
