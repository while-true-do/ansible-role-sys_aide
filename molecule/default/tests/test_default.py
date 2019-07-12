# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aide_package(host):
    pkg = host.package('aide')

    assert pkg.is_installed


def test_aide_db(host):
    file = host.file('/var/lib/aide/aide.db.gz')

    with host.sudo():
        assert file.exists
        assert file.user == 'root'
        assert file.group == 'root'


def test_aide_timer(host):
    srv = host.service('aide-check.timer')

    assert srv.is_enabled
    assert srv.is_running
