# -*- coding: utf-8 -*-
# Description: rspamd netdata python.d module
# Author: Keijo Korte <git@kvak.net> (@korteke)
# SPDX-License-Identifier: GPL-3.0-or-later

from bases.FrameworkServices.UrlService import UrlService
from json import loads

# Basic plugin settings for netdata.
update_every = 10
priority = 60000
retries = 10

ORDER = ['stats',
         'actions'
        ]

CHARTS = {
    'stats': {
        'options': [None, 'Stats', 'stats', 'Stats', 'rspamd.stats', 'line'],
        'lines': [
            ['spam_count', 'Spam', 'absolute'],
            ['ham_count', 'Ham', 'absolute'],
            ['scanned', 'Scanned', 'absolute'],
            ['learned', 'Learned', 'absolute'],
        ]
    },
    'actions': {
        'options': [None, 'Actions', 'actions', 'Actions', 'rspamd.actions', 'line'],
        'lines': [
            ['action_reject', 'Reject', 'absolute'],
            ['action_softreject', 'Soft reject', 'absolute'],
            ['action_rewritesubject', 'Rewrite subject', 'absolute'],
            ['action_addheader', 'Add header', 'absolute'],
            ['action_greylist', 'Greylist', 'absolute'],
            ['action_noaction', 'No Action', 'absolute'],
            
        ]
    },
}

class Service(UrlService):
    def __init__(self, configuration=None, name=None):
        UrlService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.url = self.configuration.get('url', 'http://localhost:11334')+'/stat'

    def check(self):
        self._manager = self._build_manager()

        data = self._get_data()

        if not data:
            return None

        return True

    def _get_data(self):
        #raw_data = self._get_raw_data()
        raw_data = loads(self._get_raw_data())
        if not raw_data:
            return None

        data = dict()
        data.update({"spam_count": str(raw_data["spam_count"])})
        data.update({"ham_count": str(raw_data["ham_count"])})
        data.update({"scanned": str(raw_data["scanned"])})
        data.update({"learned": str(raw_data["learned"])})
        data.update({"action_reject": str(raw_data["actions"]["reject"])})
        data.update({"action_softreject": str(raw_data["actions"]["soft reject"])})
        data.update({"action_rewritesubject": str(raw_data["actions"]["rewrite subject"])})
        data.update({"action_addheader": str(raw_data["actions"]["add header"])})
        data.update({"action_greylist": str(raw_data["actions"]["greylist"])})
        data.update({"action_noaction": str(raw_data["actions"]["no action"])})
        return(data)