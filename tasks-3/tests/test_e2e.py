import json
from subprocess import check_call, check_output, call


def test_read_and_write():
    config_value = 'subnet123'
    config_name = 'tests/subnet_id'
    
    invoke_write_config(config_name, config_value)
    result = invoke_read_config(config_name)

    assert result == config_value


def test_bulk_retrieval():
    result_file = 'tests/result.env'
    config_list = ['tests/subnet_id', 'tests/vpc_id']
    for index, config in enumerate(config_list):
        invoke_write_config(config, f'bar{index}')

    check_call(['inv', 'params.config-export',
                '--in-file', 'tests/bulk_config.json',
                '--out-file', result_file])

    with open(result_file, 'r') as f:
        for cnt, line in enumerate(f):
            env_name = config_list[cnt].split('/')[-1].upper()
            assert f'{env_name}=bar{cnt}' == line.strip()


def invoke_write_config(name, value):
    check_call(['inv', 'params.write',
                '--name', name,
                '--value', value])

def invoke_read_config(name):
    return check_output(['inv', 'params.read',
                           '--name', name]).strip().decode()
