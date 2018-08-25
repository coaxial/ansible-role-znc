import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_install(host):
    p = host.package("znc")

    assert p.is_installed


def test_znc_user(host):
    u = host.user('znc')

    assert u.name == 'znc'


def test_service_unit_file(host):
    f = host.file('/etc/systemd/system/znc.service')

    assert f.mode == 0o755
    assert f.user == 'root'
    assert f.group == 'root'


def test_znc_config_file(host):
    f = host.file('/var/lib/znc/configs/znc.conf')

    assert f.mode == 0o600
    assert f.user == 'znc'
    assert f.group == 'znc'


def test_znc_started(host):
    s = host.service('znc')

    assert s.is_running
    assert s.is_enabled
