==============
 @public NEWS
==============

2.3 (2021-04-13)
================
* Do type hinting the right way. (GL#10)

2.2 (2021-04-13)
================
* ``public()`` and ``private()`` can't be correctly type annotated, so the
  type hints on these two functions have been removed.  The ``ModuleAware``
  was also removed.  (GL#10)
* Added a ``py.typed`` file to satisfy type checkers.  (GL#9)
* Fixed a documentation cross-reference bug.

2.1.3 (2021-02-15)
==================
* I `blue <https://blue.readthedocs.io/en/latest/>`_ it!

2.1.2 (2021-01-01)
==================
* Update copyright years.
* Include ``test/__init__.py`` and ``docs/__init__.py`` (GL#9)

2.1.1 (2020-10-22)
==================
* Rename top-level tests/ directory to test/ (GL#8)

2.1 (2020-10-21)
================
* Clean up some typing problems.
* Reorganized docs and tests out of the code directory (GL#7).
* Fix the Windows CI tests.

2.0 (2020-07-27)
================
* Drop Python 3.4 and 3.5; add Python 3.8 and 3.9.
* The C implementation is removed. (GL#4)
* Added an ``@private`` decorator (GL#3)
* Build and test on Windows in addition to Linux.
* Fix the doctests so that they actually run and pass!
* Add type annotations and API reference documentation.
* Internal improvements and modernizations.

1.0 (2017-09-15)
================
* 1.0 release.
* Documentation improvements.

0.5 (2016-12-14)
================
* Fix MANIFEST.in inclusion of the src directory for the C extension.

0.4 (2016-11-28)
================
* Add Python 3.6 support.
* Make building the C extension optional, for environments without a C
  compiler.

0.3 (2016-05-25)
================
* Raise ``ValueError`` when ``__all__`` isn't a list (or subclass) instance.

0.2 (2016-05-22)
================
* Documentation updates based on initial feedback.
* Some minor test suite clean up.

0.1 (2016-05-09)
================
* Initial release.
