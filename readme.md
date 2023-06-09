### CommandGPT

CommandGPT is a simple command line tool for GPT-3.5 to convert

- Natural Language to PowerShell command,
- Natural Language to Bash command,
- Bash to PowerShell command,
- PowerShell to Natural Language,
- Bash to Natural Language.

**NOTE**: This project requires a valid OPENAI API key. You can get one [here](https://beta.openai.com/).

#### Installation

```bash
pip install -r requirements.txt
```

#### Usage

```bash
python main.py [-h] -i INPUT -o OUTPUT -c COMMAND [-x] [-d]
```

### Options:

    -h, --help              show this help message and exit
    -i INPUT, --input INPUT
                            Input language
    -o OUTPUT, --output OUTPUT
                            Output language
    -c COMMAND, --command COMMAND
                            Command to will be converted
    -x, --execute         Execute command and exit
    -d, --debug           Debug mode


https://user-images.githubusercontent.com/47084109/231006746-ccd82554-0ec7-431e-a612-bbb3f29f0dd4.mp4

for example,

```bash
python main.py -i nat -o ps -c "Create a file named test.txt"
```

or use the interactive mode


https://user-images.githubusercontent.com/47084109/231006889-ceb8d60c-dea3-4c8f-88d6-a50be29ee615.mp4


```bash
python main.py
```

#### Some Use Cases

- Convert Natural Language to PowerShell command

```
Welcome to the CommandGPT!
1. Natural Language to PowerShell
2. Natural Language to Bash
3. PowerShell to Bash
4. Bash to PowerShell
5. PowerShell to Natural Language
6. Bash to Natural Language
7. Exit

Please select an option: 1
Please enter a natural language command: Create a file named test.txt
PowerShell equivalent: New-Item -ItemType File -Path "test.txt"
```

- Convert Natural Language to Bash command

```
Welcome to the CommandGPT!
1. Natural Language to PowerShell
2. Natural Language to Bash
3. PowerShell to Bash
4. Bash to PowerShell
5. PowerShell to Natural Language
6. Bash to Natural Language
7. Exit

Please select an option: 2
Please enter a natural language command: List all files in the current directory except test.txt and files starting with a dot.
Bash equivalent: ls -p | grep -v / | grep -v '^test\.txt$' | grep -v '^\.'
```

- Convert Bash to Natural Language

```
1. Natural Language to PowerShell
2. Natural Language to Bash
3. PowerShell to Bash
4. Bash to PowerShell
5. PowerShell to Natural Language
6. Bash to Natural Language
7. Exit

Please select an option: 6
Please enter a bash command: curl -X "GET" localhost:9200/_cat/indices?v=true&pretty=true
Natural Language equivalent: List all indices in Elasticsearch.
```
