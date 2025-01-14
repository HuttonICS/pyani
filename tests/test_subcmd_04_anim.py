#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) The James Hutton Institute 2017-2019
# (c) University of Strathclyde 2019-2024
# Author: Leighton Pritchard
#
# Contact:
# leighton.pritchard@strath.ac.uk
#
# Leighton Pritchard,
# Strathclyde Institute for Pharmacy and Biomedical Sciences,
# 161 Cathedral Street,
# Glasgow,
# G4 0RE
# Scotland,
# UK
#
# The MIT License
#
# Copyright (c) 2017-2019 The James Hutton Institute
# Copyright (c) 2019-2024 University of Strathclyde
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Test anim subcommand for pyani.

The test suite is intended to be run from the repository root using:

pytest -v
"""

import logging
import unittest

import pytest

from argparse import Namespace
from collections import namedtuple
from pathlib import Path

from pyani.scripts import subcommands


# Convenience struct with paths to third-party executables
ThirdPartyExes = namedtuple("ThirdPartyExes", "nucmer_exe filter_exe")

# Convenience struct with paths to working directories
DirPaths = namedtuple("DirPaths", "indir outdir")

# Convenience struct for label/class files
LabelPaths = namedtuple("LabelPaths", "classes labels")


class TestANImSubcommand(unittest.TestCase):
    """Class defining tests of the pyani anim subcommand."""

    def setUp(self):
        """Configure parameters for tests."""
        testdir = Path("tests")
        self.dirpaths = DirPaths(
            testdir / "test_input" / "subcmd_anim",
            testdir / "test_output" / "subcmd_anim",
        )
        self.dirpaths.outdir.mkdir(exist_ok=True)
        self.dbpath = testdir / "test_output" / "subcmd_createdb" / "pyanidb"
        self.lblfiles = LabelPaths(
            self.dirpaths.indir / "classes.txt", self.dirpaths.indir / "labels.txt"
        )
        self.exes = ThirdPartyExes("nucmer", "delta-filter")
        self.scheduler = "multiprocessing"

        # Null logger instance
        self.logger = logging.getLogger("TestIndexSubcommand logger")
        self.logger.addHandler(logging.NullHandler())

        # Command line namespaces
        self.argsdict = {
            "anim": Namespace(
                indir=self.dirpaths.indir,
                outdir=self.dirpaths.outdir,
                dbpath=self.dbpath,
                force=False,
                name="test_anim",
                classes=self.lblfiles.classes,
                labels=self.lblfiles.labels,
                recovery=False,
                cmdline="ANIm test suite",
                nucmer_exe=self.exes.nucmer_exe,
                filter_exe=self.exes.filter_exe,
                maxmatch=False,
                nofilter=False,
                scheduler=self.scheduler,
                workers=None,
                disable_tqdm=True,
                jobprefix="ANImTest",
            )
        }

    @pytest.mark.skip_if_exe_missing("nucmer")
    def test_anim(self):
        """Test anim run."""
        subcommands.subcmd_anim(self.argsdict["anim"])
