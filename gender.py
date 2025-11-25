from enum import Enum

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHERS = "OTHERS"

    def __str__(self):
        return self.value

    def from_string(gen, gender_str):
        try:
            return gen[gender_str.upper()]
        except KeyError:
            return None
