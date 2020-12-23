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
    parser.add_argument('--directory', required=True)
    parser.add_argument('--project', required=True)
    args = parser.parse_args()

    # Validate project name
    project_pattern = re.compile(PROJECT_REGEX)
    if not project_pattern.match(args.project):
        print('Project name must match following regex: ' % PROJECT_REGEX)

    # Create the project  directory if it doesn't already exist
    if not os.path.exists(args.output_dir):
        print('Creating new directory %s' % args.output_dir)
        os.makedirs(args.output_dir)

    f = open(os.path.join(args.output_dir, ".gitignore", "w")
    f.write(GITIGNORE_CONTENT)
    f.close()

    f = open(os.path.join(args.output_dir, args.project + ".py", "w")
    f.write(SCRIPT_CONTENT)
    f.close()

    f = open(os.path.join(args.output_dir, "requirements.txt", "w")
    f.write(REQUIREMENTS_TXT_CONTENT)
    f.close

