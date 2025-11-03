from dynamodb_client import DynamoDBClient

if __name__ == "__main__":
    client = DynamoDBClient()

    id = "1234567890"
    client.insert_registration(id, "John Doe")
    print(client.get_registration(id))

    client.insert_progress(id, "task_1")
    print(client.get_progress(id))

    client.insert_result(
        id,
        "task_1",
        {
            "accuracy": 100,
            "passed": 10,
            "total": 10,
            "time_complexity": "O(n)",
            "space_complexity": "O(n)",
            "readability_overall": 15,
            "readability_naming": 5,
            "readability_structure": 5,
            "readability_simplicity": 5,
            "readability_idiomatic": 5,
            "readability_comment": 5,
        },
    )
    print(client.get_result(id, "task_1"))
