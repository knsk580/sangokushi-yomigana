import csv
from logging import getLogger, StreamHandler, DEBUG

from jinja2 import Environment, FileSystemLoader

from Person import Person

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

DATA_FILES = ["./data/sparql_sangokushi_people.tsv", "./data/sparql_sangokushi_engi_people.tsv"]


def create_people_list(tsv_path_list):
    people = []

    for tsv_file_path in tsv_path_list:
        with open(tsv_file_path, "r") as f:
            reader = csv.DictReader(f, delimiter='\t')
            # Skip header
            next(reader)
            for row in reader:
                try:
                    people.append(Person.create_person(row["name"], row["abstract"]))
                except ValueError as e:
                    logger.warning(e.args)

    return people


def create_html_file(people_list):
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template("people_list.tpl.html")

    rendered = template.render(people=people_list)

    with open("./index.html", "w") as f:
        f.write(rendered)


if __name__ == "__main__":

    create_html_file(sorted(create_people_list(DATA_FILES), key=lambda person: person.yomigana))
