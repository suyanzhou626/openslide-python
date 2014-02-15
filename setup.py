import os
from setuptools import setup

# Load version string
_verfile = os.path.join(os.path.dirname(__file__), 'openslide', '_version.py')
with open(_verfile) as _fh:
    exec(_fh.read())

setup(
    name='openslide-python',
    version=__version__,
    packages=[
        'openslide',
    ],
    maintainer='OpenSlide project',
    maintainer_email='openslide-users@lists.andrew.cmu.edu',
    description='Python interface to OpenSlide',
    long_description=open('README.rst').read(),
    license='GNU Lesser General Public License, version 2.1',
    keywords='openslide whole-slide image virtual slide library',
    url='http://openslide.org/',
    download_url='https://github.com/openslide/openslide-python/releases/download/v%(version)s/openslide-python-%(version)s.tar.gz' % {'version': __version__},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    install_requires=[
        'Pillow',
    ],
    zip_safe=True,
)
