"""
CP1404
Time estimated: 20 minutes ( 10:12pm )
Time finished: 10:34pm ( 22 minutes )
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)