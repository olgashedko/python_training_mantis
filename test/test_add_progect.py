import time

from model.project import Project


def test_add_new_project(app):
    app.session.login("administrator", "root")
    old_projects = app.ProjectHelper.get_project_list()
    project_name1 = "test" + str(len(old_projects)+1)
    app.ProjectHelper.create_new_project(Project(project_name=project_name1))
    time.sleep(1)
    new_projects = app.ProjectHelper.get_project_list()
    old_projects.append(Project(project_name=project_name1))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
