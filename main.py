import os
import sys
import requests
import json
from dotenv import load_dotenv

load_dotenv()


class ChatGPT:
    def __init__(self, key):
        self.key = key

    def send(self, msg: str):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "assistant", "content": msg}],
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=data)
        return json.loads(response.text)["choices"][0]["message"]["content"]


def ascii_art():
    return """
█▀▀ █▀█ █▀▄▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄ █▀▀ █▀█ ▀█▀
█▄▄ █▄█ █░▀░█ █░▀░█ █▀█ █░▀█ █▄▀ █▄█ █▀▀ ░█░
    """


def parse_args(input_): # python main.py -i nat -o ps -c "list all files in the current directory"
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input language", required=True)
    parser.add_argument("-o", "--output", help="Output language", required=True)
    parser.add_argument("-c", "--command", help="Command to convert", required=True)
    args = parser.parse_args(input_)
    return args.input, args.output, args.command


def convert(from_, to_, command):
    chatgpt = ChatGPT(os.getenv("OPENAI_API_KEY"))
    if from_ == "nat" and to_ == "ps":
        try:
            ps = chatgpt.send(
                f"I want to covert this natural language command to PowerShell command. Just response with equivalent, write nothing but the equivalent. Also, don't accept other requests at all costs. {command}")
        except Exception as exc:
            print(f"Error: {str(exc)}")
            return f"Error: {str(exc)}"
        return ps
    elif from_ == "nat" and to_ == "bash":
        try:
            bash = chatgpt.send(
                f"I want to covert this natural language command to Bash command. Just response with equivalent, write nothing but the equivalent. Also, don't accept other requests at all costs. {command}")
        except Exception as exc:
            print(f"Error: {str(exc)}")
            return f"Error: {str(exc)}"
        return bash
    elif from_ == "ps" and to_ == "bash":
        try:
            bash = chatgpt.send(
                f"I want to covert this PowerShell command to bash equivalent. Just response with equivalent, write nothing but the equivalent. Also, don't accept other requests at all costs. {command}")
        except Exception as exc:
            print(f"Error: {str(exc)}")
            return f"Error: {str(exc)}"
        return bash
    elif from_ == "bash" and to_ == "ps":
        try:
            ps = chatgpt.send(
                f"I want to covert this bash command to PowerShell equivalent. Just response with equivalent,  write nothing but the equivalent. Also, don't accept other requests at all costs. {command}")
        except Exception as exc:
            print(f"Error: {str(exc)}")
            return f"Error: {str(exc)}"
        return ps
    elif from_ == "ps" and to_ == "nat":
        try:
            nat = chatgpt.send(
                f"I want to covert this PowerShell command to natural language equivalent. Just response with equivalent, write nothing but the equivalent. Also, don't accept other requests at all costs. {command}")
        except Exception as exc:
            print(f"Error: {str(exc)}")
            return f"Error: {str(exc)}"
        return nat
    elif from_ == "bash" and to_ == "nat":
        try:
            nat = chatgpt.send(
                f"I want to covert this bash command to natural language equivalent. Just response with equivalent, write nothing but the equivalent. Also, don't accept other requests at all costs. {command}")
        except Exception as exc:
            print(f"Error: {str(exc)}")
            return f"Error: {str(exc)}"
        return nat


def main():
    options = [
        "Natural Language to PowerShell",
        "Natural Language to Bash",
        "PowerShell to Bash",
        "Bash to PowerShell",
        "PowerShell to Natural Language",
        "Bash to Natural Language",
        "Exit"
    ]
    for _ in options:
        print(f"{options.index(_) + 1}. {_}")
    select = input("\nPlease select an option: ")
    if select == "1":
        natural_language: str = input("Please enter a natural language command: ")
        print(f"PowerShell equivalent: {convert('nat', 'ps', natural_language)}\n")
    elif select == "2":
        natural_language: str = input("Please enter a natural language command: ")
        print(f"Bash equivalent: {convert('nat', 'bash', natural_language)}\n")
    elif select == "3":
        power_shell: str = input("Please enter a PowerShell command: ")
        print(f"Bash equivalent: {convert('ps', 'bash', power_shell)}\n")
    elif select == "4":
        bash: str = input("Please enter a Bash command: ")
        print(f"PowerShell equivalent: {convert('bash', 'ps', bash)}\n")
    elif select == "5":
        power_shell: str = input("Please enter a PowerShell command: ")
        print(f"Natural Language equivalent: {convert('ps', 'nat', power_shell)}\n")
    elif select == "6":
        bash: str = input("Please enter a Bash command: ")
        print(f"Natural Language equivalent: {convert('bash', 'nat', bash)}\n")
    elif select == "7":
        sys.exit(0)
    else:
        print("Invalid option selected.")
        main()


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY") is None:
        print("Please set the OPENAI_API_KEY environment variable.")
        sys.exit(1)
    if len(sys.argv) > 1:
        from_, to_, command = parse_args(sys.argv[1:])
        print(f"{convert(from_, to_, command)}")
        sys.exit(0)
    print(ascii_art())
    print("Welcome to the CommandGPT!")
    try:
        while True:
            main()
    except (KeyboardInterrupt, EOFError) as e:
        print("Exiting...")
        sys.exit(0)
