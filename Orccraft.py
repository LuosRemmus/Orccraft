from dataclasses import dataclass

counter: int = 0


@dataclass
class User:
    # **********    user data fields   **********
    id_: int
    race: str
    class_: str
    hp: int


@dataclass
class Warrior(User):
    strength: int
    armor: int


@dataclass
class Archer(User):
    agility: int
    arrows: int


@dataclass
class Wizard(User):
    mp: int
    intelligence: int
