# A Comparative Analysis of Collaborative and Content-Based Filtering for Book Recommendation Systems
## Data Ingestion Project


## Application Structure

- dags: contains the main dags used by airflow
- database/scripts: useful scripts
- database/setup: database creation scripts used by postgres database startup
- database/views: views used to extract/aggregate etl data;
- tests: all tests (could add more - copilot used)

## Running the application

**Notes:**

- A Makefile was used to facilitate the commands usage. For more details please open the file in the root folder.
- All the commands were tested in a unix environment. It currently doesn't support any other environment.


### How to run airflow and dependencies
Install dependencies, virtual environment and start airflow setup/configuration
```bash
make install
```

Startup all services
```bash
make up
```

## How to run tests
First is required to install the test dependencies:
```bash
make install-tests
```

Then, run pytests using the following command
```bash
make tests
```

## How to clean up
After the execution and all validations, please run the following command to cleanup your environment and free some space :)
```bash
make cleanup
```

# Next and missing steps
- Add comments;
- Add more tests;
- Setup better credentials/secrets mechanism - Unfortunately I didn't have too much time at this point;
- Add a dashboards/visualization tool to make the information more clear and understandable;
- In case of usage of large dataset would be useful to use a large machine and improve the algorithms;
- Use kubernetes + terraform + any other tool to better setup the environment.