from .ai_assistant import main, ask_question


def ai_assistant_ask_question(question, api_key, model, role, quiet):
    return ask_question(question, api_key, model, role, quiet)


def ai_assistant_main():
    main()
