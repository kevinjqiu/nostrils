Nostrils
========

A nose plugin that gathers a map of code and their covering tests so that we know what tests are affected when we change certain lines of code.

A Sample Run
------------

```bash
[master ✓] $ nosetests -s --with-nostrils --nostrils-whitelist=sample
.....
----------------------------------------------------------------------
Ran 5 tests in 0.026s

OK
File: /Users/kevin/src/nostrils/sample/worker.py
  2:     z = x + y
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_add
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add___negative
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add


  3:     return z
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_add
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add___negative
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_add


  6:     z = x - y
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_subtract


  7:     return z
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.test_subtract


  10:     z = x \
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi


  11:         * y
    * /Users/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi


  13:['/home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi']
```
