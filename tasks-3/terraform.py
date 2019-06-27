from invoke import task
from . import params

@task
def export_output(ctx, name):
    output = ctx.run(f'terraform output {name}', hide=True).stdout
    params.write(ctx, f'terraform/{name}', output)
