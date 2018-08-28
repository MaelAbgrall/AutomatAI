# AutomatAI

just for fun, and also because I don't like spending all the day tweaking hyperparameters, I'll use a genetic algorithm and later a particle swarm optimisation to create neural networks

## How does it work ?
for now this is kinda spaghetti code. Depending the results I'll create later an API or a CL app

pro:
- lazy creation of a NN

- time consuming (or you need a lot of powerful hardware or small dataset and small data)

## deps & run

```shell
python35 -m venv env

source env/bin/activate

pip install -r requirements.txt

# OR

pip install -r req_dev.txt

python main.py

```

## Parameters

- Folder (In, Checkpoints, Out)

- Population size

- RAM size

- Number of GPU + DRAM

- Data shape (In, Out/validation)

- Methodology (supervised, semi-supervised)

- Stop & monitoring parameters

	- Loss or accuracy evolution (stop)

	- Delta bewteen train and validation scores (stop)

	- Maximum/minimum accuracy/loss (monitoring)

	- Data usage (semi-supervised) (monitoring)
	
	- Benchmark result ? (monitoring) / possibly highly time consuming

- Benchmarks ? (how fast is it on a cpu / gpu / arm chip)


## Hyper parameters selection

Each of those parameters can be choosen before launching the algorithm, or let the algorithm automaticaly use them in a generation

- Loss function (optionnal)

- Optimizer (optionnal)

- Layers (optionnal, not planned yet)

- Layer parameters:

	- Kernel size

	- Regularisers

	- Ititializers

	- number of connected points (FCL)

- Data generators (optionnal)

