import os
import pkg_resources

_package_name = "honeybot"


def prevent_none(x):
    return x if x else ""


def configfile_to_list(settings_path, filename):
    elements = []
    with open(os.path.join(settings_path, "{}.conf".format(filename))) as f:
        elements = f.read().split("\n")
        elements = list(filter(lambda x: x != "", elements))
    return elements


def get_requirements():
    package = pkg_resources.working_set.by_key[_package_name]
    return [str(r) for r in package.requires()]
