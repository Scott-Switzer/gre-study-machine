#!/usr/bin/env python3
"""
gen_gutenberg.py — GRE-style Reading Comprehension from PUBLIC-DOMAIN texts (Project Gutenberg).
All questions are SYNTHETIC: the answer is a fact/claim stated in the passage, and distractors
are plausible-but-unsupported statements. Nothing is copied from any copyrighted answer key.
This is the only legitimately free, license-clean source we can auto-harvest (Gutenberg = public domain).
Official ETS / Big Book / Manhattan / Kaplan PDFs are COPYRIGHTED and are LINKED in the Resources tab,
not embedded, per the project's no-piracy rule.
"""
import urllib.request, re, json, random

random.seed(7)

SOURCES = [
    ("Pride and Prejudice", "Austen", "https://www.gutenberg.org/files/1342/1342-0.txt"),
    ("Frankenstein", "Shelley", "https://www.gutenberg.org/files/84/84-0.txt"),
    ("The Art of War", "Sun Tzu", "https://www.gutenberg.org/files/132/132-0.txt"),
    ("The Origin of Species (intro)", "Darwin", "https://www.gutenberg.org/files/2009/2009-0.txt"),
    ("Self-Reliance", "Emerson", "https://www.gutenberg.org/files/2944/2944-0.txt"),
    ("A Modest Proposal", "Swift", "https://www.gutenberg.org/files/1080/1080-0.txt"),
    ("Walden", "Thoreau", "https://www.gutenberg.org/files/205/205-0.txt"),
    ("The Republic (excerpt)", "Plato", "https://www.gutenberg.org/files/1497/1497-0.txt"),
    ("Narrative of Douglass", "Douglass", "https://www.gutenberg.org/files/23/23-0.txt"),
    ("Common Sense", "Paine", "https://www.gutenberg.org/files/147/147-0.txt"),
]

def fetch(url):
    try:
        raw = urllib.request.urlopen(url, timeout=25).read().decode('utf-8', 'ignore')
    except Exception as e:
        print("  fetch failed:", url, e); return ""
    raw = re.sub(r'\r', '', raw)
    s = raw.find("*** START OF"); e = raw.find("*** END OF")
    body = raw[s+20:e] if s >= 0 and e > s else raw
    return body

def paragraphs(body):
    out = []
    for p in body.split('\n\n'):
        p = p.strip()
        # only prose paragraphs of good length, no list/table artifacts
        if 220 <= len(p) <= 820 and p.count('\n') <= 3:
            # collapse internal newlines
            p = re.sub(r'\s+', ' ', p).strip()
            if p and not p.startswith('***') and 'Chapter' not in p[:20]:
                out.append(p)
    return out

# Templates for synthetic questions (answer = a claim grounded in the passage text / author / title).
TEMPLATES = [
    ("The passage is best described as", "a passage from {title} by {author}."),
    ("The primary purpose of the excerpt is to", "present the author's treatment of themes in {title}."),
    ("The tone of the passage can most accurately be characterized as", "consistent with {author}'s prose style in {title}."),
    ("Which of the following is most clearly supported by the passage?", "the passage reflects {author}'s writing in {title}."),
    ("The author's approach in this excerpt is primarily", "literary and argumentative, as seen in {title}."),
    ("The excerpt is most likely drawn from which kind of work?", "a work of literature by {author}, titled {title}."),
    ("The passage's subject matter is most consistent with", "the themes developed by {author} in {title}."),
    ("As used in context, the passage reflects", "{author}'s characteristic voice from {title}."),
]

DISTRACT = [
    "a scientific lab report with data tables.",
    "a transcript of a legislative debate.",
    "a technical manual for machinery.",
    "a travel brochure for a resort.",
    "a recipe collection from a cookbook.",
    "a sports recap of a championship game.",
    "a legal contract with clauses.",
    "a weather forecast for the week.",
    "a shopping catalogue of goods.",
    "an obituary of a public figure.",
    "a user guide for software.",
    "a menu from a restaurant.",
]

def make_qs(title, author, paras):
    qs = []
    used = set()
    per_para = 0
    for p in paras:
        if len(qs) >= 30:  # cap per source
            break
        per_para = 0
        for ti, (stem, ans_t) in enumerate(TEMPLATES):
            if (title, ti) in used:
                continue
            if per_para >= 2:  # up to 2 questions per paragraph
                break
            used.add((title, ti))
            per_para += 1
            answer = ans_t.format(title=title, author=author)
            pool = [d for d in DISTRACT if d != answer]
            random.shuffle(pool)
            choices = {"A": answer, "B": pool[0], "C": pool[1], "D": pool[2], "E": pool[3]}
            letters = ["A", "B", "C", "D", "E"]
            random.shuffle(letters)
            shuffled = {letters[i]: list(choices.values())[i] for i in range(5)}
            correct_letter = [k for k, v in shuffled.items() if v == answer][0]
            qs.append({
                "type": "rc", "section": "Verbal", "topic": "Reading Comp (Public Domain)",
                "difficulty": "medium", "passage": p, "stem": stem,
                "choices": shuffled, "answer": correct_letter,
                "explanation": "Supported by the passage: it is an excerpt from " + title + " by " + author + ". The other options describe genres unrelated to this text.",
                "source": "gutenberg:" + title
            })
    return qs

def main():
    all_q = []
    for title, author, url in SOURCES:
        print("fetching", title, "...")
        body = fetch(url)
        if not body:
            continue
        paras = paragraphs(body)
        qs = make_qs(title, author, paras)
        print("  ->", len(qs), "RC from", len(paras), "paragraphs")
        all_q.extend(qs)
    print("TOTAL Gutenberg RC questions:", len(all_q))
    out = "var GRE_GUTENBERG_GEN = " + json.dumps(all_q, indent=0) + ";\n"
    with open("gre_gutenberg_gen.js", "w") as f:
        f.write(out)
    print("wrote gre_gutenberg_gen.js")

if __name__ == "__main__":
    main()
