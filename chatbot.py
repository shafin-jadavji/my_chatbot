from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize the conversation history
conversation_history = []

while True:

    # Encode conversation history as a string
    history_string = "\n".join(conversation_history)

    # Fetch prompt from user
    input_text = input("You: ")

    # Tokenize (optimize) prompt
    inputs = tokenizer.encode_plus(input_text, return_tensors="pt")
    # print(f"User input: {input_text} \nToken: {inputs}")


    # Generate output from the model using prompt and history
    outputs = model.generate(**inputs)
    # print(f"Model output: {outputs}")

    # Decode output
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(f"Bot: {output_text}")

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(output_text)
    # print(f"Conversation history: {conversation_history}")