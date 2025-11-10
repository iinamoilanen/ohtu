class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license_, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license_
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return "\n- " + "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def _stringify_authors(self, authors):
        return "\n- " + "\n- ".join(authors) if len(authors) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors:{self._stringify_authors(self.authors)}\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
