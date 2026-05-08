from __future__ import print_function, absolute_import, division  # makes KratosMultiphysics backward compatible with python 2.6 and 2.7
import json
import sys
from argparse import ArgumentParser



import numpy as np
import os



import KratosMultiphysics
from KratosMultiphysics.StructuralMechanicsApplication.structural_mechanics_analysis import StructuralMechanicsAnalysis
import sys

from pathlib import Path


if __name__ == "__main__":
    with open("problem.json", "r") as kratos_input:
        parameters = KratosMultiphysics.Parameters(kratos_input.read())

    model = KratosMultiphysics.Model()
    simulation = StructuralMechanicsAnalysis(model, parameters)
    simulation.Run()