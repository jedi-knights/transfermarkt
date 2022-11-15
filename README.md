# transfermarkt
A python module for retrieving information from https://www.transfermarkt.com.

![Test](https://github.com/ocrosby/transfermarkt/docs/actions/workflows/test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ocrosby/transfermarkt/badge.svg?branch=main)](https://coveralls.io/github/ocrosby/transfermarkt?branch=main)

You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Installation
```bash
pip install transfermarkt_ocrosby
```

## Usage
```python
from transfermarkt import Market
```

### Get a list of all clubs
```python
from transfermarkt import Market

clubs = Market.get_clubs()
```

## References
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Transfermarkt](https://www.transfermarkt.com)
- [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
- [Packaging Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)