# Haochong-individual-3 [![CI](https://github.com/nogibjj/Haochong-Individual-3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Haochong-Individual-3/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Individual Project 4. First of all, I create `app.py` as my Flask app. After that, I create a templete called `index.html` to show my UI. Finally, I use Azure Web App Service to deploy my app, and I use Action to run `Makefile` and got a 100% pass. 

Important files:
* `app.py`
* `index.html`
* `Dockerfile`
* `.env`(hidden)
* `requirements.txt`

## Purpose
- build a publicly accessible auto-scaling container using Azure App Services and Flask.



## Preparation 
1. Add more packagesinto the `requirement.txt`
2. Create repo on github and clone it to local
2. Log into Azure and DockerHub 

## App Introduction
- This app is a simple web app that can provide you health suggestions. It includes following features:
1. A title indicates the purpose of this app
2. A button to select what kind of health suggestions you want to get
3. A button to generate the suggestions
4. Powered by GPT 3.5 Turbo, which has been meticulously fine-tuned to replicate the role of a consultant providing health suggestions, either psysical or mental.

## Key steps:
1. Git clone the repo to local:
- Allows me to create, run and test my code.

2. Get my OpenAI API key:
- Get my OpenAI API key from their website, create an `.env` file and set up `OPENAI_APIKEY`

![Alt text](apikey.png)

3. Transform and load data:
- Transform the csv files into a Spark dataframe which are then converted into Delta Lake Tables and stored in the Databricks environement.

4. Query Transformation and Vizulization:
- Defines a Spark SQL query to perform a predefined transformation on the data. Then, uses the predifined transformation Spark dataframe to create vizualizations.

5. File Path Checking for `make test`:
- Implements a function to check if a specified file path exists in the Databricks FileStore and test whether the Databricks API is still connected. Use databricks to double check if the csv files and delta tables are created and stored in the right place.

![Alt text](Filestore.png)

![Alt text](<delta tables.png>)

6. Clone repo into Databricks workspace:
- Clone the repo into the Databricks workspace by using the UI. Make sure the repo was pulled successfully with the latest changes.

7. Create a new cluster
- Create a new cluster in databricks and run `make install` to install all the packages in the cluster, then run the code inside databricks to make sure they work before create a pipline.

8. Create a new job to build a pipeline with automated trigger
- Create a new job to build a pipeline in databricks and set up the automated trigger. Then, run the pipeline to see if it works.

![Alt text](pipeline.png)

9. Create secrets in Github:
- Create secrets in Github to store the `SERVER_HOSTNAME`, `TOKEN` and `JOB_ID`.

![Alt text](secrets.png)





## Video demo link:


## Reference:



