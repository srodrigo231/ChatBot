# ChatBot
Chatbot with RASA with Spanish support.

### How to install
    1. Install python (3.7.9 current version)
    2. Create a virtual envoriment (python3 -m venv .venv)
    3. pip -r install requirements.txt
    4. pip install spacy
    5. pip install rasa
    6. python -m spacy download es_core_news_sm (sm - small, md - medium, lg - large) (es_dep_news_trf ???)

### Rasa commands
    1. rasa init
    2. rasa train
    3. rasa shell
    4. rasa run
    5. rasa interactive
    6. rasa visualize
    7. rasa run actions
    8. rasa x

### Rasa Multi session support
Rasa frameworlk support a session user a long 60 minutes by default.

### Rasa Stress test
To make stress test you would use this [tool](https://github.com/salgieri/rasa-locust-stress-test).

### Multilengual Support
A futute feature is the bilingual support (es/en). This is an [example](https://gitlab.com/langnerd/chatbot-engine) but with previous Rasa versions.
