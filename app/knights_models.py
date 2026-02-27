from knights import KNIGHTS
from dataclasses import dataclass

class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def __repr__(self) -> str:
        return f"name: {self.name}"



class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return  f"Weapon(name: '{self.name}', power: {self.power})"

    @classmethod
    def from_dict(cls, data: dict) -> "Weapon":
        return cls(name=data["name"], power=data["power"])
    

class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"Armour(part: '{self.part}', protection: {self.protection})"
   
    @classmethod
    def from_dict(cls, data: dict) -> "Armour":
   
        return cls(
            part = data["part"],
            protection = data["protection"]
        )

@dataclass
class Effect:
    power: int = 0
    hp: int = 0
    protection: int = 0
    
    @classmethod
    def from_dict(cls, data: dict) -> "Effect":
        return cls(
            power = data.get("power", 0), #missing keys = 0
            hp = data.get("hp", 0),
            protection = data.get("protection", 0)
        )
@dataclass
class Potion:
    name: str
    effect: Effect

    @classmethod
    def from_dict(cls, data: dict | None) -> "Potion | None":
        if data is None:
            return None
        return cls(
            name=data["name"],
            effect=Effect.from_dict(data.get("effect", {}))
        )

if __name__ == "__main__":
    armours = [
            Armour.from_dict(a)
            for a in KNIGHTS["arthur"]["armour"]
        ]
    for a in armours:
        print(a)

    weapon = Weapon.from_dict(KNIGHTS["arthur"]["weapon"])
    print (weapon)
    
    knight = Knight("brave_knight", 90, 25)
    print(knight.__dict__)


'''
task: 
    - create an obj from stuff
    - create an obj from knights

    make 2 func: 
        - preparing to the battle
        - batle itself
'''
