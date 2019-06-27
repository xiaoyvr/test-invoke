from invoke import Collection, task
from . import params, terraform


@task
def hi_A(_, name):
    print("Hi  A {}!".format(name))

ns = Collection(hi_A)
