import pprint
import re


class Person:

    def __init__(self, name, separated_name, yomigana, explain):
        self.name = name
        self.separated_name = separated_name
        self.yomigana = yomigana
        self.explain = explain

    @staticmethod
    def create_person(name, abstract):
        m = re.search(r"^(?P<separated_name>.+?)(（|\()(?P<yomigana>.+?)(、.+?(）|\))|(）|\)))は?、?(?P<explain>.*$)",
                      abstract)

        if m is None:
            raise ValueError("Invalid Format: {}".format(name))

        return Person(name, m.group("separated_name"), m.group("yomigana"), m.group("explain"))

    def __repr__(self):
        return self.__class__.__name__ + pprint.pformat(self.__dict__)
