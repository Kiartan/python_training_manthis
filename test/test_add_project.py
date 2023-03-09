from model.project import Project


def test_add_project(app):
    project_data = Project(name="test", description="desc1", status="release", view_state="private")
    #lista przed
    app.project.create(project_data)
    # lista po
    # porównanie długości
    # dodanie nowego elementu do starej listy
    # porównanie składu list

