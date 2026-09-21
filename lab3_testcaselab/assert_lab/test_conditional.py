import pytest
import os
@pytest.mark.skipif(not os.path.exists("/etc/hosts"),reason="No host file")
def test_hosts_file():
    assert           os.path.exists("/etc/hosts")
    