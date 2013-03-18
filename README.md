Nostrils
========

A [nose](https://github.com/nose-devs/nose) plugin that gathers a map of lines of code and their covering tests so that we know what tests are affected when we change certain lines of code. Currently this is a proof of concept.

Why?
----

Unit tests are an integral part of agile development. When a project gets big, unit tests take longer and it's counter-productive having to wait for minutes to get feedback for your latest code change. Running all tests whenever there's a code change is unnecessary because most your code changes aren't likely to affect all your tests. The Nostrils project aims to find out which tests are affected by your code changes by building a map of lines of code and their covering tests.


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


  13:     return z
    * /home/kevin/src/nostrils/test/test_worker.py:test.test_worker.TestFoo.test_multi
```

TODO
====

* A GUI app for viewing test coverage data.
