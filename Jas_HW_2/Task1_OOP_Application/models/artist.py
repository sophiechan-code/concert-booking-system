from .person import Person


class Artist(Person):
    def __init__(self, name: str, agency: str, email: str = "contact@agency.com"):
        super().__init__(name, email)
        self._agency = agency

    def get_agency(self) -> str:
        return self._agency

    def set_agency(self, value: str):
        self._agency = value

    def display_info(self) -> str:
        return f"Artist: {self._name}, agency: {self._agency}"
