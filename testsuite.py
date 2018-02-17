
import unittest
import json
import ansimple

class TestFiles(unittest.TestCase):

    def create_file(self, content):
        content_json = json.dumps(content)
        testfile_path = "testfile.json"
        with open(testfile_path, "w") as f:
            f.write(content_json)
        return testfile_path

    def test_empty_item(self):
        content = [{}]
        content_json = json.dumps(content)
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_invalid_item(self):
        content = [{"file": {}, "test": {} }]
        content_json = json.dumps(content)
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_install_apt_package(self):
        content = [{ "package": { "name": "vim" } }]
        content_json = json.dumps(content)
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_create_file_with_mode(self):
        content = [{ "file": { "path": "/tmp/xxx-avgowl-avgowl-666", "mode": 666, "owner": "avgowl", "group": "avgowl", "content": "" } }]
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_create_file_with_template(self):
        content = [{ "file": { "path": "/tmp/template-out", "template": "xxx", "vars": { "name": "Reinhard"} } }]
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_create_user(self):
        content = [{ "user": { "name": "dogmax", "shell": "/bin/bash", "home": "/home/dogmax" }}]
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_change_user_password(self):
        content = [{ "user": { "name": "dogmax", "password": "test" }}]
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_change_user_cryptpassword(self):
        content = [{ "user": { "name": "dogmax", "crypt_password": "$6$bSuz5IsFenH31JEU$A7PjEuaqnT6MWvzJvNQhg/RdXzvFNiFpAK/MsxYdsoG7WVpZDGTAjEWtEAbrXHY3yGLiBm8TjFHGIHhY2aqFW." }}] # test
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return

    def test_add_sshkey(self):
        content = [ { "user": { "name": "dogmax", "ssh_authorizedkey": "AAAAB3NzaC1yc2EAAAADAQABAAACAQC1oSy4WBYj7YAJV6CWUy8gYKM5yp2D9AZLxw7DNGJcYuoqm7kDG5+1n7JqtS0oHmQI3rIRfBjyabv5tBZRHzjReXL9URZ5mGqAqapSZtsDCLjP6WCM6RSfp2RKy00hvWBQ/NX4i9R1Pa3SM4nqoCYxNXQRVF4qL0lfeEznEL9QbLC5MYA0ywO7sZ5teezZG3PMCU5CO4hHtiEoZ2ydjRMMcygsxwxOOMWQAC6C5XHqJcmuMHrlUygb3SYcB+UYobLuq+KMAw6LE8X0ynMBw3ab2HulQYfAzmqzEj57BKybQrfJOVZd7x6X91wwFfdws0vaaxA5QDomQHJteZWm0X+RKEOchpH0/rmZ6LwntIWBDa9VVbzIS8JOVA+DL+06G4YCC4ImnDVQSMZmJoUYAwCjqi47hAfkgPb6sdRQ35NUa45w0MGyIrcYWKc1qjEwECQUf0tpz4CCG56TwP0mQVlzaiSYLtgg8Ky77AvcrCbquZNSav7xeuip0CwLbZBKbJe0c+RHcOZjImc3mlbWdw2mleM7hCUi6urB2++rVHt3PUbk51DyPMen4i6igjUiK/udKi76Ftu+8D6PVBfqbQRfeairSYMxqinggBJ1/bc+SNIyu8GwangV/UX46jqBvy2Hr/CVsa/elcFZBZtbcsQXKIGgY7s0D1xwTLPLBWFQPQ=="}} ]
        playbook = self.create_file(content)
        ansimple.main(playbook)
        return
