echo [$(date)]: "START"

echo [$(date)]: "creating the environment with python=3.8 version"

conda create -p venv python=3.8 -y

echo [$(date)]: "activating the environment"

conda activate "D:\Machine Learning\Gemstone-Quality-Checker-ML-Algorithm\venv"

echo [$(date)]: "Installing the dev requirements"

pip install -r requirements_dev.txt

echo [$(date)]: "END"


