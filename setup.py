# setup.py - tiny hook to build docs into ./site)
import os
import subprocess
import sys
from pathlib import Path
from setuptools import setup, Command
from setuptools.command.sdist import sdist as _sdist

class build_docs(Command):
    """Generate documentation into ./site."""
    description = "Build project documentation into ./site"
    user_options = [
        ("clean", None, "clean the output directory before building"),
    ]

    def initialize_options(self):
        self.clean = False

    def finalize_options(self):
        self.clean = bool(self.clean)

    def run(self):
        outdir = Path("site")
        if self.clean and outdir.exists():
            import shutil
            shutil.rmtree(outdir)
        outdir.mkdir(exist_ok=True)

        # run tools here ...
        cmd = [sys.executable, "-m", "tools.expand_docs.expand_docs", "--out", str(outdir)]
        self.announce(f"Running: {' '.join(cmd)}", level=2)
        # Build environment variables if you want to pass context
        env = dict(os.environ)
        env.setdefault("PYTHONHASHSEED", "0")
        subprocess.check_call(cmd, env=env)  # fails the build on nonzero exit
        self.announce(f"Docs generated in {outdir}", level=2)

class sdist(_sdist):
    def run(self):
        # Build docs before sdist (writes to ./site but we will exclude it from sdist)
        self.run_command("build_docs")
        super().run()

cmdclass = {"build_docs": build_docs, "sdist": sdist}

setup(cmdclass=cmdclass)
