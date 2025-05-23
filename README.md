# 🏞️ OBSS Internship Competition 2025 – Image Captioning Challenge
![header](https://github.com/user-attachments/assets/bced83bf-abcf-406f-9e06-9989f876c82f)

## 📌 Competition Overview

The **OBSS Internship Competition 2025** is a machine learning challenge focused on **image captioning**. The goal is to generate semantically meaningful and contextually accurate textual descriptions for input images.

This repository contains my work throughout the competition, including models, training experiments, submission files, and result visualizations.



## 🧠 Models & Approach

This project leverages state-of-the-art **vision-language models**, fine-tuned on the competition dataset to generate high-quality image captions:

- 🔹 **BLIP** – Bootstrapped Language-Image Pretraining
- 🔹 **BLIP-2** – Enhanced with Flan-T5-XL for multimodal reasoning
- 🔹 **GIT** – Generative Image-to-Text Transformer


## 🖼️ Dataset & Sample Outputs 
The dataset contains 21,367 images. Below are a few example of training set images:
![download](https://github.com/user-attachments/assets/189561a6-3403-4290-b047-d5c52aa5b5e2)
![download](https://github.com/user-attachments/assets/b48a7d0d-d4fa-44d9-8a5a-fd03e8bfdccc)


## 🔬 Evaluation & Metrics
Caption quality is primarily evaluated using the Fréchet GTE Distance (FGD) metric, a semantic similarity score based on sentence embeddings.

🔸 Embedding Model: gte-small

🔸 Additional metrics such as BLEU, CIDEr may be added for comparison

Evaluation scripts can be included if needed.

🚀 How to Use
🔗 Run Experiments via Colab
Each model has a dedicated Colab notebook
