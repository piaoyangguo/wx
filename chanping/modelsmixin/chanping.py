__author__ = 'Administrator'
from django.db import models

class productMixin(object):
    @models.permalink
    def get_absolute_url(self):
        return ('chanping:chanpingDetail', (), {'pk': self.id})


class newMixin(object):
    # @models.permalink
    # def get_absolute_url(self):
    #     return ('new:newsDetail', (), {'pk': self.id})
    @models.permalink
    def get_absolute_url(self):
        return ('new:newsDetail', (), {'pk': self.id})