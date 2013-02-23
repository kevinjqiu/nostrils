import os
import os.path
import sqlite3
# from collections import defaultdict

CWD = os.getcwd()


SCHEMATA = [
    'CREATE TABLE tests ('
    '  id INTEGER AUTO_INCREMENT,'
    '  test_case_name VARCHAR(255),'
    '  PRIMARY KEY (id));',
    'CREATE TABLE coverage ('
    '  id INTEGER AUTO_INCREMENT,'
    '  filename VARCHAR(255),'
    '  lineno INTEGER,'
    '  test_id INTEGER,'
    '  PRIMARY KEY (id),'
    '  FOREIGN KEY(test_id) REFERENCES tests(id));',
]


conn = sqlite3.connect('nostrils.db')


def create_db():
    for stmt in SCHEMATA:
        conn.execute(stmt)


def commit():
    conn.commit()


def add_test(test_case_name):
    cursor = conn.execute(
        'INSERT INTO tests(test_case_name) VALUES(?)', (test_case_name,))
    return cursor.lastrowid


def add_coverage(filename, lineno, test_id):
    cursor = conn.execute(
        'INSERT INTO coverage(filename, lineno, test_id) VALUES(?, ?, ?)', (
            filename, lineno, test_id))
    return cursor.lastrowid


class TraceCollector(object):

    def __init__(self, whitelist=[]):
        self._currentid = 0
        self._testids = {}
        self._whitelist = whitelist
        self._current_test = None

    @property
    def current_test(self):
        return self._current_test

    @current_test.setter
    def current_test(self, value):
        test_case_name = self._test_case_name(value)
        self._current_test = value
        testid = add_test(test_case_name)
        self._testids[test_case_name] = testid

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
            test_case_name = self._test_case_name(self._current_test)
            add_coverage(
                filename, lineno, self._testids[test_case_name])

    def save(self):
        commit()

    def _test_case_name(self, test_case):
        return "%s:%s.%s" % test_case.address()

    def get_test_case_name_by_id(self, testid):
        return self._testids[testid]
