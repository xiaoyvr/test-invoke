from invoke import Collection, task

@task
def get(c, key):
    print(f"getting {key} from vault - {c['keyhost']}. ")

def configure(ns): 
    ns.configure({'keyhost': 'localhost'})

ns = Collection(get)
configure(ns)
