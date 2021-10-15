# Benchmarks data for "Qubit routing via lazy synthesis"

This repo contains benchmark data and circuits for the paper [Qubit routing via lazy synthesis](https://arxiv.org/abs/2012.09663).

## Folder `./circuits`


This folder contains circuits produced by the benchmark of arithmetic circuits. All circuits are stored in myQLM binary format.

Each circuits comes in 9 forms:
- suffix `_init`: the initial circuit
- suffix `_swap`: after compilation using the first method of the paper (SWAP insertion)
- suffix `_linear`: after compilation using the second method of the paper (GL(n, F2) method)
- suffix `_clifford`: after compilation using the thirf method of the paper (Clifford method)
- suffix `_clifford1`: after compilation using the third method of the paper with reordering (Clifford\star method)
- suffix `_clifford2`: after compilation using the third method of the paper with merging (Clifford\dagger method)
- suffix `_clifford3`: after compilation using the third method of the paper with reordering and merging (Clifford\star\dagger method)
- suffic `_cowtan`: after compilation using the tket compiler (with initial mapping deactivated) (cowtan method in the paper)
- suffic `_staq`: after compilation using the Staq compiler (no initial mapping optimization, pre-processed by Zhang & Chen algorithm)

The target architecture is specified by the prefix (`Aspen_`, `Melbourne_`, or `ATA_`).

The file `load_circuit.py` contains a simple script that loads a circuit, displays its gates and some statistics (gate count, etc).

For instance:
```bash
python3 load_circuit.py circuits/Aspen_qft_4.qc_clifford3.circ
```

The script requires myqlm to be installed:

```bash
virtualenv myqlm
source ./myqlm/bin/activate
python3 -m pip install myqlm
```

## Arithemtic circuit benchmark

The result of this benchmark are stored in `./raw_data/arith.dat` in pickle format.

They can be loaded and displayed using the `./display_bench_arith` script.

## QAOA circuit benchmarks

The result of this benchmark are stored in `./raw_data/qaoa.dat` in pickle format.

They can be loaded and displayed using the `./display_bench_qaoa` script.

## Random Pauli rotation circuits

The result of this benchmark are stored in `./raw_data/paulis.dat` in pickle format.

They can be loaded and displayed using the `./display_bench_paulis` script.
