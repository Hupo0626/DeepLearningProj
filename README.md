## Environment Setup
All code was built and tested on Ubuntu 18.04 LTS with Python 2.7, Tensorflow 
1.13.1, and CUDA 10.1. Versions for other packages can be found in `requirement.txt`.

We also committed our environment to a docker image. Get it use the command below:
`docker pull hupotang/dlproj:latest`
<br>

## Run the Program
- To generate synthetic training data for the neural network:<br>`python makeSyntheticData.py 100000`
which will generate 100000 training examples in to the file `syntheticTrainingData.tar`

- To train the distance metric:<br>`python recognitionModel.py train --noisy  --distance`

- To train the proposal distribution:<br>`python recognitionModel.py train --noisy  --attention 16`

- To test the `expert-29.png` in `./drawings` folder:<br>`python recognitionModel.py test  -t drawings/expert-29.png -b 100 -l 0 --proposalCoefficient 1 --parentCoefficient --distanceCoefficient 5 --distance --mistakePenalty 10 --attention 16 --noisy --quiet`
