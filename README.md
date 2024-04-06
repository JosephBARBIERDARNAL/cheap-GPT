# cheap-GPT: for broke people

## About

### Description

Current OpenAI pricing for [chat.openai.com](https://chat.openai.com) is around 22$ per month.

This project's aim is to create a simple yet similar interface that uses GPT models using **OpenAI API** instead of the [chat.openai.com](https://chat.openai.com) interface.

### Is it worth it?

Depending on your usage, it might be worth it to pay for the OpenAI API (pay for each request) instead of the monthly subscription.

To estimate whether it is worth for you, you can use the following info:

- if you only use the GPT-3.5 model, it's useless since it's currently free on [chat.openai.com](https://chat.openai.com)

- if you use the GPT-4 (not 32k) model, and by assuming that each input is 500 tokens long (input price = 0.015$) and each output is 1000 (output price = 0.06$) tokens long, we find how many requests you need to make to reach the 22$ monthly subscription price:

```python
monthly_price = 22
input_price = 0.015
output_price = 0.06

requests = monthly_price / (input_price + output_price)
print(requests)
```

Output: `293.33333333333337`

This means that if you make more than 293 requests per month, it is worth it to pay for the subscription.

- if you use the GPT-4 32k model, and by assuming that each input is 500 tokens long (input price = 0.03$) and each output is 1000 (output price = 0.12$) tokens long, we find how many requests you need to make to reach the 22$ monthly subscription price:

```python
monthly_price = 22
input_price = 0.03
output_price = 0.12

requests = monthly_price / (input_price + output_price)
print(requests)
```

Output: `146.66666666666669`

This means that if you make more than 146 requests per month, it is worth it to pay for the subscription.

<br>

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