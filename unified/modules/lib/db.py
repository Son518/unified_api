import mysql.connector
import mysql.connector.pooling
import traceback

from unified.default_settings import logger
# from lib.auth import auth
from lib.util import applet_token as auth

class DB:
    def __init__(self, dbconfig):
        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool", pool_size=5, **dbconfig)
    def _execute_query(self, sql):
        logger.info("Executing ")
        logger.info(sql)
        try:
            cnx1 = self.cnxpool.get_connection()
            cursor = cnx1.cursor(dictionary=True)
            cursor.execute(sql)
            result = cursor.fetchall()
            logger.debug(result)
            cursor.close()
            return result

        except Exception as err:
            logger.info(err)
            traceback.print_exc()
            return None

        finally:
            cursor.close()
            logger.info("Closing")
            cnx1.close()
            
    def get_select_domain_where_condition(self, db, table_name, fields, condition, auth=auth):
        """
        Get values of given fields using SQL SELECT from given schema and table, 
        that meets the given condition and has given domain_id
        """

        fields = fields or '*'
        where_clause = f" AND {condition}" if condition is not None else ''
        domain_id = auth.current_user()['domain_id']
        sql = f"SELECT {fields} FROM {db}.{table_name} WHERE domain_id={domain_id} {where_clause}"
        logger.info(sql)
        results = self._execute_query(sql)

        return results

    def get_select_user_where_condition(self, db, table_name, fields, condition, auth=auth):
        """
        Get values of given fields using SQL SELECT from given schema and table, 
        that meets the given condition and has given user_id
        """

        fields = fields or '*'
        where_clause = f" AND {condition}" if condition is not None else ''
        domain_id = auth.current_user()['domain_id']
        user_id = auth.current_user()['user_id']
        sql = f"""
            SELECT {fields} 
            FROM {db}.{table_name} 
            WHERE domain_id={domain_id} 
            AND created_by={user_id} 
            {where_clause}"""
        logger.info(sql)
        results = self._execute_query(sql)

        return results
