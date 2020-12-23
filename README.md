<p align="center">
  <a href="https://github.com/teddywilson/python-script-template">
    <img alt="Crane" src="crane.png" width=64 />
  </a>
</p>
<h1 align="center">
  Python Script Template
</h1>

My Python script template, because I hate rewriting these things every time. This template takes two arguments:
1. `--base_directory` Base directory under which the new project should be generated (likely your dev folder)
2. `--project` The name of the project you wish to generate

## Usage
You can execute the generation script like a normal Python script via the following: 
```
pip3 install -r requirements.txt
python generate_project.py \
  --base_directory=/Path/to/dir \
  --project=my-project
```

(Preferred) Or, you can link the script to your local bin so that you can execute it anywhere:
```
sudo ln -s $(pwd)/generate_project.py /usr/local/bin/generate_python_project
```
Two caveats about this:
* Notice that symlink name drops the `py` suffix
* `usr/local/bin` must be on your $PATH

A new project (and relevant files) will be created at `$base_directory/$project`

## Content
With this template, four files are provided:
1. `$project.py` Core script with basic main function and argument parsing set up
2. `README.md` Usage instructions, project information
3. `requirements.txt` File which dependencies will be added to
4. `.gitignore` Files to be ignored by Git
