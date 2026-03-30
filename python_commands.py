commands = """

1. Running Python
	- python3 script.py - Run a Python script.
	- python3 - Start the Python interactive shell.
	- python3 --version - Show the installed Python version.
	- which python3 - Show the path to the Python 3 executable.
	- python3 -m module_name - Run a module as a script.

2. Packages & pip
	- python3 -m pip --version - Show the pip version tied to Python 3.
	- python3 -m pip install <package> - Install a package.
	- python3 -m pip uninstall <package> - Remove a package.
	- python3 -m pip list - List installed packages.
	- python3 -m pip freeze - Show installed packages in requirements format.

3. Virtual Environments
	- python3 -m venv .venv - Create a virtual environment in .venv.
	- source .venv/bin/activate - Activate the virtual environment.
	- deactivate - Exit the virtual environment.
	- which python - Show which Python is active inside the venv.
	- python --version - Show the active Python version inside the venv.

4. Useful One-Liners
	- python3 -c "print('hello')" - Run a short Python command.
	- python3 -c "import sys; print(sys.version)" - Print full Python version info.
	- python3 -c "import sys; print(sys.executable)" - Show the exact interpreter path.
	- python3 -m http.server 8000 - Start a simple web server in the current directory.

5. Files & Modules
	- python3 file.py - Run a local Python file.
	- python3 -m unittest - Run unit tests with unittest.
	- python3 -m venv env - Create a virtual environment named env.
	- python3 -m pip install -r requirements.txt - Install dependencies from a requirements file.
"""

print(commands)
