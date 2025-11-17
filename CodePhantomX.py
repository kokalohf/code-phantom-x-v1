# -*- coding: utf-8 -*-
"""
Code Phantom X v1.1
Nevidljivi AI pomoćnik – Ghost Pair Programming
Ti kucaš, Phantom hvata bagove, Ghost predlaže popravke
+ Interaktivni unos + popravljeno hvatanje grešaka
"""

import time
import random
from datetime import datetime

# ────── PHANTOM: hvata bagove (popravljeno za return, if, itd.) ──────
def phantom_analyze(code):
    issues = []
    lines = code.splitlines()
    
    for i, line in enumerate(lines, 1):
        s = line.strip()
        
        # 1. = umesto == u bilo kom izrazu (if, return, while...)
        if "=" in s and "==" not in s and not s.startswith("#"):
            if any(op in s for op in ["if", "while", "elif", "return", "for"]):
                issues.append(f"Linija {i}: Koristiš '=' umesto '==' – verovatno greška!")
        
        # 2. Debug print
        if "print(" in s and "debug" in s.lower():
            issues.append(f"Linija {i}: Izbaci debug print iz produkcije!")
        
        # 3. TODO
        if "TODO" in s:
            issues.append(f"Linija {i}: Imaš TODO – implementiraj!")
        
        # 4. pass
        if "pass" in s and not s.startswith("#"):
            issues.append(f"Linija {i}: 'pass' je prazan – dodaj logiku!")
    
    # 5. Predugačka funkcija
    if len(lines) > 25:
        issues.append(f"Funkcija predugačka ({len(lines)} linija) – razbij na manje!")
    
    return issues or ["Kod je čist! Nema očiglednih bagova."]

# ────── GHOST: predlaže popravke kao senior dev ──────
def ghost_suggest(code):
    suggestions = []
    
    # Type hintovi
    if "def " in code and "->" not in code:
        try:
            func = code.split("def ")[1].split("(")[0].strip()
            suggestions.append(f"Dodaj type hintove: def {func}(x: int) -> int:")
        except:
            suggestions.append("Dodaj type hintove za parametre i povratnu vrednost.")
    
    # Docstring
    if "def " in code and not any(d in code for d in ['"""', "'''"]):
        suggestions.append("Napravi docstring – objasni šta radi funkcija!")
    
    # Testovi
    if "def " in code:
        suggestions.append("Napiši unittest – proveri edge case-ove!")
    
    # Komentari
    if any(len(l.strip()) > 60 and not l.strip().startswith("#") for l in code.splitlines()):
        suggestions.append("Dodaj inline komentare – olakšaj čitanje!")
    
    # List comprehension
    if "for " in code and "append" in code:
        suggestions.append("Koristi list comprehension umesto for + append!")
    
    return random.choice(suggestions) if suggestions else "Odličan stil! Ništa za popravku."

# ────── LOG U STILU GHOST PAIR ──────
def log(msg, role="SYSTEM"):
    prefix = {"PROGRAMER": "TI", "PHANTOM": "PHANTOM", "GHOST": "GHOST"}.get(role, "SYSTEM")
    print(f"[{datetime.now().strftime('%H:%M')}] [{prefix.ljust(8)}] {msg}")

# ────── INTERAKTIVNI REŽIM – TI KUCAŠ, ONI REAGUJU ──────
def interactive_session():
    log("Code Phantom X v1.1 – INTERAKTIVNI REŽIM", "SYSTEM")
    log("Kucaj kod, pritisni Enter dva puta kada završiš.", "SYSTEM")
    log("Za izlaz: kucaj 'exit' i Enter", "SYSTEM")
    print("─" * 80)
    
    while True:
        print("\nTvoj kod (završi sa praznim redom):")
        code_lines = []
        empty_line_count = 0
        
        while empty_line_count < 2:
            try:
                line = input()
                if line.strip().lower() == "exit":
                    log("Code Phantom X zaustavljen. Ćao!", "SYSTEM")
                    return
                if line == "":
                    empty_line_count += 1
                else:
                    empty_line_count = 0
                code_lines.append(line)
            except EOFError:
                break
        
        # Ukloni prazne linije na kraju
        while code_lines and code_lines[-1] == "":
            code_lines.pop()
        
        if not code_lines:
            continue
        
        code = "\n".join(code_lines)
        
        log("Ti si uneo:", "PROGRAMER")
        for line in code_lines:
            print(f"   > {line}")
        print()
        
        time.sleep(1)
        
        # PHANTOM analizira
        for issue in phantom_analyze(code):
            log(issue, "PHANTOM")
        
        time.sleep(1)
        
        # GHOST predlaže
        log(ghost_suggest(code), "GHOST")
        
        print("─" * 80)

# ────── POKRETANJE ──────
if __name__ == "__main__":
    interactive_session()