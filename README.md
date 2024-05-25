
# Q&A Travel Chatbot with Gemini-Pro AI

This Streamlit application utilizes Google's generative AI, specifically the Gemini-Pro model, to provide personalized travel and activity suggestions based on user inputs. The application is designed to interact with users, asking for their travel preferences and budget, then generating tailored suggestions that enhance their travel planning experience.

## Project Setup

### Prerequisites

- Python 3.8+
- Pip
- An API key from Google Cloud with access to the Gemini-Pro model

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://yourrepository.git
   cd yourrepository
   ```

2. **Set up a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```

4. **Environment Variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your Google API key to the `.env` file:
     ```plaintext
     GOOGLE_API_KEY='your_google_api_key_here'
     ```

### Running the Application

Execute the following command to run the app:
```bash
streamlit run app.py
```

## Functionalities

- **Interactive Queries:** Users can specify their travel destination, activities they are interested in, and their budget for the trip.

- **Dynamic AI-Generated Suggestions:** Based on the user's inputs, the Gemini-Pro AI dynamically generates suggestions for activities and travel plans within the specified budget.

## Usage Instructions

1. **Open the App:**
   - Navigate to the application URL, typically `http://localhost:8501` after starting the app.

2. **Input Travel Preferences:**
   - Enter your desired travel destination.
   - Specify the types of activities you plan to engage in at the destination.
   - Choose your budget from a dropdown menu.

3. **Get Suggestions:**
   - Click the 'Submit' button to receive personalized travel and activity suggestions based on your inputs.

## Troubleshooting

- **API Key Issues:** Ensure that your API key is correctly entered in the `.env` file and that it has not expired or been restricted.

- **Connectivity Issues:** Check your internet connection if the app fails to communicate with the Gemini-Pro API.

---

For more information, visit [Streamlit Documentation](https://docs.streamlit.io) or [Google's API Documentation](https://cloud.google.com/apis/docs/overview).
