import cx_Oracle
import logging
from datetime import datetime

from src.config.config import *


class OracleConnection:
    """
     This class is used to manage the data and connection to the MOCK database.

    """

    def __init__(self):
        self.mock_data = ''
        self.missing_records = []
        self.duplicates_count = 0
        self.mock_payment_update = []
        self.connection = None
        self.cursor = None

    def get_connection(self):
        """
        Established live connection with MOCK db.
        This method can use local machine's Oracle Instant Client which is commented out below.
        """
        logging.debug('Connecting to database: ' + dsn)

        # For local environment
        # cx_Oracle.init_oracle_client(lib_dir='C:/Program Files (x86)/Oracle/instantclient_21_3')

        # get a connection
        try:
            # con = cx_Oracle.connect(db_user, db_pw, dsn)
            con = 'a_mock_connection!'
        except:
            logging.debug(
                'payments_recovery' + ' : ' + datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ' : ' + 'Mock db '
                                                                                                     'connection error')
            raise

        # print("Database version:", con.version)

        # get a cursor
        # cur = con.cursor()

        # self.connection = con
        self.connection = 'a_mock_con!'
        # self.cursor = cur
        self.cursor = 'a_mock_cursor!'

    def fetch_mock(self):
        """
        Retrieve payments from MOCK that are missing warrant data between a date range.

        """
        logging.debug('Fetching Mock records missing payment data')
        query = "SELECT a.some_trans_ref_num trans_ref_num, d.payment_grp, c.mock_payment_num, " \
                " d.payment_number mock_payment_number_payment_ref, d.payment_cashed_status cashed_status, " \
                "to_char(min(d.payment_date), 'DD-MM-YYYY') as payment_date, b.batch_num, sum(b.payment_amt) " \
                "payment_amount from mock.transactions_fis c, a_batches_fis b, mock.payment_voucher d, " \
                "payment_ap_advice_1 a where t.batch_num = b.batch_num and trunc(b.process_date) " \
                "> trunc(add_months(sysdate, -1), 'month') and trunc(b.process_date) < sysdate - 13 and " \
                "d.payment_grp = c.mock_payment_num and d.payment_grp = a.adv1_payment_grp and " \
                "mock_payment_number_payment_ref is null and a.adv1_payment_method in ('CHK', 'EFT') " \
                "group by b.payment_batch_num, c.mock_payment_num, d.payment_grp, a.adv1_payment_trans_ref_num, " \
                "d.payment_number, cashed_status, payment_date order by b.payment_batch_num, d.payment_number, " \
                "a.adv1_payment_trans_ref_num"

        # self.cursor.execute(query)

        # columns = [col[0] for col in self.cursor.description]
        # self.data = self.cursor.fetchall()
        self.mock_data = (['000619800261140720210203000000', '2611407', '2611407', '9495845', 'REC', '02-07-2022',
                           '4543', '453.00'],
                          ['000619800261189720210203000000', '2611897', '2611897', '9451111', 'REC', '02-07-2022',
                           '1122',
                           '453.00'],
                          ['000619800261154320210203000000', '6115432', '6115432', '9432156', 'REC', '02-11-2022',
                           '4517',
                           '453.00'],
                          ['000619800261111220210203000000', '2611112', '2611112', '9478954', 'REC', '02-12-2022',
                           '6335',
                           '453.00'])

        # query column information
        # logging.debug(columns)

        logging.debug(f'Returning with mock data, {len(self.mock_data)} records.')

    def update_mock(self):
        """
        Update Mock with missing payment data from mockPeopleSoft. Method finishes with closing connection to Mock.

        """
        if not self.mock_payment_update:
            logging.warning('This batch of trans_ref_numbers returned 0 records from mockPeopleSoft, '
                            'skipping to next batch.')
            return
        logging.debug('Updating MOCK with missing payment data from Mock_People_Soft')
        query = """UPDATE mock.payment_voucher pv 
                    SET pv.payment_number = :pay_num, pv.payment_cashed_status = :cashed_status
                    WHERE pv.payment_grp = :group_num"""
        # self.cursor.executemany(query, self.mock_payment_update)
        # self.connection.commit()
        logging.debug('Update complete, closing MOCK connection.')
        # self.connection.close()

    def remove_duplicates(self):
        """
        A MOCK trans_ref_num will sometimes return two records from mockPeopleSoft, one usually has payment data, while
        the other is missing data. This method removes the duplicate that is missing data.

        """
        tuples_with_payment_number = [tuple_with_payment[3] for tuple_with_payment in self.mock_payment_update if
                                      tuple_with_payment[0]]
        for tuple_update in self.mock_payment_update:
            if tuple_update[3] in tuples_with_payment_number and not tuple_update[0]:
                logging.warning(f'Removing duplicate tuple with empty payment number: {str(tuple_update)}')
                self.mock_payment_update.pop(self.mock_payment_update.index(tuple_update))

    def missing_trans_refs(self, trans_refs):
        """
        Check all trans_ref_numbers returned from MOCK's original fetch and identify which ones returned zero records
        from mockPeopleSoft.
        :param mockPeopleSoft_service: The object containing trans_ref_numbers that were found in mockPeopleSoft.
        """
        for awacs_row in self.mock_data:
            self.missing_records.append(awacs_row[0]) if awacs_row[0] not in trans_refs else 0

    def summarize_load(self):
        """
        Summarizes the different update counts that will be posted to MOCK.

        """
        no_payment_number = 0
        yes_payment_number = 0
        undocumented_occurence_count = 0
        for load in self.awacs_warrant_update:
            if load[0] == '':
                no_payment_number += 1
            elif load[0] != '':
                yes_payment_number += 1
            else:
                undocumented_occurence_count += 1

        logging.debug(f"""
          
          Load Count Summary of what will be posted to AWACS:
            
            1. Date Range: {run_start_date} - {run_end_date}
            2. Count of records in MOCK missing warrant data: {len(self.mock_data)}
            3. Updates that have a warrant number in mockPeopleSoft and will be posted to AWACS: {yes_payment_number}
            4. Updates that do not have a warrant number in mockPeopleSoft but the missing status and will be posted to MOCK: {no_payment_number}
            5. Updates that have an undocumented data occurrence in mockPeopleSoft and will be posted to MOCK: {undocumented_occurence_count}
            6. Count of AWACS trans_ref_numbers that returned multiple mockPeopleSoft records: {self.duplicates_count}
            7. Summary of AWACS trans_ref_numbers that returned zero mockPeopleSoft records: {self.missing_records}
            8. Total updates to AWACS: {len(self.mock_payment_update)}
        
        """)

