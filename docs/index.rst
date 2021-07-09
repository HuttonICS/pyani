.. pyani documentation master file, created by
   sphinx-quickstart on Fri Aug 11 13:27:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================================
Welcome to ``pyani``'s documentation!
=====================================

-----------------
Build information
-----------------

.. image:: https://circleci.com/gh/widdowquinn/pyani/tree/development.svg?style=shield
    :target: https://circleci.com/gh/widdowquinn/pyani/tree/development
.. image:: https://img.shields.io/codecov/c/github/widdowquinn/pyani.svg?style=flat-square
    :target: https://codecov.org/widdowquinn/pyani
.. image:: https://api.codacy.com/project/badge/Grade/f3e56b2bf118471aabf09514a3e6af75
    :target: https://www.codacy.com/app/widdowquinn/pyani?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=widdowquinn/pyani&amp;utm_campaign=Badge_Grade
.. image:: https://www.codefactor.io/repository/github/widdowquinn/pyani/badge
    :target: https://www.codefactor.io/repository/github/widdowquinn/pyani
.. image:: https://readthedocs.org/projects/pyani/badge/?version=latest
    :target: https://pyani.readthedocs.io/en/latest/?badge=latest
.. image:: https://img.shields.io/librariesio/sourcerank/pypi/pyani.svg?logo=koding&logoColor=white
    :target: https://libraries.io/pypi/pyani


------------------------------
``PyPI`` version and Licensing
------------------------------

.. image:: https://img.shields.io/pypi/v/pyani.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pyani
.. image:: https://img.shields.io/pypi/l/pyani.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pyani
.. image:: https://img.shields.io/pypi/format/pyani
    :target: https://pypi.org/project/pyani/
.. image:: https://img.shields.io/pypi/pyversions/pyani
    :target: https://pypi.org/project/pyani/
.. image:: https://img.shields.io/pypi/dm/pyani
    :target: https://pypi.org/project/pyani/

-----------------
``conda`` version
-----------------

.. image:: https://anaconda.org/bioconda/pyani/badges/version.svg?style=flat-square
    :target: https://anaconda.org/bioconda/pyani
.. image:: https://anaconda.org/bioconda/pyani/badges/latest_release_date.svg?style=flat-square
     :target: https://anaconda.org/bioconda/pyani
.. image:: https://anaconda.org/bioconda/pyani/badges/installer/conda.svg?style=flat-square
     :target: https://conda.anaconda.org/bioconda
.. image:: https://anaconda.org/bioconda/pyani/badges/downloads.svg?style=flat-square
     :target: https://anaconda.org/bioconda/pyani
.. image:: https://anaconda.org/bioconda/pyani/badges/platforms.svg?style=flat-square
     :target: https://anaconda.org/bioconda/pyani

If you're feeling impatient, please head over to the :ref:`QuickStart Guide <pyani-quickstart>`

-----------
Description
-----------

``pyani`` is a program and Python package that provides support for calculating average nucleotide identity (ANI) and related measures for whole genome comparisons, and for rendering relevant graphical and tabular summary output. Where available, it natively takes advantage of multicore systems, and can integrate with `SGE or OGE-compatible`_ job schedulers to manage the computationally-heavy sequence comparisons.

Installing the ``pyani`` Python package also installs the program ``pyani``, which enables command-line based analysis of genomes. Results are stored in a private `SQLite3`_ database local to the machine, which permits addition of genomes to a previous analysis without having to recalculate all previously-performed comparisons, facilitating incremental  analysis and visualisation, and enabling incremental maintenance of results for a taxonomic group as new genome sequences become available.

If you use ``pyani`` in your work, we would be grateful if you could please cite us as indicated on the :ref:`Citations <pyani-citations>` page.

----------------------------------------------
Reporting problems and requesting improvements
----------------------------------------------

If you encounter bugs or errors, or would like to suggest ways in which ``pyani`` can be improved, please raise a new issue at the ``pyani`` `GitHub issues page`_.

If you'd like to fix a bug or make an improvement yourself, contributions are welcomed, and guidelines on how to do this can be found at the :ref:`pyani-contributing` documentation page.




.. toctree::
   :maxdepth: 2
   :caption: Contents:

   citations
   about
   quickstart
   requirements
   installation
   basic_use
   examples
   subcommands
   scheduler
   testing
   contributing
   licensing
   api/pyani

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. _GitHub issues page: https://github.com/widdowquinn/pyani/issues
.. _SGE or OGE-compatible: http://gridscheduler.sourceforge.net/
.. _SQLite3: https://www.sqlite.org/index.html
