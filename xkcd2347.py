#!/usr/bin/env python3

import os
import sys
import yaml
import shutil
import pathlib
import argparse
import requests
import diskcache

def main(repo_owner, repo_name, depth, lang, flush_cache):
    config = get_config(flush_cache)
    for dep in get_deps(config, repo_owner, repo_name, depth=depth, lang=lang):
        print(dep['level'] * " ", dep['packageName'])


def get_config(flush_cache=False):
    home = pathlib.Path.home() / ".xkcd2347"
    cache = home / "cache"

    if not home.exists():
        home.mkdir()
        cache.mkdir()

    if flush_cache:
        shutil.rmtree(cache)
        cache.mkdir()

    config = home / "config.yaml"
    if not config.exists():
        github_token = input('Please enter your GitHub token: ')
        config.open('w').write(
            yaml.dump({
                "github_token": github_token
            })
        )
        print("Saved GitHub token to {}".format(config))

    config_data = yaml.safe_load(config.open())
    config_data['cache'] = diskcache.Cache(cache)
    return config_data

def get_deps(config, repo_owner, repo_name, depth=1, level=0, lang=None):
    q = '''
        {
          repository(owner: "%s", name: "%s") {
            description
            dependencyGraphManifests(first: 50) {
              nodes {
                blobPath
                dependencies {
                  nodes {
                    packageName
                    repository {
                      name
                      owner {
                        login
                      }
                      primaryLanguage {
                        name
                      }
                    }
                    requirements
                    hasDependencies
                  }
                }
              }
            }
          }
        }
        '''

    # seen is used to prevent a given dependency from being reported more than
    # one when a project have multiple dependencyGraphManifests
    seen = set()

    results = query(config, q % (repo_owner, repo_name)) 
    for m in results['data']['repository']['dependencyGraphManifests']['nodes']:
        for dep in m['dependencies']['nodes']:
            dep['level'] = level

            if lang and dep['primaryLanguage']['name'].lower() != lang.lower():
                continue

            if dep['packageName'] in seen:
                continue

            seen.add(dep['packageName'])
            yield dep

            if (depth == 0 or level + 1 < depth) and dep['hasDependencies'] == True and dep['repository']:
                yield from get_deps(
                    config,
                    dep['repository']['owner']['login'],
                    dep['repository']['name'],
                    depth,
                    level + 1
                )

def query(config, q):
    if not q in config['cache']:
        headers = {
            "Authorization": "Bearer {}".format(config['github_token']),
            "Accept": "application/vnd.github.hawkgirl-preview+json"
        }
        resp = requests.post('https://api.github.com/graphql', json={'query': q}, headers=headers)
        if resp.status_code == 200:
            config['cache'][q] = resp.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(resp.status_code, q))
    return config['cache'][q]

if __name__ == "__main__":
    argp = argparse.ArgumentParser(description="Find project dependencies using GitHub's API")
    argp.add_argument('repo', help='The repository name e.g. jupyter/notebook')
    argp.add_argument('--depth', type=int, default=1, help='Depth to search')
    argp.add_argument('--lang', help='Limit to language dependencies')
    argp.add_argument('--flush', action="store_true", help='Flush the cache of previous data')
    args = argp.parse_args()
    repo_owner, repo_name = args.repo.split('/')
    main(
        repo_owner=repo_owner,
        repo_name=repo_name,
        depth=args.depth,
        lang=args.lang,
        flush_cache=args.flush,
    )
