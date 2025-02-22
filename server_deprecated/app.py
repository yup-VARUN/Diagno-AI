import redis
import numpy as np
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

class RedisVectorDB:
    def __init__(self, host="localhost", port=6379, index_name="vector_index", dim=128):
        """Initialize Redis connection and RediSearch index."""
        self.redis_client = redis.Redis(host=host, port=port, decode_responses=True)
        self.index_name = index_name
        self.dim = dim
        self._create_index()

    def _create_index(self):
        """Create a vector search index in Redis if it doesn't exist."""
        try:
            self.redis_client.ft(self.index_name).info()  # Check if index exists
        except redis.exceptions.ResponseError:
            # Define RediSearch index
            schema = (
                redis.commands.search.field.TagField("key"),
                redis.commands.search.field.VectorField(
                    "vector",
                    "HNSW",  # Hierarchical Navigable Small World
                    {
                        "TYPE": "FLOAT32",
                        "DIM": self.dim,
                        "DISTANCE_METRIC": "COSINE",  # Options: COSINE, L2, IP
                    },
                ),
            )
            self.redis_client.ft(self.index_name).create_index(schema)
    
    def add_vector(self, key, vector):
        """Add a vector to Redis Stack."""
        if len(vector) != self.dim:
            raise ValueError(f"Vector must have {self.dim} dimensions")

        # Convert to Redis format
        vector_data = np.array(vector, dtype=np.float32).tobytes()

        # Store vector with a unique key
        self.redis_client.hset(f"vec:{key}", mapping={"key": key, "vector": vector_data})
        return True

    def search_vector(self, query_vector, k=3):
        """Search for nearest vectors in Redis."""
        if len(query_vector) != self.dim:
            raise ValueError(f"Query vector must have {self.dim} dimensions")

        # Convert query vector to Redis format
        query_vector_data = np.array(query_vector, dtype=np.float32).tobytes()

        # Perform vector search
        query = (
            redis.commands.search.query.Query("*=>[KNN {} @vector $vec AS score]".format(k))
            .sort_by("score")
            .return_fields("key", "score")
            .paging(0, k)
            .dialect(2)
        )
        
        # Execute search
        results = self.redis_client.ft(self.index_name).search(query, query_params={"vec": query_vector_data})

        return [{"key": doc["key"], "score": doc["score"]} for doc in results.docs]

    def clear_all(self):
        """Clear all vectors from the database."""
        # Get all keys matching the vector pattern
        keys = self.redis_client.keys("vec:*")
        if keys:
            self.redis_client.delete(*keys)
        # Recreate the index
        try:
            self.redis_client.ft(self.index_name).dropindex()
        except:
            pass
        self._create_index()

# Flask App
app = Flask(__name__)
CORS(app)
vector_db = RedisVectorDB(host="localhost", port=6379, index_name="vector_index", dim=128)

@app.route('/', methods = ['GET'])
def default():
    return jsonify({"message": "DIAGNO AI WILL WIN THIS MF HACKATHON!"}), 200

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

@app.route('/api/clear', methods=['POST'])
def clear_database():
    try:
        vector_db.clear_all()
        return jsonify({"message": "Database cleared successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/store_vector', methods=['POST'])
def store_vector():
    data = request.get_json()
    key = data.get("key")
    vector = data.get("vector")

    if not key or not vector:
        return jsonify({"error": "Missing key or vector"}), 400

    try:
        vector_db.add_vector(key, vector)
        return jsonify({"message": "Vector stored successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/search_vector', methods=['POST'])
def search_vector():
    data = request.get_json()
    query_vector = data.get("vector")

    if not query_vector:
        return jsonify({"error": "Missing query vector"}), 400

    try:
        results = vector_db.search_vector(query_vector, k=5)
        return jsonify({"results": results}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
