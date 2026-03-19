def load_stats():
    """
    Load statistics using SQL queries, handling None values gracefully.
    """
    try:
        # Example query using COALESCE to handle None values
        query = "SELECT COALESCE(SUM(column_name), 0) as total FROM table_name"
        result = execute_query(query)
        total = result['total']
        if total is None:
            total = 0
        print(f"Total: {total}")
    except Exception as e:
        print(f"An error occurred: {e}")
