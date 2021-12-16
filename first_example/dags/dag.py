import numpy as np
from pytrends.request import TrendReq
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def get_random_trend_in_country(country='russia'):
    try:
        pytrend = TrendReq()
        country_trends = pytrend.trending_searches(pn=country)
        country_trends['country'] = country

        df = country_trends.reset_index(drop=False)
        df = df.rename(columns={0: 'search_term', 'index': 'order'})

        # search popularity (top 10)
        rank = np.random.random_integers(0, 10)
        d = df[df.order == rank][['search_term', 'country']].set_index('country').T.to_dict('records')[0]
        return d
    except Exception as e:
        error = str(e)
        print(error)


our_dag = DAG(
    "our_dag",
    description='Python DAG example',
    schedule_interval="*/5 * * * *",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['python'],
    doc_md='*Python DAG doc* :)'
)

get_random_trend_in_russia = PythonOperator(
    task_id='get_random_trend_in_country',
    python_callable=get_random_trend_in_country,
    dag=our_dag
)


get_random_trend_in_russia
