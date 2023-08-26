#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

metadata = {
    'name': 'my_custom_module',
    'argument_spec': dict(
        my_argument=dict(type='str', required=True),
        another_argument=dict(type='int', required=False, default=5)
    )
}

def main():
    module = AnsibleModule(
        argument_spec=metadata['argument_spec'],
        supports_check_mode=True
    )
    
    my_argument_value = module.params['my_argument']
    another_argument_value = module.params['another_argument']
    
    # Your module logic here
    result_message = f"Received '{my_argument_value}'. Custom message: Argument value plus {another_argument_value}"
    
    result = {
        'changed': True,
        'result_message': result_message,
    }
    
    module.exit_json(**result)

if __name__ == '__main__':
    main()
