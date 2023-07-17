import PySimpleGUI as sg
from utils.ships import ships, get_ship_by_name
from utils.battle import Battle
from utils.theme import Theme
import pyperclip
from utils.greedy_finder import process_file

sg.theme_button_color(Theme().enabled_button_color)


class FirstMate:
    def __init__(self):
        self.setup()

    def setup(self):
        self.theme = Theme()
        self.font = ("Helvetica", 14)
        self.small_font = ("Helvetica", 12)
        self.extra_small_font = ("Helvetica", 10)
        self.disabled_button_color = ("gray", "black")
        self.image_size = (110, 65)
        self.layout = self.get_layout()
        self.window = sg.Window("First Mate 1.0.0", self.layout)
        self.player_ship_selection = ships[0]
        self.enemy_ship_selection = ships[0]
        self.battle = Battle(ships[0], ships[0], "pillage")
        self.won_battles = 0
        self.lost_battles = 0
        self.chat_log_file_path = ""

    def get_layout(self):
        layout = [
            [
                sg.Column(
                    [
                        [
                            sg.Radio(
                                "Pillage",
                                "RADIO1",
                                default=True,
                                key="-PILLAGE-MODE-",
                                enable_events=True,
                            ),
                            sg.Radio(
                                "Sink", "RADIO1", key="-SINK-MODE-", enable_events=True
                            ),
                        ]
                    ],
                    justification="center",
                )
            ],
            [
                sg.Column(
                    [
                        [sg.Text("Your Ship", font=self.font)],
                        [
                            sg.Image(
                                filename=ships[0].image_path,
                                key="Player Ship Image",
                                size=self.image_size,
                            )
                        ],
                        [
                            sg.Table(
                                values=list(
                                    map(
                                        list,
                                        zip(
                                            *[
                                                [
                                                    "Class",
                                                    "Moves PT",
                                                    "Shots PT",
                                                    "Gun Size",
                                                    "Battle Max",
                                                    "Sink Max",
                                                ],
                                                [
                                                    ships[0].size,
                                                    ships[0].moves_per_turn,
                                                    ships[0].shots_per_move,
                                                    ships[0].cannon_size,
                                                    ships[0].max_pillage_damage.small,
                                                    ships[0].max_sink_damage.small,
                                                ],
                                            ]
                                        ),
                                    )
                                ),
                                headings=["Property", "Value"],
                                justification="left",
                                num_rows=6,
                                key="-PLAYER-TABLE-",
                                hide_vertical_scroll=True,
                            )
                        ],
                        [
                            sg.Combo(
                                [ship.ship_type for ship in ships],
                                default_value=ships[0].ship_type,
                                key="Player Ship Selection",
                                size=(15, 1),
                                readonly=True,
                                font=self.font,
                                enable_events=True,
                            )
                        ],
                        [
                            sg.ProgressBar(
                                100,
                                orientation="h",
                                size=(15, 15),
                                key="Player Progress Bar",
                                bar_color=("green", "black"),
                            )
                        ],
                        [
                            sg.Text(
                                "",
                                key="Player Progress Data",
                                font=self.extra_small_font,
                            )
                        ],
                        [
                            sg.Button(
                                "One Shot",
                                key="Player Ship One Shot",
                                font=self.small_font,
                            )
                        ],
                        [
                            sg.Button(
                                "Two Shots",
                                key="Player Ship Two Shots",
                                font=self.small_font,
                            )
                        ],
                        [
                            sg.Button(
                                "Rock/Edge Damage",
                                key="Player Rock Damage",
                                font=("Helvetica", 12),
                            )
                        ],
                    ],
                    element_justification="left",
                ),
                sg.Column(
                    [
                        [sg.Text("Enemy Ship", font=self.font)],
                        [
                            sg.Image(
                                filename=ships[0].image_path,
                                key="Enemy Ship Image",
                                size=self.image_size,
                            )
                        ],
                        [
                            sg.Table(
                                values=list(
                                    map(
                                        list,
                                        zip(
                                            *[
                                                [
                                                    "Class",
                                                    "Moves PT",
                                                    "Shots PT",
                                                    "Gun Size",
                                                    "Battle Max",
                                                    "Sink Max",
                                                ],
                                                [
                                                    ships[0].size,
                                                    ships[0].moves_per_turn,
                                                    ships[0].shots_per_move,
                                                    ships[0].cannon_size,
                                                    ships[0].max_pillage_damage.small,
                                                    ships[0].max_sink_damage.small,
                                                ],
                                            ]
                                        ),
                                    )
                                ),
                                headings=["Property", "Value"],
                                justification="left",
                                num_rows=6,
                                key="-ENEMY-TABLE-",
                                hide_vertical_scroll=True,
                            )
                        ],
                        [
                            sg.Combo(
                                [ship.ship_type for ship in ships],
                                default_value=ships[0].ship_type,
                                key="Enemy Ship Selection",
                                size=(15, 1),
                                readonly=True,
                                font=self.font,
                                enable_events=True,
                            )
                        ],
                        [
                            sg.ProgressBar(
                                100,
                                orientation="h",
                                size=(15, 15),
                                key="Enemy Progress Bar",
                                bar_color=("green", "black"),
                            )
                        ],
                        [
                            sg.Text(
                                "",
                                key="Enemy Progress Data",
                                font=self.extra_small_font,
                            )
                        ],
                        [
                            sg.Button(
                                "One Shot",
                                key="Enemy Ship One Shot",
                                font=("Helvetica", 12),
                            )
                        ],
                        [
                            sg.Button(
                                "Two Shots",
                                key="Enemy Ship Two Shots",
                                font=("Helvetica", 12),
                            )
                        ],
                        [
                            sg.Button(
                                "Rock/Edge Damage",
                                key="Enemy Rock Damage",
                                font=("Helvetica", 12),
                            )
                        ],
                    ],
                    element_justification="right",
                ),
            ],
            [
                sg.Column(
                    [
                        [
                            sg.Button(
                                "Ram Damage",
                                key="Ram Damage",
                                font=self.small_font,
                            ),
                            sg.Button(
                                "Copy Score",
                                key="Copy Score",
                                font=self.small_font,
                            ),
                            sg.Button(
                                "Reset Score",
                                key="Reset",
                                font=self.small_font,
                            ),
                        ]
                    ],
                    justification="center",
                )
            ],
            [sg.Column([[sg.Text("_" * 10)]], justification="center")],
            [
                sg.Column(
                    [
                        [
                            sg.Button(
                                "Won Battle",
                                key="Won Battle",
                                font=self.small_font,
                            ),
                            sg.Text("0 - 0", key="Battle Score", font=self.font),
                            sg.Button(
                                "Lost Battle",
                                key="Lost Battle",
                                font=self.small_font,
                            ),
                        ]
                    ],
                    justification="center",
                )
            ],
            [
                sg.Column(
                    [
                        [
                            sg.Frame(
                                "",
                                [
                                    [
                                        sg.Button(
                                            "Reset All",
                                            key="Reset All",
                                        ),
                                        sg.Button(
                                            "Find Greedy Hits", key="Search Greedies"
                                        ),
                                        sg.FileBrowse(
                                            button_text="Load Log File",
                                            key="-LOGFILE-",
                                        ),
                                        sg.Button("Close", key="Exit"),
                                    ]
                                ],
                                element_justification="center",
                                background_color="white",
                            )
                        ]
                    ],
                    justification="center",
                )
            ],
        ]
        return layout

    def update_progress(self, target):
        self.window[f"{target.capitalize()} Progress Data"].update(
            self.battle.get_status_string(target)
        )

        target_damage = (
            self.battle.get_player_damage()
            if target == "player"
            else self.battle.get_enemy_damage()
        )
        # Adjust the progress bar color based on the fill level
        progress_color = ("green", "black")
        if 30 < target_damage <= 60:
            progress_color = ("yellow", "black")
        elif target_damage > 60:
            progress_color = ("red", "black")

        # Update the progress bar properties
        self.window[f"{target.capitalize()} Progress Bar"].update(
            target_damage, bar_color=progress_color
        )

    def handle_ship_selection(self, event, value, values):
        player_ship_selection = None
        enemy_ship_selection = None

        if event == "Player Ship Selection":
            player_ship_selection = get_ship_by_name(value)
            self.window["Player Ship Image"].update(
                filename=player_ship_selection.image_path, size=self.image_size
            )

        if event == "Enemy Ship Selection":
            enemy_ship_selection = get_ship_by_name(value)
            self.window["Enemy Ship Image"].update(
                filename=enemy_ship_selection.image_path, size=self.image_size
            )

        # Only reset battle if either player_ship_selection or enemy_ship_selection have been changed
        if player_ship_selection or enemy_ship_selection:
            player_ship_selection = player_ship_selection or get_ship_by_name(
                values["Player Ship Selection"]
            )
            self.player_ship_selection = player_ship_selection
            enemy_ship_selection = enemy_ship_selection or get_ship_by_name(
                values["Enemy Ship Selection"]
            )
            self.enemy_ship_selection = enemy_ship_selection

            if values["-PILLAGE-MODE-"]:
                self.battle = Battle(
                    player_ship_selection, enemy_ship_selection, "pillage"
                )
            else:
                self.battle = Battle(
                    player_ship_selection, enemy_ship_selection, "sink"
                )
            self.update_table_data()

    def update_table_data(self):
        for target in ["player", "enemy"]:
            ship_selection = getattr(self, f"{target}_ship_selection")
            max_damages = [0, 0]
            if target == "player":
                max_damages = self.battle.get_player_max_damages()
            else:
                max_damages = self.battle.get_enemy_max_damages()

            data = [
                ["Class", "Moves PT", "Shots PT", "Gun Size", "Battle Max", "Sink Max"],
                [
                    ship_selection.size,
                    ship_selection.moves_per_turn,
                    ship_selection.shots_per_move,
                    ship_selection.cannon_size,
                    max_damages[0],
                    max_damages[1],
                ],
            ]
            data_transposed = list(map(list, zip(*data)))
            self.window[f"-{target.upper()}-TABLE-"].update(values=data_transposed)

    def handle_shot_events(self, event):
        if "One Shot" in event:
            target = "player" if "Player" in event else "enemy"
            self.battle.record_shots_taken(target, 1)
        elif "Two Shots" in event:
            target = "player" if "Player" in event else "enemy"
            self.battle.record_shots_taken(target, 2)
        return self.battle

    def update_battle_score(self, event):
        if event == "Won Battle":
            self.won_battles += 1
        elif event == "Lost Battle":
            self.lost_battles += 1
        score = f"{self.won_battles} - {self.lost_battles}"
        self.window["Battle Score"].update(score)

    def run(self):
        self.window.finalize()

        self.window["Player Progress Data"].update(
            self.battle.get_status_string("player")
        )
        self.window["Enemy Progress Data"].update(
            self.battle.get_status_string("enemy")
        )

        battle_modes = {"-PILLAGE-MODE-": "pillage", "-SINK-MODE-": "sink"}

        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break

            if event in battle_modes:
                self.battle = Battle(
                    self.player_ship_selection,
                    self.enemy_ship_selection,
                    battle_modes[event],
                )

            if event in ["Won Battle", "Lost Battle"]:
                self.update_battle_score(event)

            if event == "Reset" or event == "Reset All":
                self.battle.reset_battle()
                if event == "Reset All":
                    self.won_battles = 0
                    self.lost_battles = 0
                    self.window["Battle Score"].update("0 - 0")

            if event in ["Player Ship Selection", "Enemy Ship Selection"]:
                self.handle_ship_selection(event, values[event], values)

            if event in [
                "Player Ship One Shot",
                "Player Ship Two Shots",
                "Enemy Ship One Shot",
                "Enemy Ship Two Shots",
            ]:
                self.handle_shot_events(event)

            if event in ["Player Rock Damage", "Enemy Rock Damage"]:
                target = "player" if "Player" in event else "enemy"
                self.battle.record_rock_damage(target)

            if event == "Ram Damage":
                self.battle.record_ram_damage()

            if event == "Copy Score":
                pyperclip.copy(self.battle.get_overall_score())

            if event == "Search Greedies":
                self.chat_log_file_path = values["-LOGFILE-"]
                if self.chat_log_file_path == None or self.chat_log_file_path == "":
                    sg.popup("Please load chat log file first", title="No File Loaded")
                else:
                    hits, total_hits = process_file(self.chat_log_file_path)
                    if hits:
                        message = "(COPIED TO CLIPBOARD)\n\n"
                        hits_string = "Total Hits: " + str(total_hits) + "!\n"
                        hits_string += ", ".join(
                            [f"{name}: {hit}" for name, hit in hits.items()]
                        )

                        pyperclip.copy(hits_string)
                        sg.popup(message + hits_string, title="Found Hits")
                    else:
                        sg.popup("No greedy hits found", title="Not Found")

            # Update all progress data into the GUI
            for target in ["player", "enemy"]:
                self.update_progress(target)

        self.window.close()


if __name__ == "__main__":
    app = FirstMate()
    app.run()
