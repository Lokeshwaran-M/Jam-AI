import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def gen_model(d_path,s_path):
    # Open file
    with open(d_path) as file:
        # Read each line and append to array
        data = []
        for line in file:
            data.append(line.strip())
    # Tokenize the questions and answers
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    data = tokenizer(data, padding=True, truncation=True, return_tensors="pt")

    # Train the model
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    optimizer = torch.optim.Adam(model.parameters(), lr=5e-5)

    loop_count=int(len(data)/2)
    for i in range(loop_count):
        # Prepare the inputs
        input_ids = data["input_ids"][i]
        label_ids = data["input_ids"][i+1]
        print(input_ids)
        print(label_ids)
        print(i)
        # Forward pass
        outputs = model(input_ids.unsqueeze(0), labels=label_ids.unsqueeze(0))
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        # Print the loss
        if i % 100 == 0:
            print("Loss:", loss.item())

    # Save the trained model
    model_path=f"./models/{s_path}"
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)

def gen_data_model(d_path,s_path):

    with open(d_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Tokenize the text
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2", add_prefix_space=True)
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

    # Train the model
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.resize_token_embeddings(len(tokenizer))
    optimizer = torch.optim.Adam(model.parameters(), lr=5e-5)
    print(inputs)
    for i in range(len(inputs)):
        # Prepare the inputs
        input_ids = inputs["input_ids"][0][i]
        attention_mask = inputs["attention_mask"][0][i]
        print(i)

        # Forward pass
        outputs = model(input_ids.unsqueeze(0), attention_mask=attention_mask.unsqueeze(0), labels=input_ids.unsqueeze(0))
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        # Print the loss
        if i % 100 == 0:
            print("Loss:", loss.item())

    # Save the trained model
    model_path=f"./models/{s_path}"
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)

