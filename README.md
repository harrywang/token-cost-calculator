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

## Huggingface Space Setup

1. Create a space at https://huggingface.co/spaces/new

2. Add the remote and push your code:

```bash
git remote add space https://huggingface.co/spaces/harrywang/token-cost-calculator
git push --force space main
```

3. Add a `space.yml` configuration file to provide metadata for your Hugging Face Space:

```yaml
title: Token Cost Calculator
emoji: 💰
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.24.0
app_file: app.py
pinned: false
license: mit
```

This configuration file addresses the warning about missing YAML metadata in the repo card. For more information, see: https://huggingface.co/docs/hub/spaces-config-reference

