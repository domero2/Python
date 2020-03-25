import snowflake.connector
import boto
import boto3
import datetime
from boto.s3.connection import S3Connection
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
access_key = 'get_aws_code'
secret_key = 'get_aws_code'
bucket_name = 'airflow-albi-aws'
conn = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def listFiles(client):
    """List files in specific S3 URL"""
    response = client.list_objects(Bucket=bucket_name)  # , Prefix=_PREFIX)
    for content in response.get('Contents', []):
        yield content.get('Key')

def connectToSnowflake():
    ctx = snowflake.connector.connect(user='amajcher',account='av20879.eu-west-1',password='********')
    cs = ctx.cursor()
    try:

        results=cs.execute("select * from \"DATABCOSTS\".\"LOADFILES\".\"StagingDatabricks\";").fetchall()
        for rec in results:
            print('%s, %s' % (rec[0], rec[1]))
        # cs.execute("""
        #    COPY INTO "test_db"."test_schema"."Test_table"
        #         FROM
        #             '@"test_db"."test_schema"."stage_name"/test.txt'
        #                 FILE_FORMAT = (FIELD_DELIMITER = ',' NULL_IF ='' )
        #                 ON_ERROR = "ABORT_STATEMENT"
        #     ;
        #     """)
    except:
        print("Failed to connect to snowflake")
    finally:
        cs.close()

def getAllFilesAndLastModDates():
    paginator = conn.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket=bucket_name)
    for bucket in page_iterator:
        for file in bucket['Contents']:
            try:
                metadata = conn.head_object(Bucket=bucket_name, Key=file['Key'])
                print(metadata)
                print(metadata.get("LastModified"))
            except:
                print("Failed {}".format(file['Key']))
    for file in listFiles(conn):
        print ('File found: %s' % file)
dag = DAG('WSdag', description='Getting files from S3 and connect to SF',
          schedule_interval="1 * * * *",
          start_date=datetime(2019, 10, 23, 10, 00, 0), catchup=False)

#myOperator = PythonOperator(task_id='WStask', python_callable=getAllFilesAndLastModDates, dag=dag)

getAllFilesAndLastModDates()
connectToSnowflake()
#https://www.astronomer.io/docs/cli-quickstart/
