import os
import os.path
import json
from collections import defaultdict

CWD = os.getcwd()


class TraceCollector(object):
    def __init__(self, whitelist=[]):
        self._currentid = 0
        # { testid : test_case_name }
        self._testids = {}
        # { filename : { lineno : [testid] }}
        self._data = defaultdict(
            lambda: defaultdict(
                lambda: set([])
            )
        )
        self._whitelist = whitelist
        self._current_test = None

    @property
    def current_test(self):
        return self._current_test

    @current_test.setter
    def current_test(self, value):
        # pretend contention doesn't exist
        self._currentid += 1
        # switching the context to the new test
        self._current_test = value
        self._testids[self._currentid] = self._test_case_name(self._current_test)

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
        self._data[filename][lineno].add(self._currentid)

    def save(self):
        with open('.nostrils', 'w') as f:
            json.dump(self._data, f, default=lambda x: list(x))
        with open('.nostrils-ids', 'w') as f:
            json.dump(self._testids, f)

    def _test_case_name(self, test_case):
        if hasattr(test_case, 'id'):
            return test_case.id()
        elif hasattr(test_case, 'address'):
            return "%s:%s.%s" % test_case.address()
        else:
            raise ValueError(
                'Neither `id` or `address` is present for the test case %r'
                % test_case)

    def get_test_case_name_by_id(self, testid):
        return self._testids[testid]
