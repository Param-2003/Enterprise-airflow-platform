# To demonstrate enterprise-level extensibility.
from airflow.models.baseoperator import BaseOperator

class DummyCustomOperator(BaseOperator):
    def __init__(self, custom_param, **kwargs):
        super().__init__(**kwargs)
        self.custom_param = custom_param

    def execute(self, context):
        print(f"👷 Running custom logic with param: {self.custom_param}")
