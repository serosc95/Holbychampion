#!/usr/bin/python3
import json


class Champion:
    def __init__(self, name, race, gender, level=0, exp_next_level=0, currente_exp=0, total_exp=0, stats=0, stat_points=0):
        self.__name = name
        self.__race = race
        self.__gender = gender
        self.__level = level
        self.exp_next_level = exp_next_level
        self.currente_exp = currente_exp
        self.total_exp = total_exp
        self.stats = stats
        self.stat_points = stat_points
    
    def name(self):
        return self.__name

    def race(self):
        return self.__race
    
    def gender(self):
        return self.__gender


    def level_up(self):

    def gain_Exp(self):

    def death(self):

    def save_character(self):

    def load_character(self):

    def increase_stats(self):

    