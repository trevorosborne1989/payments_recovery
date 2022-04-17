from src.services.MockPeopleSoftService import *
from src.utils.OracleConnection import *
from src.utils import utils
from src.utils.format_mockPeopleSoft import format_mockPeopleSoft
from src.utils.utils import *

from src.config.config import *


def main():
    email_subject = None
    log_name = configure_logging()
    logging.info("Starting payments_recovery")
    test = 0
    try:
        try:
            # This object has connection and cursor properties
            mock_connection = OracleConnection()
            mock_connection.get_connection()
        except Exception:
            logging.exception(
                "Exception raised during get_connection()")
            email_subject = "payments_recovery failed on get_connection()"
            raise

        # Find records missing warrant data from MOCK database
        try:
            mock_connection.fetch_mock()
        except Exception:
            logging.exception(
                "Exception raised during fetch_mock")
            email_subject = "payments_recovery failed on fetch_mock()"
            raise

        # Retrieve prompts for mockPeopleSoft query using trans_ref_nbr from MOCK
        mockPeopleSoft_service = MockPeopleSoftService()
        try:
            prompts = mockPeopleSoft_service.get_prompts_for_mockPeopleSoft(mock_connection)
        except Exception:
            logging.exception(
                "Exception raised during get_prompts_for_mockPeopleSoft()")
            email_subject = "payments_recovery failed on get_prompts_for_mockPeopleSoft()"
            raise

        # Start a batch process. Max # of records per batch and the next batch doesn't start until
        # the preceding one finishes an update to the MOCK database. This allow for the process to not have to start
        # all over if there is a failure processing a portion of all the returned mockPeopleSoft data.
        logging.debug('Batch process starting')
        for prompts_per_query in prompts:
            try:
                # Get mockPeopleSoft data
                query_id = mockPeopleSoft_service.soap_request(prompts_per_query)
                mockPeopleSoft_service.check_query_status(query_id)
                mockPeopleSoft_data = mockPeopleSoft_service.get_query_results(query_id)
            except Exception:
                logging.exception(
                    "Exception raised during soap_request()")
                email_subject = "payments_recovery failed on soap_request()"
                raise

        # Transform and filter the mockPeopleSoft data
        try:
            format_mockPeopleSoft(mockPeopleSoft_data, mock_connection)
        except Exception:
            logging.exception(
                "Exception raised during transform_mockPeopleSoft")
            email_subject = "payments_recovery failed on transform_mockPeopleSoft"
            raise

        mock_update = [
            (1234, 'REC', 2611407),
            (1234, 'REC', 2611839),
            (1234, 'REC', 2612652)
        ]

        # Update MOCK
        try:
            mock_connection.update_mock(mock_update)
        except Exception:
            logging.exception(
                "Exception raised during update_awacs")
            email_subject = "warrant_recovery failed on update_mock()"
            raise

    # Send error email if something's broken
    except Exception as e:
        email_body = str(e) + '\n' + f"See log file for details: {log_name}"
        # utils.send_email(EMAIL_NOTIFICATIONS_ERROR_RECIPIENT, email_subject, email_body)
        logging.critical("payments_recovery aborted with errors.")
        exit(1)

    # Compose success email
    email_subject = "payments_recovery completed successfully"
    email_body = \
        f"""warrant_recovery completed successfully.
            
            Date of Report Run: {datetime.now().strftime("%m/%d/%Y")}
    """
    # utils.send_email(EMAIL_NOTIFICATIONS_SUCCESS_RECIPIENT, email_subject, email_body)
    # logging.info(email_body)


if __name__ == '__main__':
    main()
