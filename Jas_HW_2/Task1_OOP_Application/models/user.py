from .person import Person


class Fan(Person):

    total_fans = 0

    def __init__(self, name: str, email: str):
        super().__init__(name, email)

        self._priority = 10
        self._joined_date = "today"

        Fan.total_fans += 1

    @classmethod
    def get_total_fans(cls) -> int:
        return cls.total_fans

    def display_info(self) -> str:
        return f"Regular Fan: {self._name}, Email: {self._email}, Priority: {self._priority}"

    def get_priority(self) -> int:
        return self._priority

    def set_priority(self, value: int):
        self._priority = value


class VIPFan(Fan):

    def __init__(self, name: str, email: str, vip_level: str = "Gold"):
        super().__init__(name, email)
        
        self._vip_level = vip_level

        self._priority = 100 if vip_level == "Platinum" else 50

    def display_info(self) -> str:
        return f"VIP Fan ({self._vip_level}): {self._name} | Priority: {self._priority}"
