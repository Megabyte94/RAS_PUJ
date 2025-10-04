# Taken from https://computationalmechanics.in/obtaining-volume-centre-of-gravity-and-inertia-matrix-from-stl-file/

import numpy as np
from pathlib import Path
from stl import mesh

# Using an existing closed stl file:
mesh_path = (Path(__file__).resolve().parent / "ros_package" / "urdf" / "mesh" / "copi_l_sho.stl")

try:
	your_mesh = mesh.Mesh.from_file(mesh_path.as_posix())
except FileNotFoundError as exc:
	raise FileNotFoundError(f"Mesh file not found at '{mesh_path}'." ) from exc

# Original STL is in millimeters. Convert results to meters-based units.
volume_mm3, cog_mm, inertia_mm = your_mesh.get_mass_properties()
scale = 1e-3  # m per mm
volume = volume_mm3 * scale**3        # m^3
cog = cog_mm * scale                  # m
inertia = inertia_mm * scale**5       # kg·m^2 for unit density (1 kg/m^3)
print("Volume                                  = {0}".format(volume))
print("Position of the center of gravity (COG) = {0}".format(cog))
# Inertia matrix: computed with implicit density=1. Units follow STL length units.
# If STL coords are meters and you later multiply by material density (kg/m^3),
# result will be in kg·m^2. Otherwise scale geometry first.
print("Inertia matrix at COG (unit density)    = {0}".format(inertia[0,:]))
print("                                          {0}".format(inertia[1,:]))
print("                                          {0}".format(inertia[2,:]))