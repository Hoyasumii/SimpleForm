"""
Project: SimpleForm
Author: Alan Reis Anjos
License: Creative Commons Attribution 4.0 International License
License Details: https://creativecommons.org/licenses/by/4.0/
"""

import os, sys, re
from typing import Any

class SimpleForm:
    
    _display = ""
    _count = 0
    _values = { }

    @property
    def values(self):
        return { key: value for key, value in self.__dict__.items() if key not in [ "_display", "_count", "orderedList", "spacing", "separator" ] }

    def __init__(self, title: str = "", separator: bool = True, orderedList: bool = True, spacing: int = 0):
        
        assert isinstance(title, str), "The title must be a string"
        assert isinstance(separator, bool), "The separator must be a boolean"
        assert isinstance(orderedList, bool), "The orderedList must be a boolean"
        assert isinstance(spacing, int), "The spacing must be a integer"

        self._display = f"{ title }"
        
        self.separator = separator
        if self.separator: self._display += f"\n{ '-' * 100 }"

        self.orderedList = orderedList
        self.spacing = " " * spacing

    def __call__(self):
        for key, value in self._values.items():
            value['title'] = key
            self._input(**value)
        if self.separator: print(f"{ '-' * 100 }")

    def add(self, **kwargs):
        for key, value in kwargs.items():
            assert isinstance(value, dict), f"The { key } must be a dict"
            assert isinstance(value["type"], type), f"The { key } must have a type"
            assert 'description' in value, f"The { key } must have a description"
        self._values.update(kwargs)

    def _clear(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def _input(self, **properties):

        self._count += 1
        self._clear()
        newEntryText = f"{ self.spacing }{ f"{ self._count }." if self.orderedList else "-" } { properties['description'] if 'description' in properties else '' }"
        
        if "min" in properties or "max" in properties:
            newEntryText += f" ({ f"min: { properties['min'] if 'min' in properties else '' } "}, max: { properties['max'] })"

        if "default" in properties:
            newEntryText += f" (default: { properties['default'] })"

        if self._display != "": print(self._display)

        newEntry = ""

        try:
            newEntry = input(newEntryText + ": ")
            if newEntry != "": newEntry = properties['type'](newEntry)

            if "default" in properties and newEntry == "":
                newEntry = properties['default']
        
            if properties['type'] == str:
                if "min" in properties and len(newEntry) < properties['min']:
                    raise

                if "max" in properties and len(newEntry) > properties['max']:
                    raise

            elif properties['type'] == int or properties['type'] == float:
                if "min" in properties and newEntry < properties['min']:
                    raise

                if "max" in properties and newEntry > properties['max']:
                    raise

            if "validate" in properties:
                assert re.match(properties['validate'], newEntry)

            self.__dict__[properties['title']] = newEntry
            self._display += f"{ "\n" if self._display != "" else "" }{ newEntryText }: { newEntry }"
        
        except ( ValueError, TypeError, AssertionError ):
            self._count -= 1
            self._input(**properties)

        except KeyboardInterrupt:
            sys.exit(0)

if __name__=="__main__":
    x = SimpleForm("Hello World", orderedList=False, spacing=2)
    
    x.add(name={
        "type": str,
        "description": "Your name",
        "default": "John Doe"
    }, age={
        "type": int,
        "description": "Your age",
        "min": 1,
        "max": 100,
        "default": 18
    }, email={
        "type": str,
        "description": "Your email",
        "validate": r"^[a-zA-Z0-9._%+-]{4,}@[a-z0-9.-]{2,}\.[a-z]{2,}$",
        "default": "alanreisanjo@gmail.com"
    })

    x()

    print(x.values)