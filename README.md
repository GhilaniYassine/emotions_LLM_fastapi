# README.md

# Emotion Analysis API

This is a FastAPI application that analyzes text input for emotional content and returns a dictionary of detected emotions. The application utilizes a generative AI model to process the input and identify various emotions based on predefined categories.

## Features

- Accepts text input via a RESTful API.
- Analyzes the text for a range of emotions including negative, positive, and neutral emotions.
- Returns a structured dictionary indicating the presence of each emotion.

## Project Structure

```
emotion-analysis-api
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── config
│   │   └── settings.py        # Configuration settings for the application
│   ├── models
│   │   └── emotions.py        # Data model for the emotions dictionary
│   ├── services
│   │   └── emotion_analyzer.py # Logic for analyzing text input for emotions
│   ├── routes
│   │   └── api.py             # API endpoints definition
│   └── utils
│       └── helpers.py         # Utility functions for text processing
├── tests
│   ├── __init__.py            # Marks the tests directory as a package
│   └── test_api.py            # Unit tests for the API endpoints
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables
├── .gitignore                  # Files and directories to ignore by Git
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd emotion-analysis-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables in the `.env` file as needed.

## Usage

To run the application, execute the following command:
```
uvicorn src.main:app --reload
```

You can then access the API at `http://127.0.0.1:8000`.

## API Endpoints

- **POST /analyze**: Accepts a JSON payload with the text to analyze and returns a dictionary of detected emotions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.