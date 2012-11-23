#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-lofic',
    version='0.1',
    description='Custom style for pygments.',
    long_description=open('README.rst').read(),
    keywords='pygments style lofic',
    license='BSD',

    author='Louis Coilliot',
    author_email='louis.coilliot@gmail.com',

    url='https://github.com/lofic/pygments-style-lofic',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    lofic=pygments_style_lofic:LoficStyle''',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
