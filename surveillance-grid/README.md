# Surveillance Grid Project

## Overview
The Surveillance Grid project is designed to scrape data from specified websites using Selenium, process the collected data, and utilize a language model (LLM) to answer queries through a web-based frontend built with Flask. This project aims to provide a comprehensive solution for data collection, processing, and interaction.

## Project Structure
```
surveillance-grid
├── src
│   ├── scraper
│   │   ├── selenium_runner.py
│   │   ├── parsers.py
│   │   └── __init__.py
│   ├── data
│   │   ├── collect.py
│   │   └── storage.py
│   ├── llm
│   │   ├── trainer.py
│   │   ├── model.py
│   │   └── embeddings.py
│   ├── api
│   │   ├── app.py
│   │   └── routes.py
│   ├── frontend
│   │   ├── templates
│   │   │   └── index.html
│   │   └── static
│   │       ├── css
│   │       │   └── styles.css
│   │       └── js
│   │           └── main.js
│   └── utils
│       └── helpers.py
├── tests
│   ├── test_scraper.py
│   ├── test_llm.py
│   └── test_api.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd surveillance-grid
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Running the Scraper**: 
   Execute the Selenium scraper to collect data:
   ```
   python src/scraper/selenium_runner.py
   ```

2. **Processing Data**: 
   Use the data collection and storage scripts to process and save the scraped data:
   ```
   python src/data/collect.py
   python src/data/storage.py
   ```

3. **Training the Language Model**: 
   Train the LLM using the collected data:
   ```
   python src/llm/trainer.py
   ```

4. **Starting the API**: 
   Launch the Flask API to handle queries:
   ```
   python src/api/app.py
   ```

5. **Accessing the Frontend**: 
   Open your web browser and navigate to `http://localhost:5000` to interact with the application.

## Testing
Run the tests to ensure everything is functioning correctly:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.