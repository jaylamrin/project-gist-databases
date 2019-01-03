from .models import Gist

def search_gists(db_connection, **kwargs):
    sql = list()
    sql.append('SELECT * FROM gists')
    if kwargs:
        sql.append(' WHERE ')
        if 'github_id' in kwargs.keys():
            sql.append(''.join("github_id = '%s'" % v for k, v in kwargs.items() if k == 'github_id'))
            if len(kwargs.keys()) > 1:
                sql.append(' AND ')
        if 'created_at' in kwargs.keys():
            sql.append(''.join("datetime(created_at) = '%s'" % v for k, v in kwargs.items() if k == 'created_at'))
            if len(kwargs.keys()) > 1:
                sql.append(' AND ')
        if 'created_at__gte' in kwargs.keys():
            sql.append(''.join("datetime(created_at) >= '%s'" % v for k, v in kwargs.items() if k == 'created_at__gte'))
            if len(kwargs.keys()) > 1:
                sql.append(' AND ')
        if 'created_at__lt' in kwargs.keys():
            sql.append(''.join("datetime(created_at) < '%s'" % v for k, v in kwargs.items() if k == 'created_at__lt'))
            if len(kwargs.keys()) > 1:
                sql.append(' AND ')
        if 'created_at__lte' in kwargs.keys():
            sql.append(''.join("datetime(created_at) <= '%s'" % v for k, v in kwargs.items() if k == 'created_at__lte'))
            if len(kwargs.keys()) > 1 and 'updated_at__gte' in kwargs.keys():
                sql.append(' AND ')
        if 'updated_at__gte' in kwargs.keys():
            sql.append(''.join("datetime(updated_at) >= '%s'" % v for k, v in kwargs.items() if k == 'updated_at__gte'))
    sql.append(';')
    query = ''.join(sql)
    c = db_connection.cursor()
    c.execute(query)
    result = [Gist(row) for row in c.fetchall()]
    return result

