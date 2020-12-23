# Python Script Template

My Python script template, because I hate rewriting these things every time. This template takes two arguments:
1. `--base_directory`: The base directory under which the new project should be generated (likely your dev folder)
2. `--project`: The name of the project you wish to generate

## Usage
```
pip3 install -r requirements.txt
python generate_project.py \
  --base_directory=/Path/to/dir \
  --project=my-project
```

## Content
With this template, four files are provided:
1. `$project.py` Core script with basic main function and argument parsing set up
2. `README.md` Usage instructions, project information
3. `requirements.txt` File which dependencies will be added to
4. `.gitignore` Files to be ignored by Git
