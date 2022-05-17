# Chatbot
Chatbot with RASA with Spanish support.

# Chatbot Skills
This chatbot will able to these over shifts:
1. Consult (developing)
2. Update (planning)
3. Schedule (planning)
4. Decline (planning)

### How to install
    1. Install python (3.7.9 current version)
    2. Create a virtual envoriment (python3 -m venv .venv)
    3. pip -r install requirements.txt
    4. pip install spacy
    5. pip install rasa
    6. python -m spacy download es_core_news_sm (sm - small, md - medium, lg - large) (es_dep_news_trf ???)

### Rasa commands
    1. rasa init : to start rasa framework
    2. rasa train : to train a model
    3. rasa shell : to run rasas server and use promt terminal to chat with bot
    4. rasa run : to run rasa server (PORT: 5005)
    5. rasa interactive : to run rasas server and use promt terminal to chat with bot in an interactive mode.
    6. rasa visualize : to visualize conversational tree.
    7. rasa run actions : it's an very important command to execute CUSTOM ACTIONS. (PORT: 5055)
    8. rasa x : to start web view RASA agent.
    9. rasa data validate : to validate consistense across different config files.

### Rasa Multi session support
Rasa framework supports a session user a long 60 minutes by default.

### Rasa Stress test
To make stress test you would use this [tool](https://github.com/salgieri/rasa-locust-stress-test).

### Multilengual Support
A future feature is the bilingual support (es/en). This is an [example](https://gitlab.com/langnerd/chatbot-engine) but with previous Rasa versions.
