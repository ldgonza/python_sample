# python_sample

Sample python project structure, base architecture and tools.

Meant  for  libraries and  small  applications  where there's  not  an
established base toolchain or  architecture. This structure should not
replace established best practices that may apply to projects based on
specific technologies.

Most  ideas extracted  verbatim  from Kenneth  Reitz's [Sample  Module
Repository](https://github.com/kennethreitz/samplemod).    Also   from
[this article](https://realpython.com/pipenv-guide/).

Features included:

- Project folder structure
- pre-populated python gitignore (Github's default)
- GPL 3.0 license
- Packaging with setup.py
- Environment managment with Pipenv
- BDD specs with mamba, expects and doublex.
- Documentation generation with sphinx.

## Use

### New project

Export the full contents of the repo into a new directory, run git init inside:

(Note: github does not allow to run 'git archive' directly against their repos).
```
$ git clone git@github.com:ldgonza/python_sample.git
$ cd python_sample
$ git archive --format=tgz HEAD > python_sample.tgz
$ mv python_sample ../ && cd ..
```

Create new directory for new project and extract all contents there:

```
$ mkdir new_project
$ mv python_sample.tgz new_project
$ cd new_project
$ tar -xzf python_sample.tgz
$ rm python_sample.tgz
```

Init git, make the first commit

```
$ git init
$ git add -a
$ git commit -m "Init project structure."
```

### Basics

Install pip, use pip to install pipenv. Then, use pipenv from the project directory.

On first checkout, get the dependencies using pipenv install. 
Then, run the program from the virtual env shell.

```
$ pipenv install
$ pipenv shell
(virtual-env-name) $ python ./python_sample/python_sample.py
```

Use pipenv install from the project directory to manage the pipfile (no need to enter the virtual env to do it). 

```
$ pipenv install mamba
```

### Project code

Replace python_sample entirely with the project's source code.

Take  note to  update pipenv's  editable install  of the  project (see
[Dependency Managment](#dependency-managment) below)  if necessary and
to update sphinx's automodule directive.

### Documentation

Modify docs/source/conf.py and docs/source/index.rst as needed.

Don't forget  to add automodule  directives to index.rst  for packages
and modules in the project:

```
.. automodule:: python_sample.python_sample
		:members:
```

Then use the MAKEFILE provided in docs/:

```
$ make html
```

### Tests

Create specs in  specs/ using mamba. File names should  have the _spec
suffix.

To run all specs in the specs/ directory:

```
$ pipenv run mamba
```

Or, to run a specific spec:

```
$ pipenv run mamba/specs/python_sample_spec.py
```

Alternatively, run mamba from inside a pipenv shell:

```
$ pipenv shell
$ mamba
```

### Single module projects

For single file/module projects, remove  the subdir and just place the
module in the root folder.

### Virtual environment

Install all dependencies by running:

```
$ pipenv install
```

Or, spawn a shell in the virtual environment with:

```
$ pipenv run <command>
```

Or, spawn a shell in the virtual environment with:

```
$ pipenv shell
```

### Dependency managment

#### Library projects

Taken from [this article](https://realpython.com/pipenv-guide/#package-distribution).

Library projects  provide a library and  are meant to be  packaged and
distributed via PyPI.

Packaging is handled through setup.py;  as a result, main dependencies
are defined there via install_requires.

The dependencies from setup.py are brought to the Pipfile by importing
the  project  as editable. This is done by the command:

```
$ pipenv install -e .
```

Other dependencies, dev dependencies in particular, are defined in the
Pipfile directly.

After updating install_requires,  to make Pipenv take note  of the new
dependencies and perform dependency resolution:

```
$ pipenv update
````

This updates Pipfile.lock as well.  To check the concrete dependencies
that have been added:

```
pipenv graph
```

Other  dependencies, particularly  dev  dependencies,  can be  defined
directly in the Pipfile or installed through:

```
pipenv install --dev <dep>
```

#### Non library projects (applications)

For non-library  projects, that is, applications,  remove setup.py and
the editable  package in the  Pipfile. Then, just  define dependencies
directly in the pipfile or through Pipenv's install command.
