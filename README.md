# transfermarkt rev: v0.1.1
A python module for retrieving information from https://www.transfermarkt.com.

![Test](https://github.com/ocrosby/transfermarkt/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ocrosby/transfermarkt/badge.svg?branch=main)](https://coveralls.io/github/ocrosby/transfermarkt?branch=main)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Installation
```bash
pip install transfermarkt_ocrosby
```

## Usage

```python
from transfermarket.market import Market
```

### Get a list of all clubs

```python
from transfermarket.market import Market

clubs = Market.get_clubs()
```


## Publishing the package

```bash
$ poetry build
$ poetry config repositories.testpypi https://test.pypi.org/legacy/
$ poetry publish -r testpypi
```

## References
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Transfermarkt](https://www.transfermarkt.com)
- [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
- [Packaging Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)
- [Semantic release with Python, Poetry & GitHub Actions](https://mestrak.com/blog/semantic-release-with-python-poetry-github-actions-20nn)
- [GitHub bot to enforce semantic PRs](https://github.com/apps/semantic-pull-requests)