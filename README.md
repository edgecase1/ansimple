# Summary
This is a toy project to implement a simple pure-python server provisioning system.
It should only use pure-python3 without additional dependencies installed.

It has plug-ins for:
- apt
- file templates 

# Usage
```
./ansimple.py playbook.json
```

# Playbooks
The input file is a JSON file. It is a sorted list of items. Each item has a single key that denotes the provider and a dict containing the options.

## Packages
Install a package (e.g. with apt-get).
```
[
  { "package":{ "name": "git" }},
]
```
## file via template and change
```
[
  { "file":{ "path": "/tmp/xxx", "owner": "root", "mode": 755, "content": "AAAA" }} 
  { "file":{ "path": "/tmp/withtemplate", "vars": {"name": "Reinhard"} }}
]
```
# User
```
[
  { "user":{ "name": "avgowl", "home": "/home/avgowl", "shell": "/bin/bash"} }}
]
```


# run tests
A test suite tests all important functions to safely implement changes.
```
python3 -m unittest testsuite
```
