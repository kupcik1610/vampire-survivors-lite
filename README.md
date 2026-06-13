# Mini Survivors 🎮

A tiny "Vampire Survivors"-style game you build **from scratch** to learn
programming — no experience needed. Move a dot, auto-shoot the enemies that
chase you, survive as long as you can.

You can build it in **two languages**. They're the same game, so pick whichever
you like (or do one, then the other to see how the ideas carry over):

- **JavaScript** — runs in a web browser, **nothing to install**. Easiest start.
- **Python** — runs with `pygame`, needs a quick one-time setup.

---

## 📁 What's in here

```
mini-survivors/
├── README.md                ← you are here
│
├── curriculum/              ← the lessons as PDFs (START HERE)
│   ├── Curriculum-JavaScript.pdf
│   └── Curriculum-Python.pdf
│
├── javascript/
│   ├── primer.html          ← 🌐 JavaScript warm-up — open this FIRST
│   ├── starter.html         ← ✏️  YOU build the game in this file
│   └── index.html           ← ✅  finished answer key (peek only when stuck)
│
└── python/
    ├── primer.py            ← 🐍 Python warm-up — run this FIRST
    ├── starter.py           ← ✏️  YOU build the game in this file
    ├── game.py              ← ✅  finished answer key (peek only when stuck)
    └── requirements.txt     ← the one package the Python version needs
```

---

## 🚀 How to start

1. **Open the curriculum PDF** for your language in the `curriculum/` folder.
   It walks you through the whole game, one small stage at a time.
2. **Open the matching `starter.` file** in a code editor
   ([VS Code](https://code.visualstudio.com/) is free and great).
3. **Follow the stages**, adding the code bit by bit. Run it after *every*
   change and watch what happens.

### JavaScript (no install)

Just double-click `javascript/starter.html` — it opens in your browser. After
each edit, save the file and refresh the page.

> **Brand new to code?** Open `javascript/primer.html` first. It's a short tour
> of the handful of JavaScript ideas the game uses (variables, arrays, loops,
> functions…), each one printed onto the page so you can see it work.

### Python (one-time setup)

In a terminal, from inside the `python/` folder:

```bash
cd python
python3 -m venv venv                     # make a private setup for this project
venv/bin/pip install -r requirements.txt # install pygame into it
venv/bin/python primer.py                # warm-up: the Python building blocks
venv/bin/python starter.py               # then start building the game
```

After that first setup, you only need the last line to play.

> **Brand new to code?** Run `primer.py` first. It's a short, no-game tour of the
> handful of Python ideas the game uses (variables, lists, loops, functions…),
> each one printed to the screen so you can see it work.

---

## 💾 Saving your progress with Git

Git lets you save snapshots of your work so you never lose it and can see how
far you've come. After you finish a stage (or any time, really):

```bash
git add .
git commit -m "Finished Stage 2 — the dot moves!"
```

To send your saved progress up to GitHub (once a remote is set up):

```bash
git push
```

> Tip: commit often, with a short message about what you just got working.
> Each commit is a checkpoint you can always come back to.

---

## 🌟 Where to go next

Once the game works, make it *yours* — faster bullets, tougher enemies, new
colors, a high score. Ideas are listed at the end of each curriculum PDF.

The goal isn't to finish the game. It's to discover that **you can make the
computer do what you want.** Have fun! 💜
