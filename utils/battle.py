from utils.ships import Ship


class Battle:
    def __init__(self, player_ship: Ship, enemy_ship: Ship, battle_mode: str) -> None:
        self.battle_mode = battle_mode  # "pillage" or "sink"

        self.player_ship = player_ship
        self.enemy_ship = enemy_ship

        # Shots, Ram, rock, and edge damage will be recorded and converted using the enemy ships cannon ball size.
        self.player_damage_taken = 0
        # Shots, Ram, rock, and edge damage will be recorded and converted using the player ships cannon ball size.
        self.enemy_damage_taken = 0

    def _get_damage(self, ship: Ship, cannon_size: str) -> float:
        if self.battle_mode == "pillage":
            return ship.max_pillage_damage[cannon_size]
        else:  # self.battle_mode == "sink"
            return ship.max_sink_damage[cannon_size]

    def record_rock_damage(self, ship: str):
        if ship == "player":
            # Will be recorded using the enemy ships cannon ball size.
            self.player_damage_taken += self.player_ship.rock_damage[
                self.enemy_ship.cannon_size
            ]

        else:
            # Will be recorded using the player ships cannon ball size.
            self.enemy_damage_taken += self.enemy_ship.rock_damage[
                self.player_ship.cannon_size
            ]

    def record_ram_damage(self):
        self.player_damage_taken += self.enemy_ship.ram_damage[self.enemy_ship.size]
        self.enemy_damage_taken += self.player_ship.ram_damage[self.player_ship.size]

    def record_shots_taken(self, ship: str, shots: int):
        if ship == "player":
            self.player_damage_taken += shots
        else:
            self.enemy_damage_taken += shots

    def get_player_damage(self):
        enemy_cannon_size = self.enemy_ship.cannon_size
        max_damage = self._get_damage(self.player_ship, enemy_cannon_size)

        return min((self.player_damage_taken / max_damage) * 100, 100)

    def get_player_shots_taken(self):
        return self.player_damage_taken

    def get_enemy_damage(self):
        player_cannon_size = self.player_ship.cannon_size
        max_damage = self._get_damage(self.enemy_ship, player_cannon_size)

        return min((self.enemy_damage_taken / max_damage) * 100, 100)

    def get_player_max_damages(self) -> list:
        pillage_damage = self.player_ship.max_pillage_damage[
            self.enemy_ship.cannon_size
        ]
        sink_damage = self.player_ship.max_sink_damage[self.enemy_ship.cannon_size]
        return [pillage_damage, sink_damage]

    def get_enemy_max_damages(self) -> list:
        pillage_damage = self.enemy_ship.max_pillage_damage[
            self.player_ship.cannon_size
        ]
        sink_damage = self.enemy_ship.max_sink_damage[self.player_ship.cannon_size]
        return [pillage_damage, sink_damage]

    def get_enemy_shots_taken(self):
        return self.enemy_damage_taken

    def get_overall_score(self):
        player_status = f"{round(self.player_damage_taken, 2)}/{round(self._get_damage(self.player_ship, self.enemy_ship.cannon_size), 2)}({round(self.get_player_damage())}%)"
        enemy_status = f"{round(self.enemy_damage_taken, 2)}/{round(self._get_damage(self.enemy_ship, self.player_ship.cannon_size), 2)}({round(self.get_enemy_damage())}%)"
        return f"{player_status} - {enemy_status}"

    def get_status_string(self, entity):
        if entity == "player":
            status = (
                f"{round(self.player_damage_taken, 2)}/{round(self._get_damage(self.player_ship, self.enemy_ship.cannon_size), 2)} (received/max)"
                + f" {round(self.get_player_damage())}%"
            )
        elif entity == "enemy":
            status = (
                f"{round(self.enemy_damage_taken, 2)}/{round(self._get_damage(self.enemy_ship, self.player_ship.cannon_size), 2)} (received/max)"
                + f" {round(self.get_enemy_damage())}%"
            )

        return status

    def reset_battle(self):
        self.player_damage_taken = 0
        self.enemy_damage_taken = 0
