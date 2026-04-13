from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    def get_email(self) -> str:
        return self._email

    def set_email(self, value: str):
        if "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value

    @abstractmethod
    def display_info(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self._name} ({self._email})"
