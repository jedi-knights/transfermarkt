from dataclasses import dataclass


@dataclass
class Domain:
    name: str
    url: str

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.url = kwargs.get("url")

    def __repr__(self):
        return f"Domain(name='{self.name}', url='{self.url}')"