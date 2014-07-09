#!/bin/bash 
set -x

echo "Importing file $1 into Mongo DB"
mvn -f ../dbimport/pom.xml exec:java -Dexec.mainClass="org.jenkinsci.usagestats.dbimport.DbImport" -Dexec.args="$1"
