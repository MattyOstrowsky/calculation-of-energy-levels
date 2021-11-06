# Calculation of energy levels

<img align="right" width="33%" src="https://cdn-icons.flaticon.com/png/512/3658/premium/3658207.png?token=exp=1636211377~hmac=b9d1579e0007bd506a8abeff161d1ea1">

## Table of contents

* [General info](#general-info)
* [Installation](#installation)
* [How to run it](#how-to-run-it)
* [License](#license)

## General info
Program that allows you to set levels
energy (and corresponding wave functions) of the media in one-dimensional
GaAs/AlGaAs semiconductor quantum well.

## Installation

1. Git clone repository:
```bash
$ git clone https://github.com/gunater/calculation-of-energy-levels.git
```
2. Install the necessary python dependencies you can use `pipenv`:
```bash
$ pipenv install
$ piipenv shell
```
or you can install from requirements.txt with `pip`:
```bash
$ pip install -r requirements.txt
```
## How to run it
To run the script, go to the main directory:
```bash
$ cd project/
```
and then run script with:
```bash
$ python3 main.py
```
The program will run with a sample batch file structure.txt and you will get output:
```bash
effective mass of heavy holes = 1.422
edge of valence band = -0.8
effective mass of electron = 0.067
effective mass of heavy holes = 0.327
effective mass of light holes = 0.09


name:AlAs
effective mass of heavy holes = 3.003
edge of valence band = -1.33
effective mass of electron = 0.124
effective mass of heavy holes = 0.51
effective mass of light holes = 0.18


name:AlGaAs
effective mass of heavy holes = 1.8404399999999999
edge of valence band = -0.959
effective mass of electron = 0.0841
effective mass of heavy holes = 0.3819
effective mass of light holes = 0.11699999999999999


Process finished with exit code 0
```
## License
All code is licensed under an MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.

