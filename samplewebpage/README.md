# 🐍 PyFlow Studio — Python Web Application

A modern, responsive, interactive Python web application powered by **Python WebAssembly (PyScript / MicroPython)** and designed for 1-click deployment to **Netlify**.

---

## 🌟 Key Features

1. **🔤 Python String & Text Lab**
   - Real-time length (`len()`), word count (`split()`), vowels, consonants, digits, and spaces.
   - Live Python membership test (`"query" in text`) with match counters.
   - Python string slicing visualizer (`text[start:end:step]`) with dual positive & negative index chips.
   - Built-in Python transformations: `.upper()`, `.lower()`, `.title()`, `.swapcase()`, `[::-1]` (reverse), and `snake_case`.

2. **⚡ Live Python Code Runner (REPL)**
   - Run real Python code directly inside your browser.
   - Captures standard output (`sys.stdout`) with execution timer (`⚡ 0.02s`).
   - Pre-loaded templates for `strings.py`, data types, Fibonacci generation, and word frequency tables.
   - Keyboard shortcut: **Ctrl + Enter** to execute code.

3. **🔢 Types & Numbers Inspector**
   - Live type evaluation (`type(x)`), dynamic type casting (`int()`, `float()`, `str()`, `bool()`).
   - Integer base representations in Decimal, Binary (`bin()`), Hexadecimal (`hex()`), and Octal (`oct()`).
   - Interactive Python truthiness reference table.

---

## 🚀 How to Host on Netlify (3 Simple Methods)

### Method 1: Netlify Drop (Fastest — 10 Seconds, No Git Required)
1. Open [app.netlify.com/drop](https://app.netlify.com/drop) in your web browser.
2. Sign in to your Netlify account (free).
3. Drag and drop this folder (`d:\GIT\newtopython`) directly into the upload area on the Netlify screen.
4. Netlify will deploy it instantly and provide you with a live URL (e.g. `https://your-site-name.netlify.app`)!

---

### Method 2: Automatic Continuous Deployment with GitHub (Recommended)
1. Commit and push this directory to your GitHub repository:
   ```bash
   git add .
   git commit -m "Add PyFlow Studio webapp"
   git push origin main
   ```
2. Go to your [Netlify Dashboard](https://app.netlify.com/) and click **"Add new site"** &rarr; **"Import an existing project"**.
3. Choose **GitHub** and select your repository.
4. Configure site settings:
   - **Build command:** *(leave empty)*
   - **Publish directory:** `.` *(root)*
5. Click **"Deploy Site"**. Every time you push changes to GitHub, Netlify automatically redeploys your web application!

---

### Method 3: Netlify CLI
If you have Node.js installed, you can deploy from PowerShell with one command:
```powershell
npx netlify deploy --prod --dir=.
```

---

## 💻 Local Testing

To preview and test the application on your computer:

```powershell
py server.py
```

Then open your browser to:
[http://localhost:8080](http://localhost:8080)

---

## 📁 Project Architecture

- **`index.html`**: Semantic HTML5 markup, PyScript 2024 runtime loader, and UI layout.
- **`style.css`**: Modern dark-mode styling with glassmorphism, glowing badges, and responsive layouts.
- **`app.py`**: Python engine running via WebAssembly in the browser (`@when` event decorators, string metrics, slicing math, and REPL execution).
- **`ui.js`**: Lightweight UI script for tab navigation, clipboard utilities, and code presets.
- **`netlify.toml`**: Netlify deployment configuration with optimized HTTP headers and WebAssembly caching.
- **`server.py`**: Local Python HTTP server with CORS headers for development.
