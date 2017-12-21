### BMI 6018-2017 Intro to Programming Term Project

### Introduction

The dataset "Education and Related Statistics for the U.S. States" is from United States (1992) Statistical Abstract of the United States. Bureau of the Census. The States data frame has 51 rows and 8 columns. The observations are the U. S. states and Washington, D. C.

This data frame contains the following columns: 
* region
  -- U. S. Census regions. A factor with levels: ENC, East North Central; ESC, East South Central; MA, Mid-Atlantic; MTN, Mountain; NE, New England; PAC, Pacific; SA, South Atlantic; WNC, West North Central; WSC, West South Central. 
* pop
  -- Population: in 1,000s. 
* SATV
  -- Average score of graduating high-school students in the state on the verbal component of the Scholastic Aptitude Test (a standard university admission exam). 
* SATM
  -- Average score of graduating high-school students in the state on the math component of the Scholastic Aptitude Test. 
* percent
  -- Percentage of graduating high-school students in the state who took the SAT exam. 
* dollars
  -- State spending on public education, in \$1000s per student. 
* pay
  -- Average teacher's salary in the state, in $1000s. 

The dataset was used for statistical analysis and linear regression.


### Files

* 6018-2017_project_main.ipynb: Main project file.
* 6018-2017_project_main.py: Main project file.
* sat_machine_learning.ipynb: Analysis data and all figures.
* sqlite_module.py: python sqlite module.
* satpkg: python package 


### Requirement:

- Python 3.6.1
- Jupyter Notebook 5.0.0
- pandas 0.20.1
- matplotlib 2.0.2
- numpy 1.12.1
- sklearn 0.19.1
- PyQt5