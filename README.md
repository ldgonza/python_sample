# python_sample

For single file/module projects, remove the subdir and just place the module in the root folder.

To run all specs

pipenv run mamba

For library projects, define dependencies in setup.py. The editable
package dependency in the pipfile makes pipenv load the library as a
dependency and pull it's own dependencies from it.

To update the pipenv, pipenv lock and install all dependencies:
update install_requires in setup.py
run

pipenv update

Check that the dependencies have been updated with
pipenv graph

Other dependencies, particularly dev dependencies, can be defined directly in the pipfile.

For non-library projects, remove setup.py and the editable package and define all dependencies directly in the pipfile.

