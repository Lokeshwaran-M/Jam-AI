import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the saved model and tokenizer

model_path ="gpt2"

model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

def ans(pmt="none"):
    # Get user input
    if "stop" in pmt :
        return "stoping"
    elif pmt=="none":
        return "no inputs"
    model.config.pad_token_id = tokenizer.eos_token_id
    # Encode the input and generate output
    input_ids = tokenizer.encode(pmt, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=model.device)
    model.to("cuda")  # move the model to the GPU
    output_ids = model.generate(input_ids.to("cuda"), max_length=50, num_beams=5, no_repeat_ngram_size=2,attention_mask=attention_mask.to("cuda"))
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output


def chat():
    while True:
        # Get user input
        pmt = input("[]=> : ")
    
        if pmt=="stop" :
            break
        global model
        model.config.pad_token_id = tokenizer.eos_token_id
        # Encode the input and generate output
        input_ids = tokenizer.encode(pmt, return_tensors="pt")
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=model.device)
        model.to("cuda")  # move the model to the GPU
        output_ids = model.generate(input_ids.to("cuda"), max_length=50, num_beams=5, no_repeat_ngram_size=2,attention_mask=attention_mask.to("cuda"))
        output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        
        # Print the output
        print("Bot:", output)












