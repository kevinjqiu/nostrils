import os
import os.path
import json
from collections import defaultdict

CWD = os.getcwd()

class TraceCollector(object):

    def __init__(self, whitelist=[]):
        # { filename : { lineno : [test_case_name] }}
        self._data = defaultdict(
            lambda : defaultdict(
                lambda : set([])
            )
        )
        self._whitelist = whitelist

    def should_collect(self, frame):
        if self._whitelist == '*':
            return True

        filename = frame.f_code.co_filename

        for folder in self._whitelist:
            if filename.startswith(os.path.join(CWD, folder)):
                return True

        return False

    def collect(self, frame):
        filename, lineno = frame.f_code.co_filename, frame.f_lineno
        if self.should_collect(frame):
            testid = "%s:%s.%s" % self._current_test.address()
            self._data[filename][lineno].add(testid)

    def save(self):
        with open('.nostrils', 'w') as f:
            json.dump(self._data, f, default=lambda x : list(x))
