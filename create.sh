#! /usr/bin/bash
source _venv/bin/activate
conan create ./creator/. --name=transitive-boost --version=1.0.0 --user=test --channel=test --build=missing --test-folder="" -pr:a=profile.txt -s build_type=Debug
