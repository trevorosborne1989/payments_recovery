import logging
import math
import time

import requests
import xml.etree.ElementTree as eTree
from xml.parsers import expat
import xmltodict
from requests.structures import CaseInsensitiveDict

from src.config.config import *


class MockPeopleSoftService:
    """
    This class accesses the SOAP services available by mockPeopleSoft PeopleSoft system. The class contains three SOAP actions:
    The request, which returns an ID for status checks, a check status query to see when results are ready, and a query
    to retrieve results. I would advise using a system like SoapUI to create your xml query with the mockPeopleSoft wsdl to
    generate each required parameter and a security header.
    """

    def __init__(self):
        self.sabhrs_trans_refs = []

    def soap_request(self, prompts):
        """
        The initial poll request for mockPeopleSoft missing warrant data.
        :param prompts: A nested list of lists containing the prompts used as search criteria (trans_ref_num). Each
                        list contains a max # of trans_ref_nums which requires a significant
                        wait time for the query. There can only be so many prompts per query as it fails otherwise.
        :return: A query ID used later to query status of results and eventually query for the results when ready.
        """
        logging.debug("Running a soap_request...")
        try:
            request_data = f"""<soapenv:Envelope xmlns:qas="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRY_SYNCPOLL_REQ_MSG.VERSION_1" xmlns:qas1="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRY_SYNCPOLL_REQ.VERSION_1" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
               <soapenv:Header><wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><wsse:UsernameToken wsu:Id="UsernameToken-F98BAEDAFBE28A04AB16433179161523"><wsse:Username>MTWS003</wsse:Username><wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Amigurumi8unn13</wsse:Password></wsse:UsernameToken></wsse:Security></soapenv:Header>
               <soapenv:Body>
                  <qas:QAS_EXEQRY_SYNCPOLL_REQ_MSG>
                     <qas1:QAS_EXEQRY_SYNCPOLL_REQ>
                        <QueryName>A_MOCK_QUERY</QueryName>
                        <isConnectedQuery>N</isConnectedQuery>
                        <OwnerType>private</OwnerType>
                        <BlockSizeKB>0</BlockSizeKB>
                        <MaxRow>0</MaxRow>
                        <OutResultType>webrowset</OutResultType>
                        <OutResultFormat>nonfile</OutResultFormat>
                        <Prompts>
                           <!--Zero or more repetitions:-->
                           <PROMPT>
                              <PSQueryName/>
                              <UniquePromptName>BIND1</UniquePromptName>
                              <FieldValue>%4765</FieldValue>
                           </PROMPT>
                           <PROMPT>
                              <PSQueryName/>
                              <UniquePromptName>BIND2</UniquePromptName>
                              <FieldValue>{prompts[0]}</FieldValue>
                           </PROMPT>
                           <PROMPT>
                              <PSQueryName/>
                              <UniquePromptName>BIND3</UniquePromptName>
                              <FieldValue>{prompts[1]}</FieldValue>
                           </PROMPT>
                           <PROMPT>
                              <PSQueryName/>
                              <UniquePromptName>BIND4</UniquePromptName>
                              <FieldValue>{prompts[2]}</FieldValue>
                           </PROMPT>
                        </Prompts>
                     </qas1:QAS_EXEQRY_SYNCPOLL_REQ>
                  </qas:QAS_EXEQRY_SYNCPOLL_REQ_MSG>
               </soapenv:Body>
            </soapenv:Envelope>
            """
            # mock the service
            # mockPeopleSoft_data = requests.post(mockPeopleSoft_web_service, headers=self.get_query_header(), data=request_data)
            mockPeopleSoft_data = mock_query_id
            # # For testing
            # # print(mockPeopleSoft_data.status_code)
            # # mockPeopleSoft_data.encoding = 'UTF-8'
            # # print(mockPeopleSoft_data.text)
            mockPeopleSoft_data_dict = self.dictionize_mockPeopleSoft_soap_response(mockPeopleSoft_data, 'request')
            print(mockPeopleSoft_data_dict)
            query_id = self.parse_query_id_dict(mockPeopleSoft_data_dict)
            return query_id

        except Exception:
            logging.debug('mockPeopleSoft soap_request failed')
            raise

    def check_query_status(self, query_id):
        logging.debug("Running check_query_status()...")
        finished = False
        try:
            request_data = f"""<soapenv:Envelope xmlns:qas="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_QUERYSTATUS_REQ_MSG.VERSION_1" xmlns:qas1="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_QUERYSTATUS_REQ.VERSION_1" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
               <soapenv:Header><wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><wsse:UsernameToken wsu:Id="UsernameToken-F98BAEDAFBE28A04AB16433018307661"><wsse:Username>MTWS003</wsse:Username><wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Amigurumi8unn13</wsse:Password></wsse:UsernameToken></wsse:Security></soapenv:Header>
               <soapenv:Body>
                  <qas:QAS_QUERYSTATUS_REQ_MSG>
                     <qas:QAS_QUERYSTATUS_REQ>
                        <qas1:PTQASWRK class="R">
                           <qas1:QueryInstanceID>{query_id}</qas1:QueryInstanceID>
                        </qas1:PTQASWRK>
                     </qas:QAS_QUERYSTATUS_REQ>
                  </qas:QAS_QUERYSTATUS_REQ_MSG>
               </soapenv:Body>
            </soapenv:Envelope>
            """

            num_attempts = 0
            while not finished:
                # mock the service
                # results = requests.post(mockPeopleSoft_web_service, headers=self.get_query_header(), data=request_data)
                results = mock_query_status
                # For testing
                # print(results.status_code)
                # results.encoding = 'UTF-8'
                # print(results.text)
                status_dict = self.dictionize_sabhrs_soap_response(results, 'check_status')
                # print(status_dict)
                status = self.parse_status_dict(status_dict)
                if status == 'success':
                    logging.debug('Sabhrs query results are ready.')
                    finished = True
                    continue
                elif status == 'running':
                    logging.debug('Sabhrs query is still running...')
                elif status == 'idnotfound':
                    logging.debug('Query instance ID not found. Cannot locate requested query')
                    raise
                elif status == 'queued':
                    logging.debug('Query is in queue and will start processing shortly')
                elif status == 'error':
                    logging.debug('Query has an error, shutting down program run')
                    raise
                # Add time in between status checks so we don't bog down SABHRS.
                time.sleep(status_check_timer)
                if num_attempts > max_attempts:
                    logging.debug('Query request timed out.')
                    raise
                else:
                    num_attempts = + 1
        except Exception:
            logging.debug('SABHRS check_query_status failed')
            raise

    def get_query_results(self, query_id):
        """
        Returns results of initial query once results are available.
        :param query_id: The id returned by the initial request.
        :return: A results dictionary.
        """
        logging.debug("Running get_query_results()...")
        try:
            request_data = f"""<soapenv:Envelope xmlns:qas="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_GETQUERYRESULTS_REQ_MSG.VERSION_1" xmlns:qas1="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_GETQUERYRESULTS_REQ.VERSION_1" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
               <soapenv:Header><wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><wsse:UsernameToken wsu:Id="UsernameToken-F98BAEDAFBE28A04AB16433019269242"><wsse:Username>MTWS003</wsse:Username><wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Amigurumi8unn13</wsse:Password></wsse:UsernameToken></wsse:Security></soapenv:Header>
               <soapenv:Body>
                  <qas:QAS_GETQUERYRESULTS_REQ_MSG>
                     <qas:QAS_GETQUERYRESULTS_REQ>
                        <qas1:PTQASWRK class="R">
                           <qas1:BlockNumber>1</qas1:BlockNumber>
                           <qas1:QueryInstance>{query_id}</qas1:QueryInstance>
                        </qas1:PTQASWRK>
                     </qas:QAS_GETQUERYRESULTS_REQ>
                  </qas:QAS_GETQUERYRESULTS_REQ_MSG>
               </soapenv:Body>
            </soapenv:Envelope>
            """
            # mock the service
            # results = requests.post(mockPeopleSoft_web_service, headers=self.get_query_header(), data=request_data)
            results = mock_query_results
            # For testing
            # print(results.status_code)
            # results.encoding = 'UTF-8'
            # print(results.text)
            results_dict = self.dictionize_sabhrs_soap_response(results, 'get_results')
            print(results_dict)
        except Exception:
            logging.debug('SABHRS get_query_status failed')
            raise
        return results_dict

    def get_query_header(self, query_type):
        """
        Selects the proper header for SOAP containing the associated SOAP action.
        :param query_type: The query type to match the header with.
        :return: A formatted header for SOAP request.
        """
        actions = {
            "normal_request": '',
            "poll_request": 'QAS_EXECUTEQRYSYNCPOLL_OPER.VERSION_1',
            "check_status": 'QAS_QUERYSTATUS.VERSION_1',
            "get_results": 'QAS_GETQUERYRESULTS_OPER.VERSION_2'
        }
        header = CaseInsensitiveDict()
        header["Content-Type"] = "application/xml"
        header["SOAPAction"] = actions.get(query_type)
        return header

    def parse_query_id_dict(self, res):
        """
        After the returned XML from the SOAP request is converted to a dict, the nested structure must be parsed for
        data.
        :param res: A nested dictionary.
        :return: The query ID used for checking status and returning results.
        """
        logging.debug('Parsing for query id')

        query_id = res['ns0:QueryInstance']['#text']

        if query_id is None:
            raise Exception('Cannot find query ID in query ID dict.')
        return query_id

    def parse_status_dict(self, res):
        """
       After the returned XML from the SOAP request is converted to a dict, the nested structure must be parsed for
       data.
       :param res: A nested dictionary.
       :return: The status .
       """
        status = res['ns0:Status']['#text']
        if status is None:
            logging.debug('Cannot find status in status dict')
            raise
        return status

    @staticmethod
    def get_prompts_for_mockPeopleSoft(mock_connection):
        """
       This method extracts trans_ref_nums from MOCK to be used for Prompts in mockPeopleSoft query.
       :param mock_connection:
       :return: A list of lists containing groups of mockPeopleSoft prompts.
       """
        logging.debug(f'Parsing sets of {max_mockPeopleSoft_query_prompts} rows from MOCK for mockPeopleSoft query...')
        i = 0
        j = 0
        count = 0
        steps = math.ceil(len(mock_connection.mock_data) / max_mockPeopleSoft_query_prompts)
        prompts = [[] for i in range(steps)]
        print(len(prompts))
        while j < steps:
            trans_ref_prompts = []
            for row in mock_connection.mock_data[i:i + max_mockPeopleSoft_query_prompts]:
                # The final slice will be out of bounds almost always. This eliminates appending an empty sequence.
                print(count)
                count += 1
                if not row:
                    continue
                print(row[0])
                trans_ref_prompts.append(row[0])
                print(trans_ref_prompts)
            prompts.append(trans_ref_prompts)
            print(prompts)
            i += max_mockPeopleSoft_query_prompts
            j += 1
        # For testing
        # print(prompts)
        # print(len(prompts))
        return [['000619800261140720210203000000', '000619800261189720210203000000',
                 '000619800261154320210203000000'], ['000619800261111220210203000000']]

    @staticmethod
    # TODO: In the bitbucket application, its converted to a string with the response.text
    # TODO: syntax which means its already converted to a string when it gets here. So you will be good
    # TODO: with passing the string XMLs that you have in the config.py file.
    # TODO: Pull over the rest of the updates from your newest branch.
    def dictionize_mockPeopleSoft_soap_response(mockPeopleSoft_data, query_type):
        """
        This method drills through the nested xml structure to the root of each unique xml query_type response. It then
        creates a nested dictionary of the remaining xml and returned data.
        :param mockPeopleSoft_data: The raw xml string to be converted to dictionary.
        :param query_type: The type of query the raw xml was returned from.
        :return: A dictionary of the retrieved mockPeopleSoft data.
        """
        xml_roots = {"poll_request": "{http://schemas.xmlsoap.org/soap/envelope/}Body/{"
                                     "http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRYSYNCPOLL_RESP_MSG"
                                     ".VERSION_1}QAS_EXEQRYSYNCPOLL_RESP_MSG/{"
                                     "http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRYSYNCPOLL_RESP_MSG"
                                     ".VERSION_1}QAS_EXEQRYSYNCPOLL_RESP/{"
                                     "http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRYSYNCPOLL_RESP.VERSION_1"
                                     "}PTQASWRK/",
                     "check_status": "{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://xmlns.oracle.com/"
                                     "Enterprise/Tools/schemas/QAS_QUERYSTATUS_RESP_MSG.VERSION_1}"
                                     "QAS_QUERYSTATUS_RESP_MSG/{http://xmlns.oracle.com/Enterprise/Tools/schemas/"
                                     "QAS_QUERYSTATUS_RESP_MSG.VERSION_1}QAS_QUERYSTATUS_RESP/{http://xmlns.oracle.com/"
                                     "Enterprise/Tools/schemas/QAS_QUERYSTATUS_RESP.VERSION_1}PTQASSTATWRK/{http://"
                                     "xmlns.oracle.com/Enterprise/Tools/schemas/QAS_QUERYSTATUS_RESP.VERSION_1}Status",
                     "get_results": "{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://xmlns."
                                    "oracle.com/Enterprise/Tools/schemas/QAS_GETQUERYRESULTS_RESP_MSG.VERSION_2}"
                                    "QAS_GETQUERYRESULTS_RESP_MSG/"
                     }
        mockPeopleSoft_root = eTree.fromstring(mockPeopleSoft_data)
        # For testing to find desired root of xml
        print(mockPeopleSoft_root)
        for child in mockPeopleSoft_root:
            print(child.tag, child.attrib)
            for step in child:
                print(step.tag, step.attrib)
                for mine in step:
                    print(mine.tag, mine.attrib)
                    for my in mine:
                        print(my.tag, my.attrib)
                        # for last in my:
                            # print(last.tag, last.attrib)
                            # for final in last:
                                # print(final.tag, final.attrib)
        mockPeopleSoft_data_xml_element = mockPeopleSoft_root.find(xml_roots.get(query_type))
        if mockPeopleSoft_data_xml_element is None:
            raise Exception(f'Error finding XML tree root for query type.')
        mockPeopleSoft_data_str = eTree.tostring(mockPeopleSoft_data_xml_element, 'UTF-8')
        return xmltodict.parse(mockPeopleSoft_data_str, 'utf-8', expat=expat, process_namespaces=False, namespace_separator=':')
