# About

A Gradio App for Calculating OpenAI API Tokens and Costs. 

Use the app on Huggingface: https://huggingface.co/spaces/harrywang/token-cost-calculator

Local setup:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then run `python app.py` or `gradio app.py` (for debugging auto reloading) to try the app at http://127.0.0.1:7860/

NOTE: To create a public link, set `share=True` in `launch()`.

