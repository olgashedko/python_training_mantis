import random
import string
import time

from model.project import Project


def test_add_new_project(app):
    app.session.login("administrator", "root")
    old_projects = app.ProjectHelper.get_project_list()
    project_name1 = random_string("",10)
    app.ProjectHelper.create_new_project(Project(project_name=project_name1))
    time.sleep(1)
    new_projects = app.ProjectHelper.get_project_list()
    old_projects.append(Project(project_name=project_name1))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
