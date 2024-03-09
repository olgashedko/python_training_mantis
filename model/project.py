from sys import maxsize


class Project:
    def __init__(self, project_name=None, project_id=None):
        self.project_name = project_name
        self.project_id = project_id

    def __repr__(self):
        return "%s%s" % (self.project_name, self.project_id)

    def __eq__(self, other):
        return (
                    self.project_id is None or other.project_id is None or self.project_id == other.project_id) and self.project_name == other.project_name

    def id_or_max(self):
        if self.project_id:
            return int(self.project_id)
        else:
            return maxsize