Install
=======

Using PyPI and pip
------------------

::

    $ (sudo) pip install pygments-style-lofic


Manual
------

::

    $ git clone git://github.com/lofic/pygments-style-lofic.git
    $ cd pygments-style-lofic
    $ (sudo) python setup.py install


Usage example
=============

::

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='lofic').style
    <class 'pygments_style_lofic.LoficStyle'>


Export the style as CSS
========================

::

    pygmentize -S lofic -f html > lofic.css


Using in LaTeX documents
========================

See the minted package at http://minted.googlecode.com


Extra information
=================

Pygments supported languages
----------------------------

Pygments at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    $ pygmentize -L lexers

Pygments styles avaible
-----------------------

To get a list of all available stylesheets, execute the following command on the
command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/


Thanks
------

This package is based upon the pygments-style-github of Hugo Maia Vieira.

This package is based upon the pygments-style-railscasts_ of Marcus Fredriksson.

.. _pygments-style-railscasts: http://github.com/DrMegahertz/pygments-style-railscasts
