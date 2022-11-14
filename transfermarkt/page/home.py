from transfermarkt.page.object import PageObject
from transfermarkt.page.transfermarkt.models import Domain
#from transfermarkt.page.utils import get_href_from_anchor, get_text_from_anchor


class HomePage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "https://www.transfermarkt.com"

        user_agent = 'Mozilla/5.0'
        user_agent += '(X11; Linux x86_64)'
        user_agent += ' AppleWebKit/537.36'
        user_agent += ' (KHTML, like Gecko)'
        user_agent += ' Chrome/47.0.2526.106'
        user_agent += ' Safari/537.36'

        self.headers = {
            'User-Agent': user_agent
        }

        self.load()

    def get_domains(self) -> list[Domain]:
        switcher = self.soup.find("tm-domainswitcher")
        unordered_list = switcher.find("li")

        domains = []
        for item in unordered_list.children():
            name = get_text_from_anchor(item)
            url = get_href_from_anchor(item)

            domain = Domain(name=name, url=url)
            domains.append(domain)

        return domains

    def get_countries(self) -> list[str]:
        countries = []

        return countries

    def get_competitions(self) -> list[str]:
        competitions = []

        return competitions


if __name__ == "__main__":
    page = HomePage()

    domains = page.get_domains()

    for domain in domains:
        print(domain)
