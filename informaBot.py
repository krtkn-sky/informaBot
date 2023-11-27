import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def load_contexts(file_path):
    contexts = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                trigger, response = parts
                contexts[trigger.lower()] = response
    return contexts

def preprocess_input(input_text):
    # Tokenize and remove stopwords
    tokens = word_tokenize(input_text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    return filtered_tokens

def get_response(user_input, contexts):
    user_tokens = preprocess_input(user_input)

    for trigger, response in contexts.items():
        if trigger in user_tokens:
            return response

    return "I'm sorry, I don't understand that."

def main():
    file_path = 'context.txt'
    contexts = load_contexts(file_path)

    print("Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input, contexts)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

