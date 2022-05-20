LOGS="pip_install.log"
PATH_GIT_URL="https://github.com/jaraco/path.git"
VENV_DIR="local_lib"
SMALL_PROGRAM="my_program.py"

# setup venv
python3.10 -m venv $VENV_DIR
source $VENV_DIR/bin/activate
pip --version


pip install --log $LOGS --force-reinstall git+$PATH_GIT_URL &&
    python "my_program.py"
