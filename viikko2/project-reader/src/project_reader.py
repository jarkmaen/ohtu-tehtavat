from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        load = toml.load("/home/jarkmaen/Documents/GitHub/ohtu-tehtavat/viikko2/project-reader/pyproject.toml")
        return Project(load['tool']['poetry']['name'], load['tool']['poetry']['description'], load['tool']['poetry']['dependencies'], load['tool']['poetry']['dev-dependencies'])
