# TO DO LIST

### ITEMS

#### SETUP AND STRUCURE

* Create new feature branch: feature/add-score-system
* Update dev branch locally and ensure it’s synced with main
* Create data/highscores.json (empty structure)
* Create config/settings.json (empty structure)

#### GAMEPLAY FEATURES

##### Difficulty Scaling

* Add difficulty configuration to settings.json
* Add logic to scale:

  * number of attempts
  * word length ranges
  * penalty rules (optional)
* Update GuessGame() to load difficulty settings dynamically



##### Categories of Words

* Update words.json structure to include categories:

  * animals
  * food
  * countries
  * etc.
* Add category selection menu
* Add select\_category() function
* Update select\_word() to filter by category + difficulty



##### Score System

* Define scoring rules (e.g., attempts left, difficulty multiplier)
* Add calculate\_score() function
* Add score accumulation per round
* Display score at end of each round
* Add total score for session



##### High‑Score Persistence

* Create highscores.json structure:

{

&#x20; "scores": \[]

}

* Add load\_highscores() function
* Add save\_highscore(name, score) function
* Add sorting logic (top 10)
* Add “View High Scores” menu option



#### USER EXPERIENCE IMPROVEMENTS

##### Colourful Terminal Output

* Choose a library: colorama (recommended)
* Add colour constants (e.g., GREEN, RED, YELLOW)
* Colour‑code:

  * correct guesses
  * wrong guesses
  * warnings
  * menus
  * win/lose messages



##### Configuration File

* Add settings.json with:

  * default difficulty
  * default category
  * attempts per difficulty
  * colour mode on/off
* Add load\_config() function
* Add save\_config() function
* Add “Settings” menu option

#### 

#### LOGGING

* Import Python’s built‑in logging module
* Create logs/game.log
* Configure logging level (INFO/DEBUG)
* Log:

  * game start/end
  * selected difficulty
  * selected category
  * chosen word (DEBUG only)
  * user guesses
  * score events
  * errors/exceptions



#### DOCUMENTATION

* Update README with:

  * new features
  * scoring rules
  * categories
  * difficulty scaling
  * high‑score system
* Add documentation to docs/:

  * scoring design
  * config file structure
  * logging overview
* Add docstrings to all new functions



#### TESTING

##### Unit Tests

* Test difficulty scaling logic
* Test category selection
* Test score calculation
* Test high‑score saving/loading
* Test config loading/saving



##### Integration Tests

* Test full round with scoring
* Test high‑score persistence across sessions



#### FINAL TIER 2 POLISH

* Run full manual test of all new features
* Update README screenshots (new menus, colours)
* Merge feature/add-score-system → dev
* Merge dev → main
* Tag release: v2.0.0

