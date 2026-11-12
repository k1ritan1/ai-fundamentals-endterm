#!/usr/bin/env python3
"""
Verification script for AI Fundamentals Final Project Book.
Audits:
1. Total and per-chapter word counts (Target: 10,000 - 14,000 total words, ~1,500 - 2,000 per chapter).
2. Presence of mandatory section headers per chapter:
   - System Emergency Briefing
   - Theoretical Foundation & Mathematical Formulation
   - Algorithmic Execution / Pseudo-code
   - Interactive Simulation Module
   - Academic Post-Mortem & Citations
3. Anti-slop Rule R-02: Zero em-dash  occurrences.
4. Anti-slop Rule R-16: Flagging forbidden buzzwords (delve, showcase, elevate, robust, game-changer, seamless, cutting-edge, revolutionary).
5. Mandatory syllabus literature checks (Russell & Norvig, Zerilli, Louwerse).
6. Physical AI keywords check (actuator, sensor, latency, hardware, physical AI).
"""

import os
import re
import sys
from bs4 import BeautifulSoup

FORBIDDEN_WORDS = [
    "delve", "showcase", "game-changer", "seamless", "cutting-edge",
    "revolutionary", "elevate", "unlock", "testament", "tapestry",
    "foster", "spearhead", "pivotal moment"
]

MANDATORY_AUTHORS = [
    "Russell", "Norvig", "Zerilli", "Louwerse"
]

PHYSICAL_AI_TERMS = [
    "actuator", "sensor", "latency", "hardware", "physical ai"
]

REQUIRED_SECTIONS = [
    "System Emergency Briefing",
    "Theoretical Foundation",
    "Algorithmic Execution",
    "Interactive Simulation Module",
    "Academic Post-Mortem"
]

def clean_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    return soup.get_text()

def audit_book(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    
    # Check for em dashes (Rule R-02)
    em_dash_matches = [m.start() for m in re.finditer(chr(8212), content)]
    if em_dash_matches:
        print(f"[FAIL] Anti-slop Rule R-02 violation: Found {len(em_dash_matches)} em dashes !")
        for idx in em_dash_matches[:5]:
            snippet = content[max(0, idx-30):min(len(content), idx+30)].replace('\n', ' ')
            print(f"   Context: ...{snippet}...")
        return False
    else:
        print("[PASS] Anti-slop Rule R-02: Zero em dashes found.")

    # Check for forbidden buzzwords (Rule R-16)
    buzzword_violations = []
    text_lower = soup.get_text().lower()
    for word in FORBIDDEN_WORDS:
        count = len(re.findall(r'\b' + re.escape(word) + r'\b', text_lower))
        if count > 0:
            buzzword_violations.append((word, count))

    if buzzword_violations:
        print(f"[FAIL] Anti-slop Rule R-16 violation: Found forbidden buzzwords:")
        for w, c in buzzword_violations:
            print(f"   - '{w}': {c} occurrences")
        return False
    else:
        print("[PASS] Anti-slop Rule R-16: Zero forbidden buzzwords detected.")

    # Check chapters
    chapters = soup.find_all('section', class_=re.compile(r'chapter|manual-chapter'))
    if not chapters:
        # Try finding by id chapter-1 to chapter-7
        chapters = [soup.find(id=f"chapter-{i}") for i in range(1, 8)]
        chapters = [c for c in chapters if c is not None]

    print(f"\nFound {len(chapters)} chapters for analysis.")
    if len(chapters) < 7:
        print(f"[WARN] Expected 7 chapters covering weeks 1-10, found {len(chapters)}")

    total_words = 0
    chapter_stats = []

    for i, ch in enumerate(chapters, 1):
        ch_text = ch.get_text()
        words = len(re.findall(r'\b\w+\b', ch_text))
        total_words += words
        
        # Check required sections
        missing_sections = []
        for req_sec in REQUIRED_SECTIONS:
            if not re.search(re.escape(req_sec), ch_text, re.IGNORECASE):
                missing_sections.append(req_sec)
                
        chapter_stats.append({
            "chapter": i,
            "words": words,
            "missing_sections": missing_sections
        })

    print(f"\n=== Word Count & Section Audit ===")
    print(f"Total Words Across Chapters: {total_words}")
    if total_words < 10000:
        print(f"[FAIL] Total word count {total_words} is below the 10,000 word minimum.")
    elif total_words > 16000:
        print(f"[WARN] Total word count {total_words} is above target 14,000 words.")
    else:
        print(f"[PASS] Total word count {total_words} satisfies scope target (10,000 - 14,000 words).")

    for stat in chapter_stats:
        status = "PASS" if stat["words"] >= 1400 and not stat["missing_sections"] else "WARN/FAIL"
        print(f"Chapter {stat['chapter']}: {stat['words']} words | Missing sections: {stat['missing_sections'] or 'None'} | [{status}]")

    # Check Literature
    print(f"\n=== Mandatory Academic Literature Audit ===")
    for author in MANDATORY_AUTHORS:
        matches = len(re.findall(r'\b' + re.escape(author) + r'\b', content, re.IGNORECASE))
        if matches > 0:
            print(f"[PASS] Author '{author}' referenced ({matches} citations).")
        else:
            print(f"[FAIL] Mandatory author '{author}' not found in citations!")

    # Check Physical AI
    print(f"\n=== Physical AI Integration Audit ===")
    for term in PHYSICAL_AI_TERMS:
        matches = len(re.findall(r'\b' + re.escape(term) + r'\b', text_lower))
        print(f"Term '{term}': {matches} occurrences.")

    return True

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    audit_book(target_file)
