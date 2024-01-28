# Stock Exchange Web App

## Overview

The SE Web App is a simple web application that displays real-time stock data in a scrolling ticker format. It uses the Polygon.io API for fetching stock information and is built with HTML, CSS, and Python Flask.

## Installation

1. **Install Dependencies:**
    ```bash
    pip install Flask requests
    ```

2. **Configure API Key:**
    - Replace `'YOUR_POLYGON_API_KEY'` in `app.py` with your actual Polygon.io API key.

3. **Run the Application:**
    ```bash
    python app.py
    ```

4. **View the App:**
    - Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the web application.

## Usage

- Visit the web page to see the scrolling ticker displaying real-time stock data.
- Interact with the ticker items for additional information.

## Configuration

To configure the application, update the API key in `app.py`:

```python
polygon_api_key = 'YOUR_POLYGON_API_KEY'
