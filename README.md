
# Branch Predictor Simulator

This project implements several branch prediction algorithms as described in the MP2 instructions.pdf
The available predictors are:
- [Smith Predictor](https://en.wikipedia.org/wiki/Smith_predictor)
- [Bimodal Predictor](https://www.cs.cornell.edu/courses/cs4110/2012fa/lectures/branch-prediction.pdf)
- [Gshare Predictor](https://inst.eecs.berkeley.edu/~cs152/fa19/lectures/Lecture14-BranchPrediction.pdf)
- [Hybrid Predictor](https://www.cs.utexas.edu/~lin/papers/hybrid-branch-predictor.pdf)

## How to Run

The main entry point is sim.py. You can run the simulator from the command line using:

```
python sim.py <predictor> <options> <trace_file>
```

### Predictor Options

- **Smith**:  
  ```
  python sim.py smith <bits> <trace_file>
  ```
  - `<bits>`: Number of bits for the counter.

- **Bimodal**:  
  ```
  python sim.py bimodal <index_bits> <trace_file>
  ```
  - `<index_bits>`: Number of bits for the index.

- **Gshare**:  
  ```
  python sim.py gshare <index_bits> <register_bits> <trace_file>
  ```
  - `<index_bits>`: Number of bits for the index.
  - `<register_bits>`: Number of bits for the global history register.

- **Hybrid**:  
  ```
  python sim.py hybrid <chooser_bits> <gshare_index_bits> <gshare_register_bits> <bimodal_index_bits> <trace_file>
  ```
  - `<chooser_bits>`: Number of bits for the chooser table.
  - `<gshare_index_bits>`: Number of bits for gshare index.
  - `<gshare_register_bits>`: Number of bits for gshare register.
  - `<bimodal_index_bits>`: Number of bits for bimodal index.

## Output

For each run, the simulator prints:
- The command used
- Number of predictions
- Number of mispredictions
- Misprediction rate
- Final contents of the predictor tables

## Validation

Validation runs and traces are available in the `validation_runs/` and traces folders. You can use these to verify correctness and compare outputs.

## Additional Information

- The project is modular, with each predictor implemented in its own file.
- Helper functions for output are in helper.py.
- Graph generation scripts are provided (graph1.py, graph2.py, graph3.py) for analysis.

---
