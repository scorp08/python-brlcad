# python3-brlcad

Compatible ctypesgen for py3:
[ctypesgen](https://github.com/olsonse/ctypesgen).

## installing

```
Sorry, not ready :(
```

or

```
git clone git@github.com:kanzure/python-brlcad.git
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
