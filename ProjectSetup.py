import os
import sys
import venv

def create_venv(project_name):
    """
    Create a new virtual environment directory for a new project and activate it.

    :param project_name: Name of the project.
    """
    venv_dir = os.path.join(os.getcwd(), project_name)
    if not os.path.exists(venv_dir):
        os.makedirs(venv_dir)

    # Create the virtual environment
    try:
        venv.create(venv_dir, with_pip=True)
    except Exception as e:
        print(f"Error creating virtual environment: {e}")
        sys.exit(1)

    # Activate the virtual environment
    activate_script = os.path.join(venv_dir, "Scripts", "activate")
    if sys.platform == "win32":
        activate_script += ".bat"
    else:
        activate_script += ".sh"
    try:
        os.system(f"source {activate_script}")
    except Exception as e:
        print(f"Error activating virtual environment: {e}")
        sys.exit(1)

    print(f"Virtual environment created and activated at {venv_dir}")

if __name__ == '__main__':
    project_name = input("Enter project name: ")
    create_venv(project_name)