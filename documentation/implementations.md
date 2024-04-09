# Overview

This app provides a powerful search functionality that enables developers to retrieve relevant search results by consuming a single API endpoint. By sending a user query to the /filter endpoint, the app returns a JSON array containing the most relevant search matches.

Under the hood, the app leverages a cutting-edge Retrieval-Augmented Generation (RAG) system, which utilizes a ChromaDB vector database to efficiently store and search through large volumes of data. This innovative approach allows for fast and accurate search results, even with complex user queries.

As the first RAG-based search solution within the company, this app offers unique benefits and capabilities not found in other internal tools. It empowers developers to easily integrate advanced search features into their own applications, saving time and resources that would otherwise be spent on building and maintaining a custom search infrastructure.

### Key features of the app include:

Simple API interface: Developers can retrieve search results by sending a POST request to the /filter endpoint with a user query.
Relevant search matches: The app returns a JSON array containing the most relevant search results based on the user's query.
High-performance search: By leveraging a RAG system and ChromaDB vector database, the app delivers fast and accurate search results, even with large datasets.
Easy integration: Developers can quickly incorporate the app's search functionality into their own applications without the need for complex setup or maintenance.

Whether you're building a content discovery platform, a knowledge management system, or any other application that requires powerful search capabilities, this app provides a reliable and efficient solution that can be easily integrated into your development workflow.


## Architecture

The app is built using a modern and efficient stack of technologies, designed to deliver high-performance search capabilities. The main components and their roles are as follows:

1. **Python 3.12**: The app is developed using Python 3.12, leveraging its powerful features and extensive ecosystem of libraries.
2. **ChromaDB**: ChromaDB is used as an in-memory vector database to store and efficiently search through the text embeddings. It provides fast similarity search capabilities, enabling the app to retrieve relevant search results quickly. 
3. **FastAPI**: FastAPI is employed as the web framework for building the API endpoints. It offers high performance, automatic API documentation, and easy integration with other components. 
4. **SlowAPI**: SlowAPI is used in conjunction with FastAPI to apply rate limiting and traffic control to the API endpoints, ensuring the app remains responsive and stable under heavy load.
5. **Uvicorn**: Uvicorn serves as the WSGI web server, providing a fast and efficient runtime environment for the FastAPI application.
6. **Sentence Transformers**: The Sentence Transformers library is utilized to generate text embeddings from the source documents. Specifically, the app uses the `all-MiniLM-L6-v2` model, which is configured to run on CPU for efficient processing. 
7. **Pandas**: Pandas is used for handling and processing the source data files, such as reading the `en-import.csv` file and preparing the data for indexing.
8. **JSON**: The `json` module is employed to load and parse the user configuration file (`cfg.json`), allowing for flexible app settings.
9. **Logging**: The `logging` module is used to capture and store important events and messages within the app, aiding in debugging and monitoring.

The app follows a typical flow for processing user queries and returning search results:

1. The source data is read from the `en-import.csv` file using Pandas and processed into a suitable format.
2. The text data is passed through the Sentence Transformers model to generate vector embeddings.
3. The vector embeddings, along with their metadata, are stored in the ChromaDB vector database for efficient similarity search. 
4. When a user sends a query to the `/filter` endpoint, the query text is transformed into a vector embedding using the same Sentence Transformers model.
5. The query embedding is used to perform a similarity search against the stored embeddings in ChromaDB, retrieving the most relevant documents.
6. The search results are returned to the user as a JSON array, containing the relevant document information.

The modular architecture of the app allows for easy maintenance, scaling, and future enhancements. The use of ChromaDB as a vector database enables efficient storage and retrieval of embeddings, while FastAPI and Uvicorn provide a robust and high-performance web framework for handling API requests.

# API Reference

This section provides detailed information about the available API endpoints in the app, their request and response formats, and any usage restrictions.


## Endpoints

### 1. Health Check

- **Endpoint:** `/`
- **Method:** GET
- **Description:** This endpoint is used to check the health status of the service. It returns a response indicating whether the service is running and available.
- **Request Format:** No request body or parameters required.
- **Response Format:** A simple text response indicating the health status of the service.
- **Authentication/Authorization:** None required.

### 2. Search Filter

- **Endpoint:** `/filter`
- **Method:** POST
- **Description:** This endpoint is used to retrieve search results based on a user's query. It takes a JSON payload containing the user's question and returns a list of relevant search results.
- **Request Format:**
  - Content-Type: `application/json`
  - Request Body:
    ```json
    {
      "query": "What is your user question?"
    }
    ```
- **Response Format:**
  - Content-Type: `application/json`
  - Response Body:
    ```json
    {
      "results": [
        {
          "title": "Title of the FAQ match",
          "body": "Answer to your query question",
          "id": "1234",
          "score": 0.85
        },
        ...
      ]
    }
    ```
  - The `results` array contains one or more search result objects, each with the following fields:
    - `title`: The title of the FAQ match.
    - `body`: The answer to the user's query question.
    - `id`: A unique identifier for the search result.
    - `score`: A relevance score between 0 and 1, indicating how closely the result matches the user's query.
- **Authentication/Authorization:** None required.

## Error Codes

The API uses standard HTTP status codes to indicate the success or failure of a request. The following status codes are commonly used:

- `200 OK`: The request was successful, and the response contains the expected data.
- `400 Bad Request`: The request was malformed or invalid. This may occur if the required JSON payload is missing or incorrectly formatted.
- `500 Internal Server Error`: An unexpected error occurred on the server side while processing the request.

## Rate Limiting

Currently, there are no specific rate limits or usage restrictions enforced by the API. However, it is recommended to use the API responsibly and avoid excessive or abusive requests that may impact the performance and availability of the service.


# Getting Started

This section provides a quick guide on how to set up and start using the app.

#### Prerequisites

To run the app, you need the following:
- Python 3.12
- PIP package manager
- A virtual environment (venv)
- Linux or macOS operating system

#### Installation

To install the app, follow these steps:
1. Run the `setup.sh` script to set up the necessary environment and dependencies.

Or do it manually:
1. Set up a new virtual environment: `python3 -m venv venv`
2. Activate new environment `source ./venv/bin/activate`
3. Execute `pip install -r requirements.txt` to install the required dependencies.

#### Configuration

The app's configuration can be adjusted in the `src/cfg.json` file. All the necessary settings are available in this file.

#### Running the App

To start the app, you have two options:

1. **Application Mode**: Run the following command to start the app in application mode:
   ```bash
   venv/bin/python3 -m ./src/main.py
   ```

2. **Server Mode**: To run the app in server mode, execute the `runserver.sh` script:
   ```bash
   bash ./runserver.sh
   ```

#### Testing

The app uses unit tests for testing and coverage for code coverage.

1. **Running Tests**: To run the unit tests, use the following command:
   ```bash
   coverage run -m unittest discover src/tests
   ```

2. **Coverage Report**: To generate a coverage report, run:
   ```bash
   coverage report --show-missing
   ```

#### Next Steps

After setting up and running the app, you can explore various possibilities for further development and customization. Some ideas for next steps include:

- Integrating the app with other systems or APIs to extend its functionality.
- Customizing the user interface to provide a more tailored experience for your specific use case.
- Implementing additional features or endpoints to enhance the app's capabilities.
- Optimizing the app's performance by fine-tuning the configuration or leveraging caching mechanisms.
- Contributing to the project by fixing bugs, improving documentation, or adding new features.

Feel free to explore the codebase, experiment with different configurations, and adapt the app to suit your needs. The modular architecture and extensive documentation make it easy to understand and build upon the existing functionality.


#### Troubleshooting

Macbook M1/2/3 Chips 

grpcio does not have good compatibility with the M chips yet.
to make this work you need to export these environment variables and install grpcio manually before
the pip install in your virtual environment.

```bash
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1

export CFLAGS="-I /opt/homebrew/opt/openssl/include"
export LDFLAGS="-L /opt/homebrew/opt/openssl/lib"

pip install --ignore-installed --no-binary grpcio grpcio
```


#### Contact
For further questions and assistance please contact:
Danny de Zeeuw - 4451477 [danny.zeeuw.osv@fedex.com]