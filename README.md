# xkcd2347

This is utility that uses the [DependencyGraphManifestConnection](https://docs.github.com/en/graphql/reference/objects#dependencygraphmanifestconnection) resource in the GitHub GraphQL API to walk the software
dependencies in projects. The utility got its strange name from this XKCD comic:

<a href="https://m.xkcd.com/2347/">
  <img src="https://imgs.xkcd.com/comics/dependency.png">
</a>

### Install

    pip install xkcd2347

### Use

```
$ xkcd2347 --depth 2 edsu/xkcd2347 
 diskcache
 pyyaml
 requests
  alabaster
  codecov
  detox
  docutils
  flake8
  httpbin
  more-itertools
  pysocks
  pytest
  pytest-cov
  pytest-httpbin
  pytest-mock
  pytest-xdist
  readme-renderer
  sphinx
  tox
  apipkg
  appdirs
  atomicwrites
  attrs
  babel
  bleach
  blinker
  brotlipy
  certifi
  cffi
  chardet
  click
  configparser
  contextlib2
  coverage
  decorator
  distlib
  dnspython
  entrypoints
  enum34
  eventlet
  execnet
  filelock
  flask
  funcsigs
  functools32
  greenlet
  idna
  imagesize
  importlib-metadata
  importlib-resources
  itsdangerous
  jinja2
  markupsafe
  mccabe
  mock
  monotonic
  pathlib2
  pluggy
  py
  pycodestyle
  pycparser
  pyflakes
  pygments
  pytest-forked
  pytz
  raven
  scandir
  singledispatch
  six
  snowballstemmer
  toml
  typing
  urllib3
  virtualenv
  webencodings
  werkzeug
  zipp
```

xkcd2347 will cache results in `~/.xkcd2347/cache` but you can ignore the cache to get more recent results by using the `--flush` command line option.
