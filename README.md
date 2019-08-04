# python-brlcad
This is compatible with python 3.x.x .If there is an issue, please Pull
Use [brlcad](http://brlcad.org/) from python based on ctypes bindings. These
ctypes bindings are generated during install-time using.
[ctypesgen] is used from https://github.com/olsonse/ctypesgen.

## installing

```
pip is not ready :(
```

or

```
git clone git@github.com:scorp08/python-brlcad.git
cd python-brlcad/
export BRLCAD_PATH=/usr/brlcad
python setup.py install
```

### installing on windows

Use either mingw or cygwin to provide gcc during installation. For details
please consult the README_WIN.md file.

### non-standard brlcad installation path

You can set the BRLCAD_HOME environment variable to the installation path of
your brlcad distribution before running the setup.py script, and the brlcad
libraries found there will be used.
You could use this to install multiple versions of brl-cad, possibly using
virtualenv to isolate the resulting python packages.

## testing

```
nosetests
```

## usage

Sorry, not yet. Check the `examples/` folder.

# Known to work with..

Operating systems known to work:

* linux distros
* windows

Support for Mac OS X is planned but not yet implemented or tested.

## license

BSD.
