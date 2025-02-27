# -*- coding: utf-8 -*-
"""
    This is part of Kerykeion (C) 2023 Giacomo Battaglia
"""

import json
from pathlib import Path
from kerykeion import AstrologicalSubject
from swisseph import difdeg2n
from typing import Union
from kerykeion.settings.kerykeion_settings import get_settings_dict


class NatalAspects:
    """
    Generates an object with all the aspects of a birthcart.
    """

    def __init__(self, kr_object: AstrologicalSubject, new_settings_file: Union[Path, None] = None):
        self.user = kr_object
        self.new_settings_file = new_settings_file
        self._parse_json_settings()

        self.init_point_list = self.user.planets_list + self.user.houses_list

    def _parse_json_settings(self):
        # Load settings file

        settings = get_settings_dict(
            self.new_settings_file,
        )

        self.planets_settings = settings["celestial_points"]
        self.aspects_settings = settings["aspects"]
        self.axes_orbit_settings = settings["general_settings"]["axes_orbit"]

    def asp_calc(self, point_one, point_two):
        """
        Utility function.
        It calculates the aspects between the 2 points.
        Args: first point, second point.
        """

        distance = abs(difdeg2n(point_one, point_two))
        diff = abs(point_one - point_two)

        if int(distance) <= self.aspects_settings[0]["orb"]:
            name = self.aspects_settings[0]["name"]
            aspect_degrees = self.aspects_settings[0]["degree"]
            color = self.aspects_settings[0]["color"]
            verdict = True
            aid = 0

        elif (
            (self.aspects_settings[1]["degree"] - self.aspects_settings[1]["orb"])
            <= int(distance)
            <= (self.aspects_settings[1]["degree"] + self.aspects_settings[1]["orb"])
        ):
            name = self.aspects_settings[1]["name"]
            aspect_degrees = self.aspects_settings[1]["degree"]
            color = self.aspects_settings[1]["color"]
            verdict = True
            aid = 1

        elif (
            (self.aspects_settings[2]["degree"] - self.aspects_settings[2]["orb"])
            <= int(distance)
            <= (self.aspects_settings[2]["degree"] + self.aspects_settings[2]["orb"])
        ):
            name = self.aspects_settings[2]["name"]
            aspect_degrees = self.aspects_settings[2]["degree"]
            color = self.aspects_settings[2]["color"]
            verdict = True
            aid = 2

        elif (
            (self.aspects_settings[3]["degree"] - self.aspects_settings[3]["orb"])
            <= int(distance)
            <= (self.aspects_settings[3]["degree"] + self.aspects_settings[3]["orb"])
        ):
            name = self.aspects_settings[3]["name"]
            aspect_degrees = self.aspects_settings[3]["degree"]
            color = self.aspects_settings[3]["color"]
            verdict = True
            aid = 3

        elif (
            (self.aspects_settings[4]["degree"] - self.aspects_settings[4]["orb"])
            <= int(distance)
            <= (self.aspects_settings[4]["degree"] + self.aspects_settings[4]["orb"])
        ):
            name = self.aspects_settings[4]["name"]
            aspect_degrees = self.aspects_settings[4]["degree"]
            color = self.aspects_settings[4]["color"]
            verdict = True
            aid = 4

        elif (
            (self.aspects_settings[5]["degree"] - self.aspects_settings[5]["orb"])
            <= int(distance)
            <= (self.aspects_settings[5]["degree"] + self.aspects_settings[5]["orb"])
        ):
            name = self.aspects_settings[5]["name"]
            aspect_degrees = self.aspects_settings[5]["degree"]
            color = self.aspects_settings[5]["color"]
            verdict = True
            aid = 5

        elif (
            (self.aspects_settings[6]["degree"] - self.aspects_settings[6]["orb"])
            <= int(distance)
            <= (self.aspects_settings[6]["degree"] + self.aspects_settings[6]["orb"])
        ):
            name = self.aspects_settings[6]["name"]
            aspect_degrees = self.aspects_settings[6]["degree"]
            color = self.aspects_settings[6]["color"]
            verdict = True
            aid = 6

        elif (
            (self.aspects_settings[7]["degree"] - self.aspects_settings[7]["orb"])
            <= int(distance)
            <= (self.aspects_settings[7]["degree"] + self.aspects_settings[7]["orb"])
        ):
            name = self.aspects_settings[7]["name"]
            aspect_degrees = self.aspects_settings[7]["degree"]
            color = self.aspects_settings[7]["color"]
            verdict = True
            aid = 7

        elif (
            (self.aspects_settings[8]["degree"] - self.aspects_settings[8]["orb"])
            <= int(distance)
            <= (self.aspects_settings[8]["degree"] + self.aspects_settings[8]["orb"])
        ):
            name = self.aspects_settings[8]["name"]
            aspect_degrees = self.aspects_settings[8]["degree"]
            color = self.aspects_settings[8]["color"]
            verdict = True
            aid = 8

        elif (
            (self.aspects_settings[9]["degree"] - self.aspects_settings[9]["orb"])
            <= int(distance)
            <= (self.aspects_settings[9]["degree"] + self.aspects_settings[9]["orb"])
        ):
            name = self.aspects_settings[9]["name"]
            aspect_degrees = self.aspects_settings[9]["degree"]
            color = self.aspects_settings[9]["color"]
            verdict = True
            aid = 9

        elif (
            (self.aspects_settings[10]["degree"] - self.aspects_settings[10]["orb"])
            <= int(distance)
            <= (self.aspects_settings[10]["degree"] + self.aspects_settings[10]["orb"])
        ):
            name = self.aspects_settings[10]["name"]
            aspect_degrees = self.aspects_settings[10]["degree"]
            color = self.aspects_settings[10]["color"]
            verdict = True
            aid = 10

        else:
            verdict = False
            name = None
            distance = 0
            aspect_degrees = 0
            color = None
            aid = None

        return (
            verdict,
            name,
            distance - aspect_degrees,
            aspect_degrees,
            color,
            aid,
            diff,
        )

    def p_id_decoder(self, name):
        """
        Check if the name of the planet is the same in the settings and return
        the correct id for the planet.
        """
        str_name = str(name)
        for planet in self.planets_settings:
            if planet["name"] == str_name:
                result = planet["id"]
                return result

    def filter_by_settings(self, init_point_list):
        """
        Creates a list of all the desired
        points filtering by the settings.
        """

        set_points_name = []
        for p in self.planets_settings:
            if p["is_active"]:
                set_points_name.append(p["name"])

        point_list = []
        for l in init_point_list:
            if l["name"] in set_points_name:
                point_list.append(l)

        return point_list

    def get_all_aspects(self):
        """
        Return all the aspects of the points in the natal chart in a dictionary,
        first all the individual aspects of each planet, second the aspects
        whitout repetitions.
        """

        point_list = self.filter_by_settings(self.init_point_list)

        self.all_aspects_list = []

        for first in range(len(point_list)):
            # Generates the aspects list whitout repetitions
            for second in range(first + 1, len(point_list)):
                verdict, name, orbit, aspect_degrees, color, aid, diff = self.asp_calc(
                    point_list[first]["abs_pos"], point_list[second]["abs_pos"]
                )

                if verdict == True:
                    d_asp = {
                        "p1_name": point_list[first]["name"],
                        "p1_abs_pos": point_list[first]["abs_pos"],
                        "p2_name": point_list[second]["name"],
                        "p2_abs_pos": point_list[second]["abs_pos"],
                        "aspect": name,
                        "orbit": orbit,
                        "aspect_degrees": aspect_degrees,
                        "color": color,
                        "aid": aid,
                        "diff": diff,
                        "p1": self.p_id_decoder(point_list[first]["name"]),
                        "p2": self.p_id_decoder(
                            point_list[second]["name"],
                        ),
                    }

                    self.all_aspects_list.append(d_asp)

        return self.all_aspects_list

    def get_relevant_aspects(self):
        """
        Filters the aspects list with the desired points, in this case
        the most important are hardcoded.
        Set the list with set_points and creating a list with the names
        or the numbers of the houses.
        """

        self.get_all_aspects()

        aspects_filtered = []
        for a in self.all_aspects_list:
            if self.aspects_settings[a["aid"]]["is_active"] == True:
                aspects_filtered.append(a)

        axes_list = [
            "First_House",
            "Tenth_House",
            "Seventh_House",
            "Fourth_House",
        ]
        counter = 0

        aspects_list_subtract = []
        for a in aspects_filtered:
            counter += 1
            name_p1 = str(a["p1_name"])
            name_p2 = str(a["p2_name"])

            if name_p1 in axes_list:
                if abs(a["orbit"]) >= self.axes_orbit_settings:
                    aspects_list_subtract.append(a)

            elif name_p2 in axes_list:
                if abs(a["orbit"]) >= self.axes_orbit_settings:
                    aspects_list_subtract.append(a)

        self.aspects = [item for item in aspects_filtered if item not in aspects_list_subtract]

        return self.aspects


if __name__ == "__main__":
    johnny = AstrologicalSubject("Johnny Depp", 1963, 6, 9, 0, 0, "Owensboro", "US")

    # All aspects
    aspects = NatalAspects(johnny).get_all_aspects()
    print(aspects)

    print("\n")

    # Relevant aspects
    aspects = NatalAspects(johnny).get_relevant_aspects()
    print(aspects)

