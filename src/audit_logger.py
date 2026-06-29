import logging
from datetime import datetime

class AuditLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | %(message)s'
        )

    def log_report_generation(self, report_name, user):
        logging.info(f"Report Generated | Report: {report_name} | User: {user}")

    def log_data_export(self, file_type, destination, user):
        logging.info(f"Data Exported | File Type: {file_type} | Destination: {destination} | User: {user}")

    def log_data_access(self, user_id, access_reason):
        logging.info(f"Data Access | User ID: {user_id} | Reason: {access_reason}")

    def query_logs(self):
        with open(self.log_file, 'r') as file:
            return file.readlines()

# Example usage
# audit_logger = AuditLogger(log_file='audit.log')
# audit_logger.log_report_generation(report_name='Monthly Financial Report', user='admin')
# audit_logger.log_data_export(file_type='PDF', destination='email@example.com', user='admin')
# audit_logger.log_data_access(user_id='1234', access_reason='Compliance Review')