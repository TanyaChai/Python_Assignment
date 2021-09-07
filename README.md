# Python_Assignment	-  HackerNews Project

### Contents of this file

	* Introduction
	* Requisites/Installation
	* Execution
	
### Introduction

The HackerNews project fetches the top and job stories in 2 formats from https://news.ycombinator.com for user convenience. Hackernews_csv.py is used to generate a .csv file with the data fetched and hackernew_db.py is used to insert the same data into a table in sqlite database.

### Requisites/Installation

- Python 3+
- Install the python packages listed in the **requirements.txt** file.
- Enter the following command in the terminal:<br />`$ pip install -r requirements.txt`

### Execution

#### 1. To run CSV part
In the terminal enter the following command: `$python hackernews_csv.py`

#### 2. To run SQlite part
In the terminal enter the following command: `$python hackernews_db.py`

