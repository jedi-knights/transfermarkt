from dataclasses import dataclass

from transfermarkt.common.gender import Gender
from transfermarkt.models.meta import MetaProperty, MetaModel


# noinspection PyTypeChecker
@dataclass
class Player(MetaModel):
    id: int
    gender: Gender
    first_name: str
    last_name: str
    club: str
    state: str
    position: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id = kwargs.get("id")
        self.gender = kwargs.get("gender")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.club = kwargs.get("club")
        self.state = kwargs.get("state")
        self.position = kwargs.get("position")

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, value: str):
        if value is not None:
            parts = value.split(" ")

            if len(parts) == 2:
                self.first_name = parts[0]
                self.last_name = parts[1]
            elif len(parts) == 3:
                self.first_name = parts[0]
                self.last_name = parts[-1]
            else:
                self.first_name = value
                self.last_name = None

    @property
    def year(self) -> str | None:
        result = self.get_property("grad_year")
        if result is None:
            result = self.get_property("graduation_year")

        return result

    @property
    def commitment(self) -> str | None:
        result = self.get_property("commitment")

        if result is None:
            result = self.get_property("college_team")

            if result is not None:
                if result.endswith(" Women"):
                    return result[:-6].strip()
                elif result.endswith(" Men"):
                    return result[:-4].strip()

        return result

    @property
    def is_committed(self) -> bool:
        commitment = self.commitment
        return commitment is not None and commitment != ""

    def __repr__(self):
        avps = []

        if self.id is not None:
            avps.append(f"id='{self.id}'")

        avps.append(f"name='{self.name}'")

        if self.year is not None:
            avps.append(f"year='{self.year}'")

        gender_type = type(self.gender)
        if gender_type == Gender:
            avps.append(f"gender='{self.gender.name}'")
        elif gender_type == str:
            avps.append(f"gender='{self.gender}'")

        if self.state is not None:
            avps.append(f"state='{self.state}'")

        avps.append(f"position='{self.position}'")

        if self.club is not None:
            avps.append(f"club='{self.club}'")

        if self.is_committed:
            avps.append(f"commitment='{self.commitment}'")

        return f"<Player({', '.join(avps)})>"
