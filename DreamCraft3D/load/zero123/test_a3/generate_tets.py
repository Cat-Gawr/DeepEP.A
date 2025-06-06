import os

import numpy as np

"""
This code segment shows how to use Quartet: https://github.com/crawforddoran/quartet,
to generate a tet grid
1) Download, compile and run Quartet as described in the link above. Example usage `quartet meshes/cube.obj 0.5 cube_5.tet`
2) Run the function below to generate a file `cube_32_tet.tet`
"""


def generate_tetrahedron_grid_file(res=32, root=".."):
    frac = 1.0 / res
    command = f"cd {root}; ./quartet meshes/cube.obj {frac} meshes/cube_{res}_tet.tet -s meshes/cube_boundary_{res}.obj"
    os.system(command)


"""
This code segment shows how to convert from a quartet .tet file to compressed npz file
"""


def convert_from_quartet_to_npz(quartetfile="cube_32_tet.tet", npzfile="32_tets"):
    file1 = open(quartetfile, "r")
    header = file1.readline()
    numvertices = int(header.split(" ")[1])
    numtets = int(header.split(" ")[2])
    print(numvertices, numtets)

    # load vertices
    vertices = np.loadtxt(quartetfile, skiprows=1, max_rows=numvertices)
    print(vertices.shape)

    # load indices
    indices = np.loadtxt(
        quartetfile, dtype=int, skiprows=1 + numvertices, max_rows=numtets
    )
    print(indices.shape)

    np.savez_compressed(npzfile, vertices=vertices, indices=indices)


root = "/home/gyc/quartet"
for res in [300, 350, 400]:
    generate_tetrahedron_grid_file(res, root)
    convert_from_quartet_to_npz(
        os.path.join(root, f"meshes/cube_{res}_tet.tet"), npzfile=f"{res}_tets"
    )
