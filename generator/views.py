from django.shortcuts import render
import subprocess

def generator_view(request):
    quest = subprocess.run(["ollama", "run", "mistral",
    "generate a new medieval fantasy quest hook in 1 short sentence, be unique"
    ], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip()

    villager = subprocess.run(["ollama", "run", "mistral",
    "generate a random medieval name (perhaps Frankish, Visigothic or Anglo-Saxon), a medieval job and a random personal quirk in 1 short sentence."
    ], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip()

    adventurer = subprocess.run(["ollama", "run", "mistral",
    "generate the name, background and quirk of a new medieval fantasy adventurer in 1 short sentence, be unique"
    ], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip()

    monster = subprocess.run(["ollama", "run", "mistral",
    "in one short sentence, generate the name, habitat and interesting ability/habit of a new medieval fantasy animal/monster, be unique"
    ], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip()

    weapon = subprocess.run(["ollama", "run", "mistral",
    "generate the name, appearance and desire of a new medieval fantasy magical weapon in 1 short sentence, be unique"
    ], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip()

    item = subprocess.run(["ollama", "run", "mistral", ""
    "generate the name, appearance and ability of a new medieval fantasy magical item in 1 short sentence"
    ], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip()

    return render(request, 'generators.html', { "quest" : quest , "villager" : villager, "adventurer" : adventurer, "monster" : monster, "weapon" : weapon, "item" : item})