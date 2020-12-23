#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import re
from sys import exit

PROJECT_REGEX = '[a-z\-\_]+'

GITIGNORE_CONTENT = """.DS_STORE"""

SCRIPT_CONTENT = """#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


if __name == "__main":
  parser = argparse.ArgumentParser()
  parser.add_argument('--argument', required=True)
"""

REQUIREMENTS_TXT_CONTENT = """argparse"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_directory', required=True)
    parser.add_argument('--project', required=True)
    args = parser.parse_args()

    # Validate project name
    project_pattern = re.compile(PROJECT_REGEX)
    if not project_pattern.match(args.project):
        print('Project name must match following regex: ' % PROJECT_REGEX)

    # Create the project  base_directory if it doesn't already exist
    project_directory = os.path.join(args.base_directory, args.project)
    if not os.path.exists(project_directory):
        os.makedirs(project_directory)

    f = open(os.path.join(project_directory, ".gitignore"), "w")
    f.write(GITIGNORE_CONTENT)
    f.close()

    f = open(os.path.join(project_directory, args.project + ".py"), "w")
    f.write(SCRIPT_CONTENT)
    f.close()

    f = open(os.path.join(project_directory, "requirements.txt"), "w")
    f.write(REQUIREMENTS_TXT_CONTENT)
    f.close

    print('Successfully generated new project at %s' % project_directory)
