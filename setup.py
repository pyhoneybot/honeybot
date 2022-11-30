# black inspired
import os
import sys

from setuptools import find_packages, setup

if not (sys.version_info.major == 3 and sys.version_info.minor >= 7 and sys.version_info.micro >= 0): 
    raise Exception("honeybot requires Python 3.7.0 at least")

from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


try:
    from src.honeybot import __version__
except Exception as e:
    pass


def get_long_description() -> str:
    return (
        (CURRENT_DIR / "README.md").read_text(encoding="utf8")
    )

if sys.argv[-1] == "publish":  # requests
    os.system("python setup.py sdist")  # bdist_wheel
    os.system("twine upload dist/* --skip-existing")
    sys.exit()

setup(
    name="honeybot",
    version=__version__,
    description="IRC bot with vast collection of plugins. First timers friendly",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="irc bot plugins",
    author="Abdur-Rahmaan Janhnageer",
    author_email="arj.python@gmail.com",
    url="https://github.com/pyhoneybot/honeybot",
    project_urls={"Changelog": "https://github.com/pyhoneybot/honeybot/blob/main/CHANGES.md"},
    license="MIT",
    py_modules=[],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "honeybot": ["settings/*.conf", "*.txt"]
    },
    python_requires=">=3.7.0",
    zip_safe=False,
    install_requires=[

    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "console_scripts": [
            "honeybot=honeybot.manage:main",
        ]
    },
)
