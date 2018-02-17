
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

    def test_install_apt_package(self):
        content = [{ "apt": { "name": "vim" } }]
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

