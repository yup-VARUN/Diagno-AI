import requests
import time
import random
import redis
import redis.commands.search.field

BASE_URL = "http://localhost:5001"

# Add this at the top level of test.py
def clear_redis():
    try:
        # Clear Redis
        redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
        redis_client.flushall()
        
        # Recreate the index
        schema = (
            redis.commands.search.field.TagField("key"),
            redis.commands.search.field.VectorField(
                "vector",
                "HNSW",
                {
                    "TYPE": "FLOAT32",
                    "DIM": 128,
                    "DISTANCE_METRIC": "COSINE",
                },
            ),
        )
        try:
            redis_client.ft("vector_index").dropindex()
        except:
            pass
        redis_client.ft("vector_index").create_index(schema)
        
        time.sleep(1)  # Give Redis time to settle
    except Exception as e:
        print(f"Failed to clear Redis: {e}")
        sys.exit(1)

# Function to generate a 128-dimensional random vector
def generate_random_vector(dimensions=128):
    return [random.random() for _ in range(dimensions)]

# Store test vectors
def store_vector(vector_key, vector_data):
    payload = {"key": vector_key, "vector": vector_data}
    response = requests.post(f"{BASE_URL}/api/store_vector", json=payload)
    print(f"Store Vector Response for {vector_key}: Status Code: {response.status_code}, Response: {response.json()}")
    return response

# Search test vectors
def search_vector(query_vector, top_k=5):
    payload = {"vector": query_vector, "top_k": top_k}
    response = requests.post(f"{BASE_URL}/api/search_vector", json=payload)
    print(f"Search Vector Response: Status Code: {response.status_code}, Response: {response.json()}")
    return response.json()

# Test Case 1: Store multiple vectors with 128 dimensions
def test_multiple_vector_storage():
    vectors = [
        ("test_vector_1", generate_random_vector()),
        ("test_vector_2", generate_random_vector()),
        ("test_vector_3", generate_random_vector()),
    ]
    
    for key, vector in vectors:
        store_vector(key, vector)
    time.sleep(2)  # Give Redis time to settle

# Test Case 2: Retrieve stored vectors (Basic Search)
def test_basic_vector_search():
    query_vector = generate_random_vector()  # Query similar to one of the stored vectors
    response = search_vector(query_vector)
    
    if "results" in response:
        assert len(response["results"]) > 0, "No results returned"
        print(f"Results: {response['results']}")
    else:
        print("Error: No results returned.")
    
# Test Case 3: Search with no matching vector (Edge Case)
def test_no_matching_vector():
    query_vector = generate_random_vector()  # Vector that shouldn't match any stored vectors
    response = search_vector(query_vector)
    
    if "results" in response:
        # Here, we assume a score of 0.3 or higher might indicate a significant match, so we'll consider a match threshold.
        assert len(response["results"]) == 0 or float(response["results"][0]["score"]) < 0.3, "Results shouldn't be similar or should be empty"
        print(f"Results for no matching vector: {response['results']}")
    else:
        print("Error: No results returned.")


# Test Case 4: Search with high value of top_k (Retrieve multiple results)
def test_search_top_k():
    query_vector = generate_random_vector()  # Query similar to one of the stored vectors
    top_k = 3  # Try to fetch the top 3 closest vectors
    response = search_vector(query_vector, top_k)
    
    assert "results" in response, "No results returned"
    assert len(response["results"]) <= top_k, f"Returned more than {top_k} results"
    print(f"Top-K Retrieval Response: {response}")

# Clear The Database before every tests
def clear_database():
    response = requests.post(f"{BASE_URL}/api/clear")
    print(f"Clear Database Response: Status Code: {response.status_code}, Response: {response.json()}")
    return response

# Test Case 5: Edge Case - Empty Database
def test_empty_database():
    print("Running test with an empty database...")
    clear_redis()  # Clear the database first
    query_vector = generate_random_vector()
    response = search_vector(query_vector)
    assert "results" in response, "No results returned"
    assert len(response["results"]) == 0, "Database shouldn't have results"
    print("Empty database test passed!")

# Main testing routine
if __name__ == "__main__":
    print("Starting serious retrieval tests...\n")
    
    # Clear database at the start
    clear_redis()

    # Run the tests
    test_multiple_vector_storage()
    test_basic_vector_search()
    test_no_matching_vector()
    test_search_top_k()
    test_empty_database()

    print("\nAll tests completed!")