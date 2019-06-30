#!/usr/bin/python3

import subprocess
from ansible.module_utils.basic import AnsibleModule


def puppet_command(params):
    command = params['path'] + ' apply --color false'

    if params['noop']: command += ' --noop'

    return command + f" {params['manifest']}"


def main():
    module = AnsibleModule(
        argument_spec=dict(
            manifest=dict(type='str', required=True),
            noop=dict(type='bool', default=False),
            path=dict(type='path', default='/usr/local/bin/puppet')
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
