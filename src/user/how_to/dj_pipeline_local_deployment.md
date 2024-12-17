(target-dj-pipeline-deployment)=
# DataJoint pipeline: On-premises deployment

This page describes the processes and resources required to deploy the [Aeon DataJoint pipeline](target-aeon-dj-pipeline) on-premises.

## Prerequisites
To deploy and operate a DataJoint pipeline, you will need the following:

1. MySQL database server (version 8.0) [configured to be DataJoint-compatible](https://github.com/datajoint/mysql-docker/blob/master/config/my.cnf)
2. Docker container (optional)
   - If you prefer using a preconfigured Docker container, [install Docker](https://docs.docker.com/engine/install/) and run:
      ```bash
      docker run -d \
         --name db \
         -p 3306:3306 \
         -e MYSQL_ROOT_PASSWORD=simple \
         -v ./mysql/data:/var/lib/mysql \
         datajoint/mysql:8.0 \
         mysqld --default-authentication-plugin=mysql_native_password
      ```
   - The above command launches a new MySQL server in a Docker container with the following credentials: 
      - Host: `localhost`
      - Username: `root`
      - Password: `simple`
   - To stop the container, run:
      ```bash
      docker stop db
      ```
3. GitHub repository containing the [codebase](aeon-mecha-github:) of the DataJoint pipeline
   - [Install the codebase](target-install-aeon-mecha). No additional modifications are needed to deploy the pipeline locally.
4. File storage
   - Provide a location for the pipeline to access/store the data files (e.g. a local directory or mounted network storage).
5. Compute environment
   - Ensure you have a compute environment with the necessary software installed to run the pipeline (e.g. a laptop, local workstation, or an HPC cluster).
6. Data to be ingested and processed
   - You may use the [Single mouse in a foraging assay](sample-data-single-mouse-foraging:) sample dataset as a starting point to test the pipeline.

## Pipeline configuration
DataJoint requires a configuration file named `dj_local_conf.json`. This file should be located in the root directory of the codebase.

1. Create the `dj_local_conf.json` file
   - Copy the `sample_dj_local_conf.json` file and rename it to `dj_local_conf.json`.
   - Update the file with your database credentials (username, password, and database host).
   - Ensure the file is kept secure and not shared publicly.
2. Set `database.prefix`
   - In the `custom` section, set `database.prefix` to your desired value, or keep the default `aeon_`.
3. Set the data directory (`ceph_aeon`)
   - In the `custom` section, set the `ceph_aeon` value (under `repository_config`) to the root directory of your data (i.e. the directory that is one level above the `raw` directory).
   - For example, if the `raw` directory is located at `D:/data/project-aeon/aeon/data/raw/`, set the `ceph_aeon` value to `D:/data/project-aeon/aeon/data`.

Now that the pipeline is installed and configured, you can start [ingesting and processing](target-dj-data-ingestion-processing) your data.