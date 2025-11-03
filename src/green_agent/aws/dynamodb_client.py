import concurrent
from datetime import datetime

import boto3


class DynamoDBClient:
    """
    This class is a client for the DynamoDB database. It manages three tables:
    - registration: stores the registration information of white agents
    - in_progress: stores in-progress tasks of white agents
    - results: stores the results of white agents on individual tasks
    """

    def __init__(self, region="us-west-2", reset=False):
        if reset:
            self.client = boto3.client("dynamodb", region_name=region)
            self._setup()

        self.dynamodb = boto3.resource("dynamodb")
        self.registration_table = self.dynamodb.Table("registration")
        self.progress_table = self.dynamodb.Table("in_progress")
        self.results_table = self.dynamodb.Table("results")

    def get_registration(self, id):
        response = self.registration_table.get_item(Key={"id": id})
        return response.get("Item", None)

    def get_progress(self, id):
        response = self.progress_table.get_item(Key={"id": id})
        return response.get("Item", None)

    def get_result(self, id, task_id):
        response = self.results_table.get_item(Key={"id": id, "task_id": task_id})
        return response.get("Item", None)

    def insert_registration(self, id, name):
        self.registration_table.put_item(
            Item={
                "id": id,
                "name": name
            }
        )

    def insert_progress(self, id, task_id, start_time=None):
        self.progress_table.put_item(
            Item={
                "id": id,
                "task_id": task_id,
                "start_time": start_time or datetime.now().isoformat(),
            }
        )

    def insert_result(self, id, task_id, result):
        self.results_table.put_item(
            Item={
                # schema can be simplified
                "id": id,
                "task_id": task_id,
                "accuracy": result.get("accuracy"),
                "passed": result.get("passed"),
                "total": result.get("total"),
                "time_complexity": result.get("time_complexity"),
                "space_complexity": result.get("space_complexity"),
                "readability_overall": result.get("readability_overall"),
                "readability_naming": result.get("readability_naming"),
                "readability_structure": result.get("structure"),
                "readability_simplicity": result.get("simplicity"),
                "readability_idiomatic": result.get("idiomatic"),
                "readability_comment": result.get("comment"),
            }
        )

    def _setup(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [
                executor.submit(self._recreate_table, "registration", False),
                executor.submit(self._recreate_table, "in_progress", False),
                executor.submit(self._recreate_table, "results", True),
            ]
            for f in concurrent.futures.as_completed(futures):
                f.result()

    def _recreate_table(self, table_name, range_key=False):
        waiter_config = {'Delay': 3, 'MaxAttempts': 20}

        print(f"Recreating {table_name} table...")
        try:
            self.client.delete_table(TableName=table_name)
        except self.client.exceptions.ResourceNotFoundException:
            pass

        waiter = self.client.get_waiter('table_not_exists')
        waiter.wait(TableName=table_name, WaiterConfig=waiter_config)

        if range_key:
            key_schema = [{"AttributeName": "id", "KeyType": "HASH"},
                          {"AttributeName": "task_id", "KeyType": "RANGE"}]
            attribute_definitions = [{"AttributeName": "id", "AttributeType": "S"},
                                     {"AttributeName": "task_id", "AttributeType": "S"}]
        else:
            key_schema = [{"AttributeName": "id", "KeyType": "HASH"}]
            attribute_definitions = [{"AttributeName": "id", "AttributeType": "S"}]

        self.client.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            BillingMode="PAY_PER_REQUEST"
        )

        waiter = self.client.get_waiter('table_exists')
        waiter.wait(TableName=table_name, WaiterConfig=waiter_config)
        print(f"Done creating {table_name} table")
