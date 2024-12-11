# This file should be run once env_c is activate from the ~/.venv dir
import sys
import flask

print(f"This is program {__file__}")
print(f"The Python version is {sys.version}")
print(f"The Flask version is {flask.__version__}")