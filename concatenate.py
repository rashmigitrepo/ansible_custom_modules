#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
metadata = {
    'name': 'concatenate',
    'argument_spec': dict(
        string1=dict(type='str', required=True),
        string2=dict(type='str', required=False, default='Mumbai')
    )
}
def concatenate_strings(string1, string2):
    combined_string = string1 + string2
    return combined_string
def main():
    module = AnsibleModule(
        argument_spec=metadata['argument_spec'],
        supports_check_mode=True
    )
    string1_value = module.params['string1']
    string2_value = module.params['string2']
    # Your module logic here
    combined_result = concatenate_strings(string1_value, string2_value)
    result_message = f"Concatenation of '{string1_value}' and '{string2_value}' is '{combined_result}'"
    result = {
        'changed': True,
        'result_message': result_message,
    }
    module.exit_json(**result)
if __name__ == '__main__':
    main()

