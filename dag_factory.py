from airflow import DAG
from airflow.base import BaseOperator

import inspect


class DagFactory:
    """
    * Construct DAGs from yaml files,
    giving all parameter and logic 
    exceptions instead of stopping at 
    first one.
    """
    @classmethod
    def create_dag(cls, config, errs):
        """

        """
        pass