# coding: utf-8
import json
from django.conf import settings
from myproject.responseHooks import is_mobile_terminal


class SetTerminalTypeMiddleware(object):
    def process_request(self, request):
        t_type = u'pc'
        client = request.GET.get('client')
        if client == 'mobile':
            request.session['client_type'] = 'mobile'
        elif client == 'pc':
            request.session['client_type'] = 'pc'

        if 'client_type' in request.session:
            if request.session['client_type'] == 'mobile':
                t_type = u'mobile'
        else:
            try:
                if is_mobile_terminal(request):
                    t_type = u'mobile'
            except:
                pass
        request.terminal_type = t_type
        request.site_name = getattr(settings, 'SITE_NAME', 'sw')
        return None

    def process_response(self, request, response):
        if hasattr(request, 'searchQuery'):
            searchquery = request.searchQuery
            if searchquery is not None:
                response.set_cookie('cachequery', json.dumps(searchquery))
        return response