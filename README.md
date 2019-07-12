<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_aide.svg)](https://github.com/while-true-do/ansible-role-sys_aide/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_aide.svg)](https://github.com/while-true-do/ansible-role-sys_aide/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_aide.svg)](https://github.com/while-true-do/ansible-role-sys_aide/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_aide.svg)](https://github.com/while-true-do/ansible-role-sys_aide/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_aide.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_aide)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_aide%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_aide)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_aide%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_aide)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_aide%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_aide)

# Ansible Role: sys_aide

An Ansible Role to install and configure AIDE.

## Motivation

[AIDE](https://aide.github.io/) (Advanced Intrusion Detection Environment) is
a file and directory integrity checker. It is part of many compliance guidelines
and many operators will have the need to use it.

## Description

This Ansible Role installs and configures AIDE.

-   install packages
-   configure database path and name
-   initialize a new database
-   create systemd timer or cron job

## Requirements

Used Modules:

-   [Ansible package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible lineinfile Module](https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html)
-   [Ansible stat Module](https://docs.ansible.com/ansible/latest/modules/stat_module.html)
-   [Ansible template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible cron Module](https://docs.ansible.com/ansible/latest/modules/cron_module.html)
-   [Ansible systemd Module](https://docs.ansible.com/ansible/latest/modules/systemd_module.html)
-   [Ansible command Module](https://docs.ansible.com/ansible/latest/modules/command_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_aide)
```
ansible-galaxy install while_true_do.sys_aide
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_aide)
```
git clone https://github.com/while-true-do/ansible-role-sys_aide.git while_true_do.sys_aide
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.sys_aide

## Package Management
wtd_sys_aide_package: "aide"
# State can be present|latest|absent
wtd_sys_aide_package_state: "present"

## Configuration Management
# DB Configuration
wtd_sys_aide_conf_db_path: "/var/lib/aide"
wtd_sys_aide_conf_db_name: "aide.db.gz"
wtd_sys_aide_conf_db_new_name: "aide.db.new.gz"
# Scheduler can be: cron|systemd|none
wtd_sys_aide_conf_scheduler: "systemd"
# times can be any valid time format for the scheduler
# daily, weekly, monthly are recommended
wtd_sys_aide_conf_times: "weekly"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_aide
```

#### Advanced

Use cron as a scheduler and run the check daily.

```
- hosts: all
  roles:
    - role: while_true_do.sys_aide
      wtd_sys_aide_conf_scheduler: "cron"
      wtd_sys_aide_conf_times: "daily"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_aide/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_aide/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
