import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('svc', [
    'mosquitto',
    'nginx'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize('svc', [
    'mariadb'
])
def test_svc_disabled(host, svc):
    service = host.service(svc)

    assert not service.is_running
    assert not service.is_enabled
