from airflow import DAG
from airflow.operators.python import PythonOperator, ShortCircuitOperator
from datetime import datetime

from scripts.logger_creator import CreateLogger
from scripts.sql_handler import SQL_Handler

logger = CreateLogger('LOAD-DATA-DAG', handlers=1)
logger = logger.get_default_logger()

# DECLARING Airflow DAG CONFIGURATION
DAG_CONFIG = {
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email': ['sisaybethelhem@gmail.com'],
    'email_on_failure': True,
    'schedule_interval': '@daily',
}

# Declaring DAG used functions
# Kafka Data Reader


def _check_mysql_connection():
    try:
        sql = SQL_Handler(host='localhost', port=3306,
                          username='root', password='')

        logger.info(
            'SUCCESSFULLY CONNECTED TO THE DATABASE')
        return True

    except Exception as e:
        logger.exception(
            'DATABASE CONNECTION FAILED, DAG EXITING')
        return False


def _create_database():
    try:
        sql = SQL_Handler(host='localhost', port=3306,
                          username='root', password='')

        sql.sql_query("CREATE DATABASE IF NOT EXISTS traffic_data")

        logger.info(
            'DAG CREATED "traffic_data" DATABASE SUCCESSFULLY')
        return True

    except Exception as e:
        logger.exception('DAG FAILED TO CREATE DATABASE "traffic_data"')
        return False

def _create_stations_table():
    try:
        sql = SQL_Handler(host='localhost', port=3306,
                          username='root', password='')

        create_stations_table_query = """
            CREATE TABLE IF NOT EXISTS stations(
                id INT PRIMARY KEY,
                FWY INT,
                direction VARCHAR(2),
                district INT,
                county INT,
                city INT,
                state_pm VARCHAR(10),
                abs_pm FLOAT,
                latitude FLOAT,
                longitude FLOAT,
                length FLOAT,
                type VARCHAR(3),
                lanes INT,
                name VARCHAR(50),
                user_id_1 VARCHAR(6),
                user_id_2 VARCHAR(20),
                user_id_3 INT,
                user_id_4 INT
            )
        """

        sql.insert_table(
            table_create_query=create_stations_table_query, database='traffic_data')

        insert_stations_query = """
            INSERT INTO stations
            (id,FWY,direction,district,county,city,state_pm,abs_pm,latitude,
            longitude,length,type,lanes,name,user_id_1,user_id_2,user_id_3,user_id_4)
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)
        """

        sql.insert_values(database='traffic_data',
                          insert_query=insert_stations_query, file_path='../data/I80_stations.csv')

        logger.info('SUCCESSFULLY CREATED "stations" TABLE')

        return True

    except Exception as e:
        logger.exception('FAILED TO CREATE "stations" TABLE')
        return False


# DAG
with DAG('RAW-DATA-EXTRACTOR-AND-LOADER', catchup=False, default_args=DAG_CONFIG) as dag:

    checking_db_connection = ShortCircuitOperator(
        task_id='checking_db_connection',
        python_callable=_check_mysql_connection
    )

    creating_db = ShortCircuitOperator(
        task_id='creating_db',
        python_callable=_create_database
    )

    creating_stations_table = ShortCircuitOperator(
        task_id='creating_stations_table',
        python_callable=_create_stations_table
    )


    checking_db_connection >> creating_db>> creating_stations_table