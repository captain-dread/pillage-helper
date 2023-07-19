import os
import sys


class Damage:
    def __init__(self, small: float, medium: float, large: float) -> None:
        self.small = small
        self.medium = medium
        self.large = large

    def __getitem__(self, cannon_size: str) -> float:
        if cannon_size.lower() == "small":
            return self.small
        elif cannon_size.lower() == "medium":
            return self.medium
        elif cannon_size.lower() == "large":
            return self.large
        else:
            raise KeyError(
                f"'{cannon_size}' cannon size not recognized. Please use 'small', 'medium', or 'large'."
            )


class Ship:
    def __init__(
        self,
        ship_type: str,
        size: str,
        moves_per_turn: int,
        shots_per_move: int,
        cannon_size: str,
        max_pillage_damage: Damage,
        max_sink_damage: Damage,
        rock_damage: Damage,
        ram_damage: Damage,
    ) -> None:
        self.ship_type = ship_type
        self.size = size
        self.moves_per_turn = moves_per_turn
        self.shots_per_move = shots_per_move
        self.cannon_size = cannon_size
        self.max_pillage_damage = max_pillage_damage
        self.max_sink_damage = max_sink_damage
        self.rock_damage = rock_damage
        self.ram_damage = ram_damage

        if getattr(sys, "_MEIPASS", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        self.image_path = os.path.join(
            base_path, "utils", "images", f"{ship_type.replace(' ', '_')}.png"
        )


ships = [
    Ship(
        "Sloop",
        "Small",
        4,
        1,
        "Small",
        Damage(6, 4, 3),
        Damage(10, 6.667, 5),
        Damage(0.5, 0.333, 0.25),
        Damage(0.5, 0.333, 0.25),
    ),
    Ship(
        "Cutter",
        "Small",
        4,
        1,
        "Small",
        Damage(7.5, 5, 3.75),
        Damage(12, 8, 6),
        Damage(0.625, 0.417, 0.3125),
        Damage(0.5, 0.333, 0.25),
    ),
    Ship(
        "Dhow",
        "Small",
        4,
        1,
        "Medium",
        Damage(7.5, 5, 3.75),
        Damage(12, 8, 6),
        Damage(0.625, 0.417, 0.3125),
        Damage(0.5, 0.333, 0.25),
    ),
    Ship(
        "Fanchuan",
        "Small",
        3,
        1,
        "Large",
        Damage(7.875, 5.225, 3.9375),
        Damage(13.125, 8.75, 6.5625),
        Damage(0.65625, 0.4375, 0.328125),
        Damage(0.5, 0.333, 0.25),
    ),
    Ship(
        "Longship",
        "Medium",
        4,
        2,
        "Small",
        Damage(9, 6, 4.5),
        Damage(15, 10, 7.5),
        Damage(0.75, 0.5, 0.375),
        Damage(0.5, 0.333, 0.25),
    ),
    Ship(
        "Baghlah",
        "Medium",
        3,
        2,
        "Medium",
        Damage(12, 8, 6),
        Damage(20, 13.333, 10),
        Damage(1, 0.667, 0.5),
        Damage(1, 0.667, 0.5),
    ),
    Ship(
        "Merchant Brig",
        "Medium",
        3,
        1,
        "Medium",
        Damage(12, 8, 6),
        Damage(20, 13.333, 10),
        Damage(1, 0.667, 0.5),
        Damage(1, 0.667, 0.5),
    ),
    Ship(
        "Junk",
        "Medium",
        3,
        1,
        "Large",
        Damage(15, 10, 7.5),
        Damage(25, 16.66, 12.5),
        Damage(1.25, 0.833, 0.625),
        Damage(1.5, 1, 0.75),
    ),
    Ship(
        "War Brig",
        "Medium",
        3,
        2,
        "Medium",
        Damage(15, 10, 7.5),
        Damage(25, 16.667, 12.5),
        Damage(1.25, 0.833, 0.625),
        Damage(2, 1.333, 1),
    ),
    Ship(
        "Merchant Galleon",
        "Large",
        3,
        1,
        "Large",
        Damage(18, 12, 9),
        Damage(30, 20, 15),
        Damage(1.5, 1, 0.75),
        Damage(2.5, 1.667, 1.25),
    ),
    Ship(
        "Xebec",
        "Large",
        3,
        2,
        "Medium",
        Damage(21, 14, 10.5),
        Damage(25, 23.3333, 17.5),
        Damage(1.75, 1.167, 0.875),
        Damage(2.5, 1.667, 1.25),
    ),
    Ship(
        "War Galleon",
        "Large",
        3,
        2,
        "Large",
        Damage(15, 10, 7.5),
        Damage(25, 16.667, 12.5),
        Damage(1.75, 1.167, 0.875),
        Damage(2.5, 1.667, 1.25),
    ),
    Ship(
        "War Frigate",
        "Large",
        3,
        2,
        "Large",
        Damage(30, 20, 15),
        Damage(50, 33.333, 25),
        Damage(2.5, 1.667, 1.25),
        Damage(3, 2, 1.5),
    ),
    Ship(
        "Grand Frigate",
        "Large",
        3,
        2,
        "Large",
        Damage(36, 24, 18),
        Damage(60, 40, 30),
        Damage(3, 2, 1.5),
        Damage(4, 2.667, 2),
    ),
]


def get_ship_by_name(ship_name: str) -> Ship:
    for ship in ships:
        if ship.ship_type.lower() == ship_name.lower():
            return ship
    raise ValueError(f"Ship '{ship_name}' not found.")
