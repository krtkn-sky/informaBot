# InformaBot: Context-Based Chatbot with NLTK

InformaBot is a simple command-line based chatbot implemented in Python that uses Natural Language Processing (NLP) techniques provided by the Natural Language Toolkit (NLTK). The chatbot responds to user input based on predefined trigger words associated with various contexts.

![image](https://github.com/krtkn-sky/informaBot/assets/121655285/e3064a1f-66e2-438d-893d-ad854d2fb278)

## How to Use

1. **Install Dependencies:**
   Make sure you have Python installed on your system. Install the required dependencies by running the following command:

   ```bash
   pip install nltk
   ```

2. **Run InformaBot:**
   Execute the chatbot script by running:

   ```bash
   python informaBot.py
   ```

   InformaBot will greet you and wait for your input. Type 'exit' to end the conversation.

## Contexts and Trigger Words

InformaBot recognizes specific trigger words associated with different contexts. These trigger words are defined in the `context.txt` file.

### Example Trigger Words:

1. **greeting**
2. **goodbye**
3. **age**
4. **weather**
5. **joke**
6. **name**
7. **programming**
8. **python**
9. **music**
10. **food**
11. **hobby**
12. **sports**
13. **technology**
14. **mathematics**
15. **movie**
16. **book**
17. **travel**
18. **history**
19. **news**
20. **emotion**

### NLTK Techniques Used:

1. **Tokenization:**
   The NLTK library is used for tokenizing user input, breaking it down into individual words for analysis.

2. **Stopword Removal:**
   Stopwords, common words like "the" and "is," are removed from the user input to focus on relevant words.

3. **Text Processing:**
   InformaBot preprocesses user input, converting it to lowercase and removing non-alphanumeric characters.

## Customizing InformaBot

Feel free to customize the `context.txt` file by adding more trigger words. Adjustments can also be made to the NLTK techniques used for text processing based on specific requirements.

Happy chatting with InformaBot!
