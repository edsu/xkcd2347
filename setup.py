from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    version = '0.0.4',
    name = 'xkcd2347',
    url = 'http://github.com/edsu/xkcd2347',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/mit-license.php',
    py_modules = ['xkcd2347'],
    description = 'List the dependencies for a github project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points = {'console_scripts': ['xkcd2347 = xkcd2347:main']},
    install_requires = ['requests', 'pyyaml', 'diskcache'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'python-dotenv'],
)
