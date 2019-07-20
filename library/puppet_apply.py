#!/usr/bin/python3

import subprocess
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.utils import Utils


# construct puppet command for module
def puppet_command(params):
    # establish base command
    command = Utils.find_puppet() + ' apply --color false'

    # add optional arguments and flags
    if params['noop']: command += ' --noop'

    return command + f" {params['manifest']}"


# main method
def main():
    # initialize ansible module
    module = AnsibleModule(
        argument_spec=dict(
            manifest=dict(type='str', required=True),
            noop=dict(type='bool', default=False),
        )
    )

    # execute puppet apply command
    try:
        output = subprocess.check_output(puppet_command(module.params), shell=True)
    except:
        # TODO: claims that output not assigned yet here
        module.fail_json(changed=False, msg=output)
    else:
        module.exit_json(changed=True)


if __name__ == '__main__':
    main()
