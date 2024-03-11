from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        url = self.app.config['soap']['wsdlUrl']
        client = Client(url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        url = self.app.config['soap']['wsdlUrl']
        client = Client(url)
        project_list = []
        try:
            project_data_array = client.service.mc_projects_get_user_accessible(username, password)
            for i in range(0, len(project_data_array)):
                project_list.append(Project(project_name=project_data_array[i].name, project_id=project_data_array[i].id))

            return project_list
        except WebFault:
            return project_list
