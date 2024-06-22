# FastAPI 서버의 URL
import time
import requests

BASE_URL = "http://localhost:8000"

def measure_api_response_time(url, method="get", data=None, params=None):
    total_time = 0
    number_of_requests = 10  # 측정을 위한 요청 횟수

    for _ in range(number_of_requests):
        start_time = time.time()
        if method == "get":
            response = requests.get(url, params=params)
        elif method == "post":
            response = requests.post(url, json=data)
        elif method == "put":
            response = requests.put(url, json=data)
        elif method == "delete":
            response = requests.delete(url, params=params)
        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / number_of_requests
    print(f"Average response time for {method.upper()} {url}: {average_time:.4f} seconds")
    return average_time

# 각 엔드포인트에 대한 응답 시간 측정
measure_api_response_time(f"{BASE_URL}/")
measure_api_response_time(f"{BASE_URL}/items/1")
measure_api_response_time(f"{BASE_URL}/items/", method="post", data={"name": "Test Item", "description": "A test item", "price": 10.0})
measure_api_response_time(f"{BASE_URL}/items/1", method="put", data={"name": "Updated Item", "description": "An updated item", "price": 15.0})
measure_api_response_time(f"{BASE_URL}/items/1", method="delete")
