from model.project import Project
import random
import string
import re


def clear(s):
    return re.sub("['`\/]", "", s)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(map(lambda x: clear(x), [random.choice(symbols) for i in range(random.randrange(maxlen))]))


status = ["development", "release", "stable", "obsolete"]
view_state = ["public", "private"]


testdata = [Project(name="", description="", status="-", view_state="-")] + [
    Project(name=random_string("name", 20), description=random_string("description", 20), status=random.choice(status),
            view_state=random.choice(view_state))
    #for i in range(n)
    ]


def test_add_project(app):
    project_data = testdata
    old_projects = app.project.get_project_list()
    app.project.create(project_data)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project_data)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

