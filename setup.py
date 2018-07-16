from distutils.core import setup
setup(
    name='pr-stats',
    version='0.0.1',
    author='Hleb Viniarski',
    author_email='hleb_viniarski@epam.com',
    scripts=['bin/pr-stats', 'bin/module.py'],
    description='Util to get pull request stats from github',
)
