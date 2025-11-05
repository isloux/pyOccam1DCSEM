# Gemini Code Understanding

## Project Overview

This project, `pyOccam1DCSEM`, is a Python package for 1D controlled-source electromagnetic (CSEM) forward modeling. It acts as a Python wrapper for the Fortran-based Occam1DCSEM code originally developed by Kerry Key. The package allows users to define models, run simulations, and process the output using Python.

The core of the project consists of a Fortran library for the heavy numerical computations, and a Python interface for user interaction, data handling, and visualization.

## Building and Running

The project uses a custom `setup.py` script that handles the configuration, compilation of the Fortran code, and installation of the Python package.

### Building the Project

1.  **Configure the build:**
    This step prepares the project for compilation and sets the installation path for the compiled library.

    ```bash
    python3 setup.py configure --prefix=<lib_installation_path>
    ```

2.  **Compile the Fortran library:**
    This command compiles the Fortran source code into a shared library that the Python code can call.

    ```bash
    python3 setup.py lib
    ```

3.  **Install the Python package:**
    This will install the `pyoccam1dcsem` package, making it available in your Python environment.

    ```bash
    pip3 install .
    ```

### Running a Simulation

1.  **Generate a RUNFILE:**
    The `occamfile` module can be used to generate a sample `RUNFILE`, which contains the parameters for the simulation.

    ```bash
    python3 -m pyoccam1dcsem.occamfile
    ```

2.  **Run the forward model:**
    The `dipole` module executes the forward model using the parameters defined in the `RUNFILE`.

    ```bash
    python3 -m pyoccam1dcsem.dipole
    ```

## Development Conventions

*   **Languages:** The project uses a combination of Python for the high-level interface and Fortran for the core numerical modeling.
*   **Build System:** The build process is managed by a `distutils`-based `setup.py` script with custom commands, along with `autoconf` and `automake` for the Fortran component.
*   **Dependencies:** The Python code relies on `pandas` for data manipulation and `matplotlib` for plotting.
*   **Code Structure:**
    *   `setup.py`: The main entry point for building and installing the project.
    *   `pyoccam1dcsem/`: The main Python package directory.
        *   `src/`: Contains the Fortran source code.
        *   `dipole.py`: Defines the `Dipole` class, which is the main interface to the Fortran library.
        *   `occamfile.py`: Provides tools for reading and writing the "Occam" file format used for input and output.
*   **Testing:** A `test` directory exists within the `pyoccam1dcsem` package, suggesting that tests are available, but the `README.md` does not specify how to run them.
