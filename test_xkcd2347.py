import os
import dotenv
import shutil
import pathlib
import xkcd2347
import diskcache

dotenv.load_dotenv()
key = os.environ.get('GITHUB_TOKEN')


def test_key():
    assert key

def test_get_dependencies():
    gh = xkcd2347.GitHub(key=key)
    deps = list(gh.get_dependencies('docnow', 'twarc'))
    assert len(deps) > 0
    assert deps[0]['repository']['owner']['login']

def test_cache():
    cache_dir = pathlib.Path('test-cache')
    if cache_dir.exists():
        shutil.rmtree(cache_dir)
        cache_dir.mkdir()
    cache = diskcache.Cache(cache_dir)
    
    gh = xkcd2347.GitHub(key=key, cache=cache)
    deps = list(gh.get_dependencies('docnow', 'twarc'))
    assert len(deps) > 0
    assert deps[0]['repository']['owner']['login']
