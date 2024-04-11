import DatabaseManager as dm

def get_column_names(tablename):
    """UTILITY_FUNC: Return column names of specified table."""
    cmd = f"""
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA='{dm.manager.db_name}' 
        AND TABLE_NAME='{tablename}';
    """
    columnnames = dm.manager.execute_read_query(cmd)
    columnnames = [col[0] for col in columnnames]
    return columnnames

def get_record_default_value(db_name, tablename, column_name):
    """Get the initial default value (if any) for a corresponding table and column."""
    # Returns None (NULL) if no default value was found.
    cmd = f"""
SELECT 
    COLUMN_DEFAULT
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
  TABLE_SCHEMA = '{db_name}' 
  AND TABLE_NAME = '{tablename}'
  AND COLUMN_NAME = '{column_name}';
    """
    res = dm.manager.execute_read_query(cmd)
    res = res[0][0]
    if res == "NULL" or res is None:
        return None
    else:
        return res

class Table:
    def __init__(self, tablename, data, commit=True):
        self.tablename = tablename
        self.data = data

        columns = get_column_names(tablename)
        for d in columns:
            if not d in self.data.keys():
                default = get_record_default_value('chatplatform', tablename, d)
                if default: # None if no default.
                    self.data[d] = default
        if commit:
            pass