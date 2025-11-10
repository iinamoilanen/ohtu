import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
    

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        poetry_data = data.get("tool", {}).get("poetry", {})
        
        name = poetry_data.get("name", "No name")
        description = poetry_data.get("description", "No description")
        dependencies = list(poetry_data.get("dependencies", {}).keys())
        dev_dependencies = list(poetry_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        authors = poetry_data.get("authors", [])
        license_ = poetry_data.get("license", "No license")

        project = Project(name, description, dependencies, dev_dependencies, license_, authors)

        return project

        #return Project("Test name", "Test description", [], [])
