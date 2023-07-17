import re
from collections import defaultdict
import PySimpleGUI as sg


def has_battle_started(line):
    possible_starts = ["You intercepted the", "You have been intercepted by the"]
    return any(start in line for start in possible_starts)


def has_battle_ended(line):
    possible_end = "The victors plundered"
    return possible_end in line


def get_individual_greedy_hit(line):
    pattern = r"\[\d{2}:\d{2}:\d{2}\]\s(.*?)\s(swing|perform|execute|deliver)s a"
    match = re.search(pattern, line)
    return match and match.group(1)


def pull_greedy_hits_from_battle_log(latest_battle):
    hits = defaultdict(int)
    total_hits = 0

    for line in latest_battle:
        name = get_individual_greedy_hit(line)
        if name:
            hits[name] += 1
            total_hits += 1
    return hits, total_hits


def process_file(file_path):
    try:
        latest_battle = []
        recording_battle = False
        with open(file_path, "r") as file:
            for line in file:
                if recording_battle:
                    latest_battle.append(line.strip())
                if has_battle_started(line):
                    latest_battle = []
                    recording_battle = True
                elif has_battle_ended(line):
                    recording_battle = False

        greedy_results, total_hits = pull_greedy_hits_from_battle_log(latest_battle)
        return greedy_results, total_hits
    except Exception as e:
        sg.popup("Error processing file: ", e)
