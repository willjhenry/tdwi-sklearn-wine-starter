# TDWI Wine Classifier — Local Agent Lab (Lab 2)

This repository is the starter project for the **local agent** hands-on workshop segment. **Lab content lives in the Jupyter notebook:**

- [`LAB2-Local-Agent-Wine-Classifier.ipynb`](LAB2-Local-Agent-Wine-Classifier.ipynb)

### Lab map

| Step | You do | You learn |
|------|--------|-----------|
| **Setup** ([README](README.md)) | Fork, clone, `.venv`, test push | Your own GitHub repo for the exercise |
| **Lab 2** | Local Cursor agent builds a Wine classifier → `AGENTS.md` → `scripts/check.sh` → `/commit-code` | Recipe 1–3: deterministic gates, agent context, slash-command inner loop |

**Contrast with Lab 3:** Lab 3 uses **Cursor Cloud Agents** and GitHub PR Automations. Lab 2 stays **local**—same inner-loop ideas (`check.sh` + sub-agent review), wired through **`/commit-code`** instead of a Cloud Agent golden prompt.

**After the lab:** [WORKFLOW_RECIPES.md](WORKFLOW_RECIPES.md) — agent workflow framework and adoption path for later recipes.

---

Follow the steps below to fork, clone, and verify you can push to your own copy on GitHub.

---

## 1. Create a GitHub account if you don't have one

If you already have an account, skip to step 2.

1. Go to [GitHub](https://github.com) and create an account.

## 2. Authenticate your local Git to your GitHub account

1. You only need this step if you created a new account **or** if local Git is not authenticated to GitHub. If unsure, skip and return if Git prompts for a password in step 6.
2. Create a **classic** Personal Access Token with the **`repo`** scope:
   1. Sign in to [GitHub](https://github.com)
   2. Open your profile menu (top right) → **Settings**
   3. In the left sidebar, scroll to **Developer settings** → **Personal access tokens** → **Tokens (classic)**
   4. Click **Generate new token** → **Generate new token (classic)**
   5. Add a note (e.g. `TDWI workshop`), set an expiration if you like, and check the **`repo`** scope
   6. Click **Generate token**, then **copy the token immediately** (you will not see it again). Store it somewhere safe—you will use it as your password when Git prompts you over HTTPS

## 3. Fork the workshop repository

1. Go to the main workshop repo on GitHub:  
   **https://github.com/willjhenry/tdwi-sklearn-wine-starter** *(update when published)*
2. Click **Fork** → **Create a new fork**
3. Click **Create fork** in the lower right

## 4. Clone your fork in Cursor

1. Copy the HTTPS URL from **your** forked repo (**Code** → **HTTPS**, then copy the link)
2. In Cursor, open the Command Palette (**Cmd/Ctrl + Shift + P**) → type: **Git: Clone**
3. Paste the HTTPS URL and clone the repo
4. Select **Open** when asked if you would like to open the cloned repository
5. Select **Open Workspace** when the popup appears in the lower right

## 5. Set up the Python environment (`.venv`)

You need Python 3 installed locally. In Cursor, open a terminal (**Terminal** → **New Terminal**) with the project folder as the working directory, then run the commands for your OS.

**Mac**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows** (PowerShell or Command Prompt in the integrated terminal)

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If Windows reports that `python` is not found, try `py -m venv .venv` instead of `python -m venv .venv`.

**Both platforms — select the interpreter in Cursor**

1. Open the Command Palette (**Cmd/Ctrl + Shift + P**) → **Python: Select Interpreter**
2. Choose the interpreter labeled **`.venv`** (path should include `.venv` in this project)

When the venv is active, your terminal prompt usually shows `(.venv)`. You can confirm with `which python` (Mac) or `where python` (Windows)—the path should point inside `.venv`.

## 6. Make your first push

1. Create a test file, `test.txt`. In the file write:  
   `this is just a test file to test committing and pushing`
2. Commit the change in Cursor:
   1. Open the **Source Control** tab in the Primary Side Bar
   2. Press the **+** (plus) to the right of `test.txt` to stage the file
   3. Write a simple commit message in the **Message** input, e.g. `a test commit`
   4. Press the **Commit** button
   5. Press the **Synchronize Changes** button in the lower left corner
   6. If Git prompts for credentials: enter your **GitHub username** and, for the password, paste your **Personal Access Token** (created in step 2)—not your GitHub account password

---

After setup, open [`LAB2-Local-Agent-Wine-Classifier.ipynb`](LAB2-Local-Agent-Wine-Classifier.ipynb).
