from ansible.module_utils.basic import AnsibleModule


# utility class for ansible puppet module
class Utils():
    # find the installation location of puppet
    def find_puppet():
        # attempt to find puppet
        puppet = AnsibleModule.get_bin_path('puppet', False, ['/opt/puppetlabs/bin'])

        # useful error message if puppet not found
        if puppet is None: AnsibleModule.fail_json(msg='Unable to find puppet in path. Puppet needs to be installed.')

        return puppet
