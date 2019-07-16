#!/usr/bin/python3

import subprocess
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.utils import Utils


def puppet_command(params):
    command = Utils.find_puppet() + ' agent -t --color false'

    if params['noop']: command += ' --noop'
    if params['environment'] is not None: command += f" --environment {params['environment']}"

    return command


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='run', choices=['run', 'stop']),
            environment=dict(type='str'),
            noop=dict(type='bool', default=False),
        )
    )

    try:
        output = subprocess.check_output(puppet_command(module.params), shell=True)
    except:
        # TODO: claims that output not assigned yet here
        module.fail_json(changed=False, msg=output)
    else:
        module.exit_json(changed=True)


if __name__ == '__main__':
    main()
