#! /usr/bin/bash
python -m venv _venv
source _venv/bin/activate
pip install conan numpy
conan --version
deactivate
