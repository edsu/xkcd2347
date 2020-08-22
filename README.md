# xkcd2347

xkcd2347 is a small utility that uses the
[DependencyGraphManifestConnection](https://docs.github.com/en/graphql/reference/objects#dependencygraphmanifestconnection)
resource in the GitHub GraphQL API to walk the software dependencies in
projects. The utility got its strange name from this XKCD comic:

<a href="https://m.xkcd.com/2347/">
  <img src="https://imgs.xkcd.com/comics/dependency.png">
</a>

## Install

    pip install xkcd2347

### Use

```
$ xkcd2347 --depth 2 edsu/xkcd2347
diskcache: https://github.com/wikifactory/dircache
pyyaml: https://github.com/yaml/pyyaml
requests: https://github.com/psf/requests
 alabaster: https://github.com/bitprophet/alabaster
 codecov: https://github.com/webknjaz/codecov-python
 detox: https://github.com/tox-dev/detox
 flake8: https://github.com/PyCQA/flake8
 httpbin: https://github.com/postmanlabs/httpbin
 more-itertools: https://github.com/more-itertools/more-itertools
 pysocks: https://github.com/Anorov/PySocks
 pytest: https://github.com/pytest-dev/pytest
 pytest-cov: https://github.com/pytest-dev/pytest-cov
 pytest-httpbin: https://github.com/kevin1024/pytest-httpbin
 pytest-mock: https://github.com/pytest-dev/pytest-mock
 pytest-xdist: https://github.com/pytest-dev/pytest-xdist
 readme-renderer: https://github.com/pypa/readme_renderer
 sphinx: https://github.com/sphinx-doc/sphinx
 tox: https://github.com/tox-dev/tox
 apipkg: https://github.com/pytest-dev/apipkg
 appdirs: https://github.com/ActiveState/appdirs
 atomicwrites: https://github.com/untitaker/python-atomicwrites
 attrs: https://github.com/python-attrs/attrs
 babel: https://github.com/python-babel/babel
 bleach: https://github.com/mozilla/bleach
 blinker: https://github.com/jek/blinker
 brotlipy: https://github.com/python-hyper/brotlipy
 certifi: https://github.com/certifi/python-certifi
 cffi: https://github.com/chevah/python-cffi
 chardet: https://github.com/chardet/chardet
 click: https://github.com/pallets/click
 configparser: https://github.com/mdsitton/configparser-3.2.0r3
 contextlib2: https://github.com/jazzband/contextlib2
 coverage: https://github.com/nedbat/coveragepy
 decorator: https://github.com/micheles/decorator
 distlib: 
 dnspython: https://github.com/rthalley/dnspython
 entrypoints: 
 enum34: https://github.com/certik/enum34
 eventlet: https://github.com/eventlet/eventlet
 execnet: https://github.com/pytest-dev/execnet
 filelock: https://github.com/benediktschmitt/py-filelock
 flask: https://github.com/pallets/flask
 funcsigs: https://github.com/aliles/funcsigs
 functools32: https://github.com/michilu/python-functools32
 greenlet: https://github.com/python-greenlet/greenlet
 idna: https://github.com/kjd/idna
 imagesize: https://github.com/shibukawa/imagesize_py
 importlib-metadata: 
 importlib-resources: 
 itsdangerous: https://github.com/pallets/itsdangerous
 jinja2: https://github.com/pallets/jinja
 markupsafe: https://github.com/pallets/markupsafe
 mccabe: https://github.com/PyCQA/mccabe
 mock: https://github.com/calvinchengx/python-mock
 monotonic: https://github.com/atdt/monotonic
 pathlib2: https://github.com/mcmtroffaes/pathlib2
 pluggy: https://github.com/pytest-dev/pluggy
 py: https://github.com/pytest-dev/py
 pycodestyle: https://github.com/PyCQA/pycodestyle
 pycparser: https://github.com/eliben/pycparser
 pyflakes: https://github.com/PyCQA/pyflakes
 pygments: https://github.com/pygments/pygments
 pytest-forked: https://github.com/pytest-dev/pytest-forked
 pytz: https://github.com/stub42/pytz
 raven: https://github.com/getsentry/raven-python
 scandir: https://github.com/benhoyt/scandir
 singledispatch: https://github.com/ambv/singledispatch
 six: https://github.com/benjaminp/six
 snowballstemmer: https://github.com/snowballstem/snowball
 toml: https://github.com/uiri/toml
 typing: https://github.com/python/typing
 urllib3: https://github.com/urllib3/urllib3
 virtualenv: https://github.com/cheshire/virtualenv
 webencodings: https://github.com/gsnedders/python-webencodings
 werkzeug: https://github.com/pallets/werkzeug
 zipp: https://github.com/jaraco/zipp
```

xkcd2347 will cache results in `~/.xkcd2347/cache` but you can ignore the cache to get more recent results by using the `--flush` command line option.

If you give set `--level 0` then xkcd2347 will try to find all the dependencies
as far down as they go. It does take care to not get caught in circular
dependencies.

## Use as a Library

```python

import xkcd2347

gh = xkcd2347.GitHub(key="yourkeyhere")

for dep in gh.get_dependencies('docnow', 'twarc'):
    print(dep['packageName'])
```

## Develop

Put your GitHub token in a .env file:

    GITHUB_TOKEN=YOUR_TOKEN_HERE

And then run the tests!

    python setup.py test
