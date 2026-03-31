commands = """

1. Running Python
	- python3 script.py - Run a Python script.
	- python3 - Start the Python interactive shell.
	- python3 -i script.py - Run a script, then stay in interactive mode.
	- python3 --version - Show the installed Python version.
	- which python3 - Show the path to the Python 3 executable.
	- python3 -m module_name - Run a module as a script.
	- python3 -m site - Show Python site-packages and related paths.

2. Packages & pip
	- python3 -m pip --version - Show the pip version tied to Python 3.
	- python3 -m pip install <package> - Install a package.
	- python3 -m pip install --upgrade <package> - Upgrade a package.
	- *python3 -m pip uninstall <package> - Remove a package.
	- python3 -m pip list - List installed packages.
	- python3 -m pip freeze - Show installed packages in requirements format.
	- python3 -m pip show <package> - Show details about an installed package.
	- python3 -m pip install -r requirements.txt - Install dependencies from a requirements file.
	- python3 -m pip wheel <package> - Build a wheel for a package.

3. Virtual Environments
	- python3 -m venv .venv - Create a virtual environment in .venv.
	- source .venv/bin/activate - Activate the virtual environment.
	- deactivate - Exit the virtual environment.
	- which python - Show which Python is active inside the venv.
	- python --version - Show the active Python version inside the venv.
	- python -m pip list - List installed packages in the active venv.
	- *rm -r .venv - Delete the virtual environment directory.

4. Builds, Checks & Packaging
	- python3 -m py_compile file.py - Check that a Python file compiles.
	- python3 -m compileall . - Compile all Python files under the current directory.
	- python3 -m build - Build source and wheel distributions for a project.
	- python3 -m setuptools --help - Show setuptools help, if available.
	- python3 setup.py sdist bdist_wheel - Build source and wheel packages for older projects.
	- python3 -m ensurepip --upgrade - Install or upgrade pip in the current Python.

5. Useful One-Liners
	- python3 -c "print('hello')" - Run a short Python command.
	- python3 -c "import sys; print(sys.version)" - Print full Python version info.
	- python3 -c "import sys; print(sys.executable)" - Show the exact interpreter path.
	- python3 -c "import os; print(os.getcwd())" - Print the current working directory.
	- python3 -c "import json; print(json.dumps({'x': 1}, indent=2))" - Pretty-print JSON from a one-liner.
	- python3 -m http.server 8000 - Start a simple web server in the current directory.

6. Testing, Formatting & Quality
	- python3 -m unittest - Run unit tests with unittest.
	- python3 -m unittest discover - Discover and run tests automatically.
	- pytest - Run tests with pytest, if installed.
	- pytest -k <pattern> - Run pytest tests matching a pattern.
	- python3 -m doctest -v file.py - Run doctests in a file.
	- black . - Format Python code with Black, if installed.
	- ruff check . - Run Ruff lint checks, if installed.
	- ruff format . - Format Python code with Ruff, if installed.

7. Files & Modules
	- python3 file.py - Run a local Python file.
	- python3 -m venv env - Create a virtual environment named env.
	- python3 -m package.module - Run a module inside a package.
	- python3 -m pdb file.py - Debug a script with the built-in debugger.
	- python3 -m timeit "'-'.join(['a', 'b'])" - Benchmark a small Python expression.
	- python3 -m zipapp myapp - Create a runnable .pyz archive from a directory.

8. Project Introspection
	- python3 -m sysconfig - Show Python build and install configuration info.
	- python3 -c "import sys; print(sys.path)" - Show the module search path.
	- python3 -c "import platform; print(platform.python_implementation())" - Show the Python implementation.
	- python3 -m pydoc str - Open built-in documentation for an object or module.
	- python3 -m pip check - Verify installed packages have compatible dependencies.
"""

print(commands)
