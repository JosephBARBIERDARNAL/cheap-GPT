# cheap-GPT

## Project Description

Current OpenAI pricing for [chat.openai.com](https://chat.openai.com) is around 22$ per month.

This project's aim is to create a simple yet similar interface that uses GPT models using OpenAI API instead of the chat.openai.com interface.

## Set up

- Clone the repository

```bash
git clone https://github.com/JosephBARBIERDARNAL/cheap-GPT.git
cd cheap-GPT
```

<br>

- Install the dependencies within a virtual environment

```bash
python3.10 -m venv venv
source venv/bin/activate
```

Open a new window and then run:

```bash
pip install -r requirements.txt
```

<br>

- Create a `secrets.toml` in the `.streamlit` directory

```
touch .streamlit/secrets.toml
```

<br>

- Add your OpenAI API key to the `secrets.toml` file. It should look like this:

```toml
OPENAI_API_KEY="sk-restOfYourKey"
```


<br>

And that's it! You can now run the app to open the interface with:

```bash
streamlit run main.py
```

The app should open in your default browser.

<br>

## Features

This project is functional but will be improve through time (**contributions are welcome**). Here are the current features:

- Send a message to the GPT model (GPT-3.5 and GPT-4)

- Create images with the DALL-E model (DALL-E-2 and DALL-E-3)