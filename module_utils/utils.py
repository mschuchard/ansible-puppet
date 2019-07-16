from ansible.module_utils.basic import AnsibleModule


class Utils():
    def find_puppet():
        puppet = AnsibleModule.get_bin_path('puppet', False, ['/opt/puppetlabs/bin'])

        if puppet is None: AnsibleModule.fail_json(msg='Unable to find puppet in path. Puppet needs to be installed.')

        return puppet
