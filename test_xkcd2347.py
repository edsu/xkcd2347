from xkcd2347 import get_deps, get_config

def test_get_deps():
    config = get_config()
    deps = list(get_deps(config, 'docnow', 'twarc'))
    assert len(deps) > 0
    assert deps[0]['repository']['owner']['login']
    
