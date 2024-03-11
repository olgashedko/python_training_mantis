import random
import string
import time

from model.project import Project


def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    if len(old_projects) == 0:
        project_name1 = random_string("", 10)
        app.projectHelper.create_new_project(Project(project_name=project_name1))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.projectHelper.delete_project_by_id(project)
    time.sleep(1)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])