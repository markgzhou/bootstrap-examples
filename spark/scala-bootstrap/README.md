# Spark-Scala-Example-Project

A simple Scala project that you can build and run in Spark immediately.

Here are the steps to run:

Run `./gradlew clean sJ` to build jar file.

To test local spark, run `spark-submit --class "com.examples.GetStarted" --master local[2] build/libs/spark-java-example-for-databricks-shadow.jar /tmp/test_output`
