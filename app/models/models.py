import os
import pymysql
# import json
from dotenv import load_dotenv
import app.models.db_errorhandling as db_errorhandling
error_handler=db_errorhandling.ErrorHandling()

## Tuple to list conversion 
def touple_list_to_list(touple_list):
    """ This will convert set of Touples 
        into List format
    """
    row_output = []
    for imtems in touple_list: 
        for element in imtems:
            row_output.append(element)
    return row_output
    # print(result)

## Tuple to dict conversion 


class DBConnect:
    """ Data Links to handle Entire 
        DB operations 
    """
    db_user = None
    db_pass = None
    db_name = None
    db_session= None
     
    
    # print()
    @classmethod
    def touple_list_to_dict(cls,touples):
        cls.result = {}
        for index, item in enumerate(touples, start=1):
            cls.result[f'{index}'] = {
                'daemon_name': item[0],
                'daemon_id': item[1],
                'daemon_status': item[2],
                'instance': item[3]
            }
        return cls.result

    @classmethod
    def init_app_db_connect_string(cls):
        load_dotenv()
        cls.db_url = "127.0.0.1"
        cls.db_user = os.getenv("DB_USER")
        cls.db_pass = os.getenv("DB_PASS")
        cls.db_name = os.getenv("DB_NAME")
        # print(cls.db_user,cls.db_pass,cls.db_name) 

    @classmethod
    def connect(cls):
        flag_value=False
        """ Method to get DB connection using pymysql"""
        try:
        # print 'Connect params - {}'.format(args)
            DBConnect.init_app_db_connect_string()
            cls.db_session = pymysql.connect(host=cls.db_url,
                             user=cls.db_user, passwd=cls.db_pass, database=cls.db_name)
            print("Sucessfully connected !!")
            flag_value=True
            cls.cursor = cls.db_session.cursor()
        except pymysql.DatabaseError as db_err:
            print("DB error to connected !! ",db_err)
            cls.error_handler.set_fatal()
            cls.error_handler.exit_program(db_err)
            # If the database connection succeeded create the cursor
            # we-re going to use.
        
        return flag_value

    @classmethod
    def disconnect(cls):
        """ Method to get disconnect from DB connection """
        try:
            cls.cursor.close()
            cls.db_session.close()
        except pymysql.DatabaseError as db_err:
            print ("DB error to connected !! ",db_err)
            cls.error_handler.set_fatal()
            cls.error_handler.exit_program(db_err)

    @classmethod
    def select(cls, sql_query, *args):
        """ Method to run select query with and without arguments """
        try:
        # print "In SELECT :",args
            if not args:
                # if no input argument then perform execute without arg
                cls.cursor.execute(sql_query)
                # time.sleep(10)
                # print("Query Executed !!")
            else:
                if isinstance(args[0], dict):
                    # print 'In SELECT of type dict:',args[0]
                    cls.cursor.execute(sql_query, args[0])

                else:
                    cls.cursor.execute(sql_query, args)
            result = cls.cursor.fetchall()
            # print "After SELECT:",result
            return_row_count = cls.cursor.rowcount
        except pymysql.DatabaseError as db_err:
            # print("Error", db_err)
            result =0
            return_row_count=0
            cls.error_handler.set_fatal()
            cls.error_handler.exit_program(db_err)
            
        return result, return_row_count


    @classmethod
    def insert(cls, sql_query, *args):
        """ Method to run insert query with and without arguments """
        try:
            if not args:
                cls.cursor.execute(sql_query)
            else:
                if isinstance(args[0], dict):
                    cls.cursor.execute(sql_query, args[0])
                else:
                    cls.cursor.execute(sql_query, args)
            cls.db_session.commit()
        except pymysql.DatabaseError as db_err:
            cls.error_handler.set_fatal()
            print("Query Failed : ", sql_query)
            cls.error_handler.exit_program(db_err)

    @classmethod
    def update(cls, sql_query, *args):
        """ Method to run insert query with and without arguments """
        try:
            if not args:
                cls.cursor.execute(sql_query)
            else:
                if isinstance(args[0], dict):
                    cls.cursor.execute(sql_query, args[0])
                else:
                    cls.cursor.execute(sql_query, args)
            cls.db_session.commit()
        except pymysql.DatabaseError as db_err:
            cls.error_handler.set_fatal()
            print("Query Failed : ", sql_query)
            cls.error_handler.exit_program(db_err)

    @classmethod
    def delete(cls, sql_query, *args):
        """ Method to run delete query with and without arguments """
        try:
            if not args:
                cls.cursor.execute(sql_query)
            else:
                if isinstance(args[0], dict):
                    cls.cursor.execute(sql_query, args[0])
                else:
                    cls.cursor.execute(sql_query, args)
            cls.db_session.commit()
        except pymysql.DatabaseError as db_err:
            cls.error_handler.set_fatal()
            print("Query Failed : ", sql_query)
            cls.error_handler.exit_program(db_err)
