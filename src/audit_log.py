import sqlite3
from datetime import datetime

class AuditLog:
    def __init__(self, db_path):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Initialize the audit log database."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                action_type TEXT NOT NULL,
                metadata TEXT
            )
        ''')
        connection.commit()
        connection.close()

    def log_action(self, user_id, action_type, metadata=None):
        """Log an action in the audit log."""
        timestamp = datetime.now().isoformat()
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO audit_log (user_id, timestamp, action_type, metadata)
            VALUES (?, ?, ?, ?)
        ''', (user_id, timestamp, action_type, metadata))
        connection.commit()
        connection.close()

    def retrieve_logs(self, filter_criteria=None):
        """Retrieve logs based on filter criteria."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM audit_log'
        parameters = []

        if filter_criteria:
            filters = []
            if 'user_id' in filter_criteria:
                filters.append('user_id = ?')
                parameters.append(filter_criteria['user_id'])
            if 'action_type' in filter_criteria:
                filters.append('action_type = ?')
                parameters.append(filter_criteria['action_type'])
            if 'date_range' in filter_criteria:
                filters.append('timestamp BETWEEN ? AND ?')
                parameters.extend(filter_criteria['date_range'])

            query += ' WHERE ' + ' AND '.join(filters)

        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        connection.close()
        return rows

# Example usage
# audit_log = AuditLog(db_path='audit_log.db')
# audit_log.log_action(user_id='user123', action_type='Export', metadata='Data exported: sales_data.csv')
# logs = audit_log.retrieve_logs(filter_criteria={'user_id': 'user123', 'action_type': 'Export'})
# print(logs)