In order to run this playbook with a dynamic inventory using a private key and limit to only nodes in a group...

% ansible-playbook -i ./aws_ec2_inventory.py playbook.yml --private-key=/Users/laurenterhune/Downloads/aterhune.pem --limit ec2

PLAY [Example playbook] ****************************************************************************************************************************

TASK [Run a command] *******************************************************************************************************************************
changed: [i-02b6d2fdd6489e828]

TASK [Display command output] **********************************************************************************************************************
ok: [i-02b6d2fdd6489e828] => {
    "command_output.stdout": "Hello, world!"
}

PLAY RECAP *****************************************************************************************************************************************
i-02b6d2fdd6489e828        : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0