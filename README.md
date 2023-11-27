```
# InformaBot: Context-Based Chatbot with NLTK

InformaBot is a simple command-line based chatbot implemented in Python that uses Natural Language Processing (NLP) techniques provided by the Natural Language Toolkit (NLTK). The chatbot responds to user input based on predefined trigger words associated with various contexts.

## How to Use

1. **Install Dependencies:**
   Make sure you have Python installed on your system. Install the required dependencies by running the following command:

   ```bash
   pip install nltk
   ```

2. **Run InformaBot:**
   Execute the chatbot script by running:

   ```bash
   python chatbot.py
   ```

   InformaBot will greet you and wait for your input. Type 'exit' to end the conversation.

## Contexts and Trigger Words

InformaBot recognizes specific trigger words associated with different contexts. These trigger words are defined in the `context.txt` file. Each line in the file consists of a trigger word followed by a detailed response associated with that context.

### Example Trigger Words:

1. **greeting**: Hello, hi
2. **goodbye**: Goodbye, bye
3. **age**: age
4. **weather**: weather
5. **joke**: joke
6. **name**: name
7. **programming**: programming
8. **python**: python
9. **music**: music
10. **food**: food
11. **hobby**: hobby
12. **sports**: sports
13. **technology**: technology
14. **mathematics**: mathematics
15. **movie**: movie
16. **book**: book
17. **travel**: travel
18. **history**: history
19. **news**: news
20. **emotion**: emotion

### NLTK Techniques Used:

1. **Tokenization:**
   The NLTK library is used for tokenizing user input, breaking it down into individual words for analysis.

2. **Stopword Removal:**
   Stopwords, common words like "the" and "is," are removed from the user input to focus on relevant words.

3. **Text Processing:**
   InformaBot preprocesses user input, converting it to lowercase and removing non-alphanumeric characters.

## Customizing InformaBot

Feel free to customize the `context.txt` file by adding more trigger words and responses to expand InformaBot's capabilities. Adjustments can also be made to the NLTK techniques used for text processing based on specific requirements.

Happy chatting with InformaBot!
```

This version of the README now refers to the chatbot as "InformaBot" throughout the document.
