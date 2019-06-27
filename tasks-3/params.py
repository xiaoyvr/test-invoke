from invoke import task
# from .lib import aws
import json

# CLIENT = aws.AWS('/config/')

# @task
# def hi(_, name):
#     print("Hi {}!".format(name))


# @task(autoprint=True)
# def read(_, name):
#     return CLIENT.read_param(name)


# @task
# def write(_, name, value):
#     CLIENT.write_param(name, value)
#     print("Successfully saved config.")


# @task
# def config_export(ctx, in_file, out_file):
#     config_list = get_config_list(in_file)
#     with open(out_file, 'w') as result_file:
#         for config in config_list:
#             config_value = CLIENT.read_param(config['name'])
#             env_var_name = config['out_env_var']
#             result_file.write(f'{env_var_name}={config_value}\n')


# def get_config_list(in_file):
#     with open(in_file, 'r') as config_file:
#         return json.load(config_file)
