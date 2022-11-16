class MetaProperty:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.value = kwargs.get("value")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, input_name: str):
        if input_name is not None:
            input_name = input_name.strip()

        self._name = input_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, input_value: str):
        if input_value is not None:
            if type(input_value) != str:
                input_value = str(input_value)

            input_value = input_value.strip()

        self._value = input_value

    def __repr__(self):
        if self.value is None:
            return f"{self.name}=null"
        else:
            return f"{self.name}='{self.value}'"

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value


class MetaModel:
    def __init__(self, **kwargs):
        self.meta = kwargs.get("meta", [])

    def has_property(self, name: str) -> bool:
        for item in self.meta:
            if item.name == name:
                return item.value is not None and item.value != ""

        return False

    def get_property(self, name: str) -> str | None:
        for item in self.meta:
            if item.name == name:
                return item.value

        return None

    def update_property(self, name: str, value: str | None):
        found = False
        for item in self.meta:
            if item.name == name:
                found = True
                item.value = value

        if not found:
            self.add_property(name, value)

    def add_property(self, name: str, value: str | None):
        if value is not None:

            if type(value) == str:
                value = value.strip()

                if len(value) == 0:
                    value = None

        if self.has_property(name):
            self.update_property(name, value)
        else:
            self.meta.append(MetaProperty(name=name, value=value))

    def remove_property(self, name: str):
        for item in self.meta:
            if item.name == name:
                self.meta.remove(item)
                break

