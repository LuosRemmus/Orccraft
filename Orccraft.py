from dataclasses import dataclass


@dataclass
class Weapon:
    id_: int
    name: str
    type_: str
    damage: int


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
    intelligence: int
    mp: int
