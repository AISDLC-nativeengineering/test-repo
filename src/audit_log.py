import psycopg2

# Connect to PostgreSQL
def connect_database():
    connection = psycopg2.connect(
        database="audit_logs",
        user="admin",
        password="securepassword",
        host="localhost",
        port="5432"
    )
    return connection

# Log Permission Enforcement
def enforce_permissions(user_role):
    if user_role not in ["admin", "compliance_officer"]:
        raise PermissionError("Access Denied")

# Search Audit Logs
def search_logs(connection, user=None, action_type=None, date_range=None):
    cursor = connection.cursor()

    # Base query
    query = "SELECT * FROM audit_log WHERE TRUE"

    # Apply filters
    if user:
        query += f" AND user_id = '{user}'"
    if action_type:
        query += f" AND action_type = '{action_type}'"
    if date_range:
        query += f" AND timestamp BETWEEN '{date_range[0]}' AND '{date_range[1]}'"

    cursor.execute(query)
    return cursor.fetchall()

# Retention Policy
def apply_retention_policy(connection, retention_days):
    cursor = connection.cursor()
    query = f"DELETE FROM audit_log WHERE timestamp < NOW() - INTERVAL '{retention_days} day'"
    cursor.execute(query)
    connection.commit()

if __name__ == "__main__":
    conn = connect_database()
    enforce_permissions("admin")
    logs = search_logs(conn, user="john_doe", action_type="export", date_range=("2023-01-01", "2023-04-01"))
    for log in logs:
        print(log)
    apply_retention_policy(conn, retention_days=90)