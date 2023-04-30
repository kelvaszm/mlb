#sql_connect.py
import sqlalchemy
import keyring

class Sql_connect:
    """
    sql_connect class will create an sql alchemy object to handle statements.
    """
    def __init__(self, database_config):
        
        user = database_config['user']
        host = database_config['host']
        port = database_config['port']
        schema = database_config['schema']

        conn_string = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'\
                        .format(user,
                                keyring.get_password(user, schema),
                                host,
                                port,
                                schema)

        #create sql_alchemy engine
        self.engine = self.get_engine(conn_string)


    def get_engine(self, conn_string):
        """
        Create sqlaclchemy engine with connection string
        """
        return sqlalchemy.create_engine(conn_string, echo=False)


    def get_column_datatypes(self, table_name):
        """
        Get column names and datatypes for a table.
        """
        md = sqlalchemy.MetaData()

        table = sqlalchemy.Table(table_name, md, autoload_with=self.engine)

        return [(col.name, col.type) for col in table.c]


    def load(self, df, table_name):
        """
        Load pandas dataframe into database
        """
        return df.to_sql(name = table_name, con=self.engine, if_exists = 'append', index = False)

