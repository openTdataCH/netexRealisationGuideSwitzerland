# setup.py - tiny hook to build docs into ./site)
import os
import subprocess
import sys

from setuptools import setup, Command
from setuptools.command.sdist import sdist as _sdist

class build_docs(Command):

    description = "Build project documentation."
    user_options = [
        ("clean", None, "clean the output directory before building"),
    ]

    def initialize_options(self):
        self.clean = False

    def finalize_options(self):
        self.clean = bool(self.clean)

    def run(self):

        env = dict(os.environ)
        base_url = env.get("BASE_URL", "")
        cmd = [sys.executable, "-m", "tools.toolchain", "--base-url", base_url]

        self.announce(f"Running: {' '.join(cmd)}", level=2)
        # Build environment variables to pass context

        env.setdefault("PYTHONHASHSEED", "0")
        subprocess.check_call(cmd, env=env)  # fails the build on nonzero exit
        self.announce(f"Docs generated.", level=2)

class sdist(_sdist):
    def run(self):
        # Build docs before sdist (writes to ./site but we will exclude it from sdist)
        self.run_command("build_docs")
        super().run()

cmdclass = {"build_docs": build_docs, "sdist": sdist}

setup(cmdclass=cmdclass)
