from invoke import Collection, task
import key_vault as kv

@task
def push(c, name):
    # print(c.config)
    pwd = kv.get(c, "cr_pwd")
    print(f"pushing {name} to cr - {c['registryAddress']}. ")

@task
def print_config(c):
    print(c.config)

def configure(ns):
    ns.configure({'registryAddress': 'localhost'})
    kv.configure(ns)

ns = Collection(push, print_config)
configure(ns)
