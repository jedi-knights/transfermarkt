from transfermarket.models.domain import Domain


class TestDomainConstructor:
    def test_name(self):
        assert Domain(name="test").name == "test"

    def test_url(self):
        assert Domain(url="test").url == "test"


def test_repr():
    domain = Domain(name="test1", url="test2")
    assert repr(domain) == "Domain(name='test1', url='test2')"
