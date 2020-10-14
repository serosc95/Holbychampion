#!/usr/bin/python3
import json


class Champion:
    def __init__(self, name, race, gender, level=0, exp_next_level=0, currente_exp=0, total_exp=0, stats=0, stat_points=0):
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.exp_next_level = exp_next_level
        self.currente_exp = currente_exp
        self.total_exp = total_exp
        self.stats = stats
        self.stat_points = stat_points

    def level_up(self):

    def gain_Exp(self):

    def death(self):

    def save_character(self):

    def load_character(self):

    def increase_stats(self):

    