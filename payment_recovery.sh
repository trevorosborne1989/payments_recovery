# Payments Recovery
# Shell script to schedule application 


WORKING_DIR=/****mydirectory***/python/payments_recovery
VENV=$WORKING_DIR/venv/bin/activate

export ORACLE_HOME=/data/oracle/app/oracle/product/12.1.0/client_2
export LD_LIBRARY_PATH=/data/oracle/app/oracle/product/12.1.0/client_2/lib

source $VENV
python $WORKING_DIR/main.py
EXIT_STATUS=$?
deactivate

exit $EXIT_STATUS
