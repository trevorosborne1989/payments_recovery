import csv
import logging
import re
import xml.etree.ElementTree as eTree
from xml.parsers import expat
import xmltodict

from src.config.config import *


def format_mockPeopleSoft(mockPeopleSoft_queries, mock_connection):
    """
    Transforms the queried mockPeopleSoft data to a format that can import to MOCK.
    Loads tuples with mockPeopleSoft data that will be used for final SQL update.

    @:return list of tuples containing update to MOCK (payment_number, recon_status, payment_group)
    """
    logging.debug('Beginning mockPeopleSoft data transformation...')
    mockPeopleSoft_queries.dictionize_sabhrs_soap_response()

    logging.debug('Matching mockPeopleSoft data to MOCK records missing warrant data.')
    try:
        for mockPeopleSoft_row in mockPeopleSoft_queries.mockPeopleSoft_xml_dict['ns0:query']['ns0:row']:
            for mock_row in mock_connection.mock_data:
                trans_ref = str(mock_row['ns0:TRANS_REF_NBR_N'])
                try:
                    payment_id_ref = str(mock_row['ns0:PYMNT_ID_REF'])
                except KeyError as err:
                    logging.debug(f'{err}: Record with TRANS_REF_NBR_N = {trans_ref} is missing PYMT_ID_REF in mockPeopleSoft '
                                  f'which is payment number in MOCK')
                    payment_id_ref = ''
                try:
                    recon_status = str(mock_row['ns0:RECON_STATUS'])
                except KeyError as err:
                    logging.debug(f'{err}: Record with TRANS_REF_NBR_N = {trans_ref} is missing status in mockPeopleSoft')
                    recon_status = ''
                if trans_ref == str(mock_row[0]):
                    logging.debug('Matched and appending ' + str(mock_row))
                    # Extract vou_hdr_warrant_grp from trans_ref_nbr_n
                    payment_group = trans_ref[2: 7]
                    # Remove padding from PYMNT_ID_REF which will be MOCK missing warrant number
                    payment_number = str([pad.lstrip('0') for pad in payment_id_ref])
                    payment_tuple = (payment_number, recon_status, payment_group)
                    logging.debug('Matched and appending missing payment data: ' + trans_ref + str(payment_tuple))
                    mock_connection.mock_payment_update.append(payment_tuple)
    except KeyError as err:
        logging.debug('MOCK is not missing any warrant data.')
