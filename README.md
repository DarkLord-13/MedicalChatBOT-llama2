I ran it on i5 8th gen with 8GB RAM, 16GB is preferred, if you have GPU, kindly download the GPU version from the given link, and change the llm parameter in the load function accordingly, refer the documentation for it.

Credit to AI Anytime, i have referred it from his youtube video.

1. Create a directory MEDICALCHATBOT (all the files and folders must be in it) or just clone this repo

   first create a virtual environment (venv)
   pip install -r requirements.txt
   python -m venv venv
   venv\Scripts\activate

   Now download the quantized model (save it in the same directory, say MEDICALCHATBOT)
   link -> https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin

   Save the pdf file in directory named data (if you change the name, make the necessary changes accordingly)

   run ingest.py

   run model.py
