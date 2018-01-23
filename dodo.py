DOIT_CONFIG = {'verbosity': 2}

from ioamdoit import *

# The aim would be to not have anything much here, but right now
# that's not easy because of awkward installation/specification of
# dependencies across projects.

def task_install_pip_dependencies():
    return {'actions': ['pip install pytest-nbsmoke']}

def task_install_doc_dependencies():
    # would not need to exist if nbsite had conda package
    return {
        'actions': [
            'conda install -y -q -c conda-forge notebook ipython sphinx beautifulsoup4 graphviz selenium phantomjs',
            'pip install nbsite sphinx_ioam_theme']
        }

def task_lint():
    return {'actions': ['flake8 --ignore E,W parambokeh']}


def task_lint_nb():
    return {'actions': ['pytest --nbsmoke-lint examples/']}


def task_test_nb():
    return {'actions': ['pytest --nbsmoke-run examples/']}


def task_all_tests():
    return {'actions': [],
            'task_dep': ['lint','lint_nb','test_nb']}


def task_docs():
    # TODO: could do better than this, or nbsite could itself use doit
    # (providing a dodo file for docs, or using doit internally).
    return {'actions': [
        'nbsite_nbpagebuild.py ioam parambokeh ./examples ./doc',
        'sphinx-build -b html ./doc ./doc/_build/html',
        'nbsite_fix_links.py ./doc/_build/html',
        'touch ./doc/_build/html/.nojekyll',
        'nbsite_cleandisthtml.py ./doc/_build/html take_a_chance']}
