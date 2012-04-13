Nostrils
========

A nose plugin that gathers a map of code and their covering tests so that we know what tests are affected when we change certain lines of code.

A Sample Run
------------

```bash
[master ✓] $ nosetests --with-nostrils  -s --nostrils-whitelist=sample
.....
----------------------------------------------------------------------
Ran 5 tests in 0.019s

OK
File: /home/kevin/src/nostrils/sample/worker.py
  2:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add', '/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_add', '/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add___negative']
  3:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add', '/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_add', '/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add___negative']
  6:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_subtract']
  7:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_subtract']
  10:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi']
  11:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi']
  13:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi']
```
