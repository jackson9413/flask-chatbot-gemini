# Flask Chatbot with Google Gemini

This project is a chatbot application built using Flask and Google Gemini. The chatbot allows users to interact with an AI model to get responses to their queries.

## Project Structure

The project structure is as follows:

```bash
flask-chatbot-gemini/
├── .env
├── app.py
├── LICENSE
├── README.md
├── static/
│   └── style.css
└── templates/
    └── index.html
```


## Prerequisites

- Python 3.x
- Flask
- Google Gemini API Key

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-chatbot-gemini.git
    cd flask-chatbot-gemini
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your [`.env`] file with your Google Gemini API key:
    ```env
    GOOGLE_API_KEY=YOUR_OWN_GOOGLE_API_KEY
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to [`http://127.0.0.1:5000/`].

3. Type your message in the input box and click the send button to interact with the chatbot.

## Project Files

- [`app.py`]: Main Flask application file.
- [`static/style.css`]: CSS file for styling the chatbot interface.
- [`templates/index.html`]: HTML template for the chatbot interface.
- [`.env`]: Environment file containing the Google Gemini API key.
- [`LICENSE`]: MIT License for the project.
- [`README.md`]: Project documentation.

## License

This project is licensed under the MIT License. See the [`LICENSE`] file for details.

