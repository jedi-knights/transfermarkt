import pytest

from transfermarkt.models.meta import MetaModel, MetaProperty


@pytest.fixture
def meta_property():
    return MetaProperty(name="test", value="value")


@pytest.fixture
def meta_model():
    return MetaModel(meta=[MetaProperty(name="test", value="value")])


class TestMetaPropertyConstructor:
    def test_name(self, meta_property):
        assert meta_property.name == "test"

    def test_value(self, meta_property):
        assert meta_property.value == "value"


class TestValueSetter:
    def test_with_number(self, meta_property):
        meta_property.value = 123
        assert meta_property.value == "123"


def test_repr(meta_property):
    assert repr(meta_property) == "test='value'"


def test_eq(meta_property):
    assert meta_property == MetaProperty(name="test", value="value")


def test_repr_none(meta_property):
    meta_property.value = None
    assert repr(meta_property) == "test=null"


def test_model_has_property(meta_model):
    assert meta_model.has_property("test")


def test_model_has_property_not(meta_model):
    assert not meta_model.has_property("not-test")


def test_model_get_property(meta_model):
    assert meta_model.get_property("test") == "value"


def test_model_get_property_not(meta_model):
    assert meta_model.get_property("not-test") is None


def test_model_update_property(meta_model):
    meta_model.update_property("test", "new-value")
    assert meta_model.get_property("test") == "new-value"


def test_model_update_property_not(meta_model):
    meta_model.update_property("not-test", "value")
    assert meta_model.get_property("not-test") == "value"


def test_model_update_property_none(meta_model):
    meta_model.update_property("test", None)
    assert meta_model.get_property("test") is None


def test_model_add_property(meta_model):
    meta_model.add_property("new-test", "value")
    assert meta_model.get_property("new-test") == "value"


def test_model_add_property_none(meta_model):
    meta_model.add_property("new-test", None)
    assert meta_model.get_property("new-test") is None


def test_model_add_property_empty(meta_model):
    meta_model.add_property("new-test", "")
    assert meta_model.get_property("new-test") is None


def test_model_add_property_existing(meta_model):
    meta_model.add_property("test", "new-value")
    assert meta_model.get_property("test") == "new-value"


def test_model_add_property_existing_none(meta_model):
    meta_model.add_property("test", None)
    assert meta_model.get_property("test") is None


def test_model_remove_property(meta_model):
    meta_model.remove_property("test")
    assert not meta_model.has_property("test")


def test_model_remove_property_not(meta_model):
    meta_model.remove_property("not-test")
    assert not meta_model.has_property("not-test")
