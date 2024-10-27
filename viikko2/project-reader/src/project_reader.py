from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        toml_data = toml.loads(content)
        #print('toml_data:')
        #print(toml_data)
        name = toml_data.get("tool", {}).get("poetry", {}).get("name", "-")
        #print('Name:', name)
        description = toml_data.get("tool", {}).get("poetry", {}).get("description", "-")
        license = toml_data.get("tool", {}).get("poetry", {}).get("license", "-")
        authors = toml_data.get("tool", {}).get("poetry", {}).get("authors", [])
        #print(license, authors)
        #print('Description:', description)
        dependencies = list(toml_data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        #print('Dependencies:', dependencies)
        dev_dep = list(toml_data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        #print('Dev Dependencies:', dev_dep)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
        return Project(name, description, license, authors, dependencies, dev_dep)