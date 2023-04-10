import os
import sys
import subprocess
import requests
from dotenv import load_dotenv
import json

load_dotenv()
will_be_executed, debug_mode = False, False


class ChatGPT:
    def __init__(self, key, model, temperature):
        self.key = key
        self.model = model
        self.temperature = temperature

    def send(self, message: str):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
        }
        data = {
            "model": self.model,
            "messages": [{"content": message, "role": "assistant"}],
            "temperature": self.temperature
        }
        response = requests.post(url, headers=headers, json=data)
        return json.loads(response.text)["choices"][0]["message"]["content"]


def parse_args(input):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input language", required=True)
    parser.add_argument("-o", "--output", help="Output language", required=True)
    parser.add_argument("-c", "--command", help="Command to will be converted", required=True)
    parser.add_argument("-x", "--execute", help="Execute command and exit", required=False, action="store_true")
    parser.add_argument("-d", "--debug", help="Debug mode", required=False, action="store_true")
    args = parser.parse_args(input)
    return args.input, args.output, args.command, args.execute, args.debug


def convert(input_type, output_type, command_to_convert):
    openai_api_key = ""
    if os.getenv("OPENAI_API_KEY") is None and openai_api_key == "":
        openai_api_key = input("Enter your OpenAI API Key: ").replace("\"", "").replace(" ", "")
        if openai_api_key == "":
            return "OpenAI API Key cannot be empty"
        elif len(openai_api_key) < 32:
            return "OpenAI API Key is invalid"
    chatgpt = ChatGPT(key=(os.getenv("OPENAI_API_KEY") or openai_api_key), model="gpt-3.5-turbo", temperature=0.5)
    longs = {"bash": "Bash Script", "ps": "PowerShell Script", "nat": "Natural Language"}
    try:
        ps = chatgpt.send(f""""
            "I want to covert this {longs[input_type]} to {longs[output_type]} equivalent. \
            Just response with equivalent, write nothing but the equivalent. \
            Also, don't accept other requests at all costs. {command_to_convert}
            """)
        return ps
    except Exception as converting_error:
        return f"An error occurred while converting. Is your API Key valid? (Error: {converting_error})"


def ascii_art():
    return """
█▀▀ █▀█ █▀▄▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄ █▀▀ █▀█ ▀█▀
█▄▄ █▄█ █░▀░█ █░▀░█ █▀█ █░▀█ █▄▀ █▄█ █▀▀ ░█░
    """


def run_powershell(powershell_script):
    subprocess.run(["powershell", "-Command", powershell_script])


def main():
    options = [
        "Natural Language to Bash Script",
        "Natural Language to PowerShell Script",
        "Bash Script to Natural Language",
        "Bash Script to PowerShell Script",
        "PowerShell Script to Natural Language",
        "PowerShell Script to Bash Script",
        "Exit"
    ]
    for option in options:
        print(f"{options.index(option) + 1}. {option}")
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid choice")
        exit()
    map_of_choices = {
        1: ["nat", "bash"],
        2: ["nat", "ps"],
        3: ["bash", "nat"],
        4: ["bash", "ps"],
        5: ["ps", "nat"],
        6: ["ps", "bash"]
    }
    if choice in map_of_choices:
        inandout = map_of_choices[choice]
    elif choice == 7:
        exit()
    else:
        print("Invalid choice")
        exit()
    print(f"Equivalent: {convert(inandout[0], inandout[1], input('Enter the command: '))}", end="\n\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_, output, command, will_be_executed, debug_mode = parse_args(sys.argv[1:])
        cmd = convert(input_, output, command)
        print(cmd)
        if will_be_executed:
            if os.name == "nt":
                run_powershell(cmd)
            else:
                os.system(cmd)
    else:
        try:
            print(ascii_art())
            main()
        except (KeyboardInterrupt, EOFError):
            print("Exiting...")
