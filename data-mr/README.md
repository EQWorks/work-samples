## Environment

Any environment that supports `Docker Engine` (latest stable) is fine. `Docker Compose` is strongly recommended for simpler orchestration and container management. In most cases you can run Docker on your own computer with `Docker for <Your OS>`, see <https://docs.docker.com/> for instructions. The Community Edition is sufficient.

We will be using an open source [Docker Spark](https://github.com/gettyimages/docker-spark) setup provided by Getty Images for you to solve the problems in. Your problems will be around writing data processing jobs through [Apache Spark](http://spark.apache.org/). Spark has first-tier support for Scala, Java and Python languages.

## Setup

0. Make sure Docker is installed properly on the machine you wish to develop and test run your Spark job
1. Clone [`git@github.com:gettyimages/docker-spark.git`](https://github.com/gettyimages/docker-spark)
2. If you have `Docker Compose` setup properly, at the root of the cloned `docker-spark` repository, run `$ docker-compose up -d` (`-d` is to ensure it runs in daemon, or background mode)
3. Check Spark UI at `localhost://8080` and you should see 1 master and 1 worker. Should you need more worker instances (and provided `Docker Compose` is setup), simply do `docker-compose scale worker=<Number of Workers>`.

## Notes on working through the problems

If you're not already familiar with [Apache Spark](http://spark.apache.org/), you'll need to go through its documentation for available APIs. The version that comes with the Docker Spark setup is around `Spark v2.1`.

For jobs that rely on external dependencies and libraries, make sure they are properly packaged on submission. Either case, we will also need the source code of the solution, including the build instructions, such as [Maven](https://maven.apache.org/) or [SBT](http://www.scala-sbt.org/).

Make sure the jobs can be submitted (through `spark-submit` command) in the Spark Master container (you can enter its shell using `docker exec -it dockerspark_master_1 /bin/bash`). There is a `data` directory provided that maps between the Spark Master container and your host system, which is accessible as `/tmp/data` within the Docker container -- this is where you want to place both your jobs and the sample data that come with the problems.
