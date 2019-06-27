from invoke import task, Collection

@task
def build(c):
    print("Building!")

ns = Collection(build)