/**
 * UI Helper script for PyFlow Studio
 * Handles navigation tabs, preset selections, clipboard helpers, and fast feedback.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Navigation Tab Switching
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTabId = btn.getAttribute('data-tab');

            tabButtons.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(pane => pane.classList.remove('active'));

            btn.classList.add('active');
            const targetPane = document.getElementById(targetTabId);
            if (targetPane) {
                targetPane.classList.add('active');
            }
        });
    });

    // Deploy Guide Button in Header switches to Netlify tab
    const deployGuideBtn = document.getElementById('btn-deploy-guide');
    if (deployGuideBtn) {
        deployGuideBtn.addEventListener('click', () => {
            const netlifyTabBtn = document.getElementById('nav-netlify-tab');
            if (netlifyTabBtn) {
                netlifyTabBtn.click();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        });
    }

    // 2. Text Input Preset Buttons
    const textPresets = document.querySelectorAll('.btn-text-preset');
    const strInput = document.getElementById('str-input');
    textPresets.forEach(btn => {
        btn.addEventListener('click', () => {
            const text = btn.getAttribute('data-text');
            if (strInput && text) {
                strInput.value = text;
                // Dispatch input event so Python picks it up
                strInput.dispatchEvent(new Event('input', { bubbles: true }));
            }
        });
    });

    // 3. Code Presets
    const codeSelect = document.getElementById('code-preset-select');
    const codeTextarea = document.getElementById('python-code-input');

    const PRESETS = {
        strings: `# Python String Iteration, Search & Slicing
text = "The best things in life are free and Python makes them simple!"

print(f"Original Text: {text}")
print(f"Length: {len(text)}")
print(f"Check 'free' in text: {'free' in text}")
print(f"Check 'expensive' in text: {'expensive' in text}")

print("\\nIterating over first word:")
for letter in text.split()[0]:
    print(f"  Character: {letter}")

print("\\nSlicing Demos:")
print(f"  First 8 chars: '{text[:8]}'")
print(f"  Last 7 chars:  '{text[-7:]}'")
print(f"  Every 4th char: '{text[::4]}'")
`,
        datatypes: `# Python Data Types & Type Casting
val_int = 42
val_float = 3.14159
val_str = "100"
val_bool = True

print(f"val_int: {val_int} | Type: {type(val_int)}")
print(f"val_float: {val_float} | Type: {type(val_float)}")
print(f"val_str: '{val_str}' | Type: {type(val_str)}")

# Type Conversions
converted_int = int(val_str)
print(f"\\nCasting str to int: {converted_int} + 50 = {converted_int + 50}")
print(f"Float to int: int({val_float}) = {int(val_float)}")
print(f"Int to float: float({val_int}) = {float(val_int)}")

# Truthiness
empty_list = []
print(f"\\nTruthiness of empty list: bool([]) = {bool(empty_list)}")
print(f"Truthiness of non-empty str: bool('Python') = {bool('Python')}")
`,
        fibonacci: `# Fibonacci Generator & Math Functions
import math

def generate_fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

count = 10
fib = generate_fibonacci(count)
print(f"First {count} Fibonacci numbers:")
print(fib)

# Math functions
numbers = [4, 9, 16, 25, 36, 49]
print("\\nSquare Roots:")
for num in numbers:
    print(f"  sqrt({num}) = {math.isqrt(num)}")
`,
        wordcounter: `# Word Frequency Counter
sample_story = """
Python is versatile. Python is elegant.
Learning Python is fun and practical for everyday automation.
"""

words = sample_story.lower().replace(".", "").split()
frequency = {}

for w in words:
    frequency[w] = frequency.get(w, 0) + 1

print(f"Total words: {len(words)}")
print("\\nWord Frequency Table:")
for word, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
    print(f"  {word.ljust(12)} : {count} times")
`
    };

    if (codeSelect && codeTextarea) {
        codeSelect.addEventListener('change', (e) => {
            const key = e.target.value;
            if (PRESETS[key]) {
                codeTextarea.value = PRESETS[key];
            }
        });
    }

    // Clear code button
    const clearCodeBtn = document.getElementById('btn-clear-code');
    if (clearCodeBtn && codeTextarea) {
        clearCodeBtn.addEventListener('click', () => {
            codeTextarea.value = '';
            codeTextarea.focus();
        });
    }

    // Clear terminal button
    const clearTerminalBtn = document.getElementById('btn-clear-terminal');
    const terminalOutput = document.getElementById('terminal-output');
    if (clearTerminalBtn && terminalOutput) {
        clearTerminalBtn.addEventListener('click', () => {
            terminalOutput.textContent = 'Terminal cleared.';
            terminalOutput.classList.remove('error');
        });
    }

    // Copy Buttons (Generic)
    document.querySelectorAll('.btn-copy-code').forEach(btn => {
        btn.addEventListener('click', () => {
            const textToCopy = btn.getAttribute('data-copy');
            if (textToCopy) {
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const original = btn.textContent;
                    btn.textContent = 'Copied! ✓';
                    setTimeout(() => { btn.textContent = original; }, 1800);
                });
            }
        });
    });

    // Copy transform output
    const copyTransformBtn = document.getElementById('btn-copy-transform');
    const transformOutput = document.getElementById('transform-output');
    if (copyTransformBtn && transformOutput) {
        copyTransformBtn.addEventListener('click', () => {
            navigator.clipboard.writeText(transformOutput.textContent).then(() => {
                const original = copyTransformBtn.textContent;
                copyTransformBtn.textContent = 'Copied! ✓';
                setTimeout(() => { copyTransformBtn.textContent = original; }, 1800);
            });
        });
    }

    // Keyboard shortcut: Ctrl+Enter (or Cmd+Enter) to run code
    if (codeTextarea) {
        codeTextarea.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                e.preventDefault();
                const runBtn = document.getElementById('btn-run-code');
                if (runBtn) runBtn.click();
            }
        });
    }
});
