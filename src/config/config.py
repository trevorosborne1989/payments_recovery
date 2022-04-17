# email - dev and test
EMAIL_NOTIFICATIONS_HOST = 'mail.gmail.to'
EMAIL_NOTIFICATIONS_SUCCESS_RECIPIENT = "trevorosborne1989@gmail.com"
EMAIL_NOTIFICATIONS_ERROR_RECIPIENT = "trevorosborne1989@gmail.com"
EMAIL_NOTIFICATIONS_FROM = 'payments_recovery.NoReply@gmail.com'

# email - prod
# EMAIL_NOTIFICATIONS_HOST = 'mail.gmail.to'
# EMAIL_NOTIFICATIONS_SUCCESS_RECIPIENT = "trevorosborne1989@gmail.com"
# EMAIL_NOTIFICATIONS_ERROR_RECIPIENT = "ProdFailure@gmail.com"
# EMAIL_NOTIFICATIONS_FROM = 'payments_recovery.NoReply@gmail.com'

# directories - dev
WORKING_DIR = "/Users/primary/Workspace/bitbucket/trusted_software/payments_recovery"
LOCAL_LOG_DIR = WORKING_DIR + "/logs"

# directories - test
# WORKING_DIR = "/data/project/QAA/in/python/payments_recovery"
# LOCAL_LOG_DIR = WORKING_DIR + "/logs"

# directories - prod
# WORKING_DIR = "/data/project/PROD/in/python/payments_recovery"
# LOCAL_LOG_DIR = WORKING_DIR + "/logs"

# mock db - dev and test
db_user = "mock"
dsn = ' TTT99mcx'
db_pw = 'mc67thd5'

# mock db -prod
# db_user = "mock"
# dsn = ' TTT99mcp'
# db_pw = 'mf656ds6'

# mockPeopleSoft connection - dev and test
mockPeopleSoft_user = 'MTWS003'
mockPeopleSoft_password = 'Amigurumi8unn13'
mockPeopleSoft_wsdl = 'https://mockPeopleSofttst/PSIGW/PeopleSoftServiceListeningConnector/FSSY/QAS_QRY_SERVICE.1.wsdl'
mockPeopleSoft_web_service = 'https://mockPeopleSofttst/PSIGW/PeopleSoftServiceListeningConnector/FSSY'

# mockPeopleSoft connection - prod
# mockPeopleSoft_user = 'MTWS003'
# mockPeopleSoft_password = 'Amigurumi8unn13'
# mockPeopleSoft_wsdl = 'https://mockPeopleSoft/PSIGW/PeopleSoftServiceListeningConnector/FSSY/QAS_QRY_SERVICE.1.wsdl'
# mockPeopleSoft_web_service = 'https://mockPeopleSoft/PSIGW/PeopleSoftServiceListeningConnector/FSSY'

# mockPeopleSoft query - dev, test, and prod
mockPeopleSoft_query_name = 'AP_VCHR_PYMNT_INFO'
mockPeopleSoft_is_connected_query = 'N'
mockPeopleSoft_owner_type = 'private'
mockPeopleSoft_block_size_kb = '0'
mockPeopleSoft_max_row = '0'
mockPeopleSoft_output_type = 'webrowset'
mockPeopleSoft_out_result_format = 'nonfile'
mockPeopleSoft_business_unit = '1150%'
max_mockPeopleSoft_query_prompts = 3
max_attempts = 5
mock_query_id = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <soapenv:Body>
      <QAS_EXEQRYSYNCPOLL_RESP_MSG xmlns="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRYSYNCPOLL_RESP_MSG.VERSION_1">
         <QAS_EXEQRYSYNCPOLL_RESP>
            <PTQASWRK class="R" xmlns="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_EXEQRYSYNCPOLL_RESP.VERSION_1">
               <QueryInstance>f1644507-b78c-11ec-b361-3103acfac7dd</QueryInstance>
            </PTQASWRK>
         </QAS_EXEQRYSYNCPOLL_RESP>
      </QAS_EXEQRYSYNCPOLL_RESP_MSG>
   </soapenv:Body>
</soapenv:Envelope>
"""
mock_query_status = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
   <QAS_QUERYSTATUS_RESP_MSG xmlns="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_QUERYSTATUS_RESP_MSG.VERSION_1">
      <QAS_QUERYSTATUS_RESP>
         <PTQASSTATWRK class="R" xmlns="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_QUERYSTATUS_RESP.VERSION_1">
            <Status>success</Status>
            <NumColumns>21</NumColumns>
            <TotalBlocks>1</TotalBlocks>
            <TotalBytes>26590</TotalBytes>
            <TotalRows>0</TotalRows>
         </PTQASSTATWRK>
      </QAS_QUERYSTATUS_RESP>
   </QAS_QUERYSTATUS_RESP_MSG>
</soapenv:Body>
</soapenv:Envelope>
"""
mock_query_results = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
   <QAS_GETQUERYRESULTS_RESP_MSG xmlns="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_GETQUERYRESULTS_RESP_MSG.VERSION_2">
      <webRowSet xmlns="http://java.sun.com/xml/ns/jdbc">
         <properties>
            <escape-processing>true</escape-processing>
            <fetch-direction>1000</fetch-direction>
            <fetch-size>0</fetch-size>
            <isolation-level>1</isolation-level>
            <key-columns/>
            <map/>
            <max-field-size>0</max-field-size>
            <max-rows>0</max-rows>
            <query-timeout>0</query-timeout>
            <read-only>true</read-only>
            <show-deleted>false</show-deleted>
            <table-name/>
         </properties>
         <metadata>
            <column-count>21</column-count>
            <column-definition>
               <column-index>1</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Reference</column-label>
               <column-name>D.PYMNT_ID_REF</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>2</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>decode(D.PYMNT_STATUS, 'P', 'P</column-label>
               <column-name>EXPR2_2</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>3</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Date</column-label>
               <column-name>D.PYMNT_DT</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>91</column-type>
               <column-type-name>DATE</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>4</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Status</column-label>
               <column-name>D.RECON_STATUS</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>5</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Reconciled</column-label>
               <column-name>D.PYMNT_RECONCILE_DT</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>91</column-type>
               <column-type-name>DATE</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>6</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Stat/Actn</column-label>
               <column-name>E.STALEDATE_STATUS_N</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>7</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Staledt DT</column-label>
               <column-name>E.STALEDATE_DT_N</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>91</column-type>
               <column-type-name>DATE</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>8</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Action DT</column-label>
               <column-name>E.STALEDATE_ACT_DT_N</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>91</column-type>
               <column-type-name>DATE</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>9</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Tran Ref</column-label>
               <column-name>H.TRANS_REF_NBR_N</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>10</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Unit</column-label>
               <column-name>A.BUSINESS_UNIT</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>11</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>SetID</column-label>
               <column-name>F.SETID</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>12</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Remit Supp</column-label>
               <column-name>A.REMIT_VENDOR</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>13</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Supplier</column-label>
               <column-name>F.NAME1</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>14</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Voucher</column-label>
               <column-name>A.VOUCHER_ID</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>15</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Invoice</column-label>
               <column-name>B.INVOICE_ID</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>16</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>true</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Gross Amt</column-label>
               <column-name>B.GROSS_AMT</column-name>
               <schema-name/>
               <column-precision>3</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>3</column-type>
               <column-type-name>DECIMAL</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>17</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Entered</column-label>
               <column-name>B.ENTERED_DT</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>91</column-type>
               <column-type-name>DATE</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>18</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Type</column-label>
               <column-name>H.PYMNT_MT_TYPE_N</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>19</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Method</column-label>
               <column-name>A.PYMNT_METHOD</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>20</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Offset Tst</column-label>
               <column-name>H.OFFSET_TESTED_N</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
            <column-definition>
               <column-index>21</column-index>
               <auto-increment>false</auto-increment>
               <case-sensitive>false</case-sensitive>
               <currency>false</currency>
               <nullable>0</nullable>
               <signed>false</signed>
               <searchable>false</searchable>
               <column-display-size>0</column-display-size>
               <column-label>Reason</column-label>
               <column-name>A.PYMNT_HOLD_REASON</column-name>
               <schema-name/>
               <column-precision>0</column-precision>
               <column-scale>0</column-scale>
               <table-name/>
               <catalog-name/>
               <column-type>12</column-type>
               <column-type-name>VARCHAR</column-type-name>
            </column-definition>
         </metadata>
         <data>
            <currentRow>
               <columnValue>NOT PAID</columnValue>
               <columnValue>CLOSED</columnValue>
               <columnValue/>
               <columnValue>OFF</columnValue>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue>39000.000</columnValue>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
               <columnValue/>
            </currentRow>
         </data>
      </webRowSet>
      <QAS_QUERYRESULTS_STATUS_RESP xmlns="http://xmlns.oracle.com/Enterprise/Tools/schemas/QAS_QUERYRESULTS_STATUS_RESP.VERSION_2">
         <status>finalBlockRetrieved</status>
      </QAS_QUERYRESULTS_STATUS_RESP>
   </QAS_GETQUERYRESULTS_RESP_MSG>
</soapenv:Body>
</soapenv:Envelope>
"""

