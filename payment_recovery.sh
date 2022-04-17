# Warrant Recovery
# This shell script is meant to be run from Control-M at 7:15am Mon-Fri. 
# This app calls a number of stored procedures which update the AWACS and
# CCUBS databases with the warrant status return file records from SABHRS


WORKING_DIR=/data/project/batch/SFSLBATCH/MTPROD/sfslin/python/warrant_recovery
VENV=$WORKING_DIR/venv/bin/activate

export ORACLE_HOME=/data/oracle/app/oracle/product/12.1.0/client_2
export LD_LIBRARY_PATH=/data/oracle/app/oracle/product/12.1.0/client_2/lib

source $VENV
python $WORKING_DIR/main.py
EXIT_STATUS=$?
deactivate

exit $EXIT_STATUS
