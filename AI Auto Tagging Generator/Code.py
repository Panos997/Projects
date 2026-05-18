!rm -rf /content/Projects
!git clone https://github.com/Panos997/Projects.git /content/Projects
%cd "/content/Projects/AI Auto Tagging Generator"
!pip install -r requirements.txt


import sys
sys.path.append("/content/Projects")

from importlib import import_module

ui = import_module("AI Auto Tagging Generator.ui")
ui.run_app()
