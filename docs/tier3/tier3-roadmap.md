# 🎨 Tier 3 Roadmap — GUI Version (Tkinter)

Tier 3 focuses on transforming the game from a console-based experience into a fully interactive graphical application using Tkinter.  
This roadmap outlines the structure, tasks, and milestones required to complete the GUI version while building on the existing Tier 2 architecture.

---

## 📁 SETUP & STRUCTURE

- Create new feature branch: `feature/gui-version`
- Create new folder structure:
```
gui/
└── components/
```
- Set up base Tkinter window (`main_window.py`)
- Define GUI architecture (screens, widgets, animations)
- Ensure gameplay logic from Tier 2 remains separate from GUI layer

---

## 🖥️ GUI SCREENS

### **Main Menu**
- Start Game button  
- Settings button  
- View High Scores button  
- Exit button  

### **Game Screen**
- Word display label  
- A–Z letter buttons  
- Attempts remaining indicator  
- Used letters display  
- Restart button  
- Exit to menu button  

### **Settings Screen**
- Difficulty dropdown  
- Category dropdown  
- Colour mode toggle  
- Logging level toggle  
- Save settings button  

### **High Scores Screen**
- Load and display scores from `highscores.json`
- Sorted list of top scores
- Back to menu button

---

## 🎮 GAMEPLAY INTEGRATION

- Connect GUI events to existing gameplay logic:
- `select_word()`
- `check_guess()`
- `calculate_score()`
- `load_config()`
- `save_highscore()`
- Replace console input with button interactions
- Update GUI display after each guess
- Trigger animations on:
- correct guess  
- wrong guess  
- win  
- lose  

---

## ✨ VISUAL FEEDBACK & ANIMATIONS

- Highlight correct letters  
- Shake animation for wrong guesses  
- Button colour transitions  
- Flash animation for win/lose  
- Smooth screen transitions  

---

## 🧩 USER EXPERIENCE IMPROVEMENTS

- Disable used letter buttons  
- Responsive layout for different window sizes  
- Light/dark colour themes  
- Error popups for invalid config or missing files  
- Clean navigation between screens  

---

## 📘 DOCUMENTATION

- Add Tier 3 section to `docs/index.md`
- Create:
- `docs/tier3/tier3-roadmap.md`
- `docs/tier3/future-improvements.md`
- Add GUI screenshots once implemented
- Update README with:
- GUI preview  
- New folder structure  
- Updated instructions  

---

## 🧪 TESTING

### **Unit Tests**
- Existing gameplay tests remain valid  
- Add tests for:
- config saving/loading via GUI  
- high-score persistence via GUI  

### **Manual GUI Testing**
- Test all screens  
- Test all buttons  
- Test animations  
- Test full gameplay loop  
- Test settings persistence  
- Test high-score updates  

---

## 🏁 FINAL TIER 3 POLISH

- Full manual GUI test pass  
- Add GUI screenshots to README  
- Update documentation  
- Merge `feature/gui-version` → `dev`  
- Merge `dev` → `main`  
- Tag release: `v3.0.0`

---

