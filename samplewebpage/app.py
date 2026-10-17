"""
PyFlow Studio — Core Python Engine
Runs directly in the browser via WebAssembly (PyScript / MicroPython)
Provides real-time string analysis, slicing visualizer, REPL runner, and type inspector.
"""

import sys
import io
import time
import math
# PyScript WebAssembly Runtime Imports
try:
    from pyscript import when, document, window  # type: ignore
except ImportError:
    # Graceful fallback for local desktop Python interpreter & IDE linting
    def when(event_type, selector):  # type: ignore
        def decorator(func):
            return func
        return decorator
    document = None  # type: ignore
    window = None  # type: ignore

# 1. Engine Initialization & Status
# ---------------------------------------------------------------------------
def init_engine():
    badge = document.getElementById("runtime-status")
    text = document.getElementById("runtime-text")
    if badge and text:
        badge.classList.remove("pulsing")
        badge.classList.add("ready")
        dot = badge.querySelector(".status-dot")
        if dot:
            dot.classList.remove("pulsing")
        text.innerText = "Python 3.12 Engine: Active ⚡"
    
    # Run initial analysis and base converter
    update_string_analysis()
    update_type_inspector()
    update_number_bases()
    print("Python runtime successfully initialized in browser.")


# ---------------------------------------------------------------------------
# 2. String & Text Analysis Lab
# ---------------------------------------------------------------------------
def get_input_text():
    elem = document.getElementById("str-input")
    return elem.value if elem else ""

def update_string_analysis(event=None):
    text = get_input_text()
    
    # Metrics
    length = len(text)
    words = len(text.split())
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())

    # Update Stats DOM
    set_text("stat-length", str(length))
    set_text("stat-words", str(words))
    set_text("stat-vowels", str(vowels))
    set_text("stat-consonants", str(consonants))
    set_text("stat-digits", str(digits))
    set_text("stat-spaces", str(spaces))

    # Update search and slice
    check_membership()
    apply_slice()

@when("input", "#str-input")
def on_str_input_change(event):
    update_string_analysis()


# ---------------------------------------------------------------------------
# 3. Substring & Membership Search ("query in text")
# ---------------------------------------------------------------------------
def check_membership(event=None):
    text = get_input_text()
    search_elem = document.getElementById("str-search")
    query = search_elem.value if search_elem else ""

    result_pill = document.getElementById("search-result-pill")
    bool_elem = document.getElementById("search-bool")
    count_elem = document.getElementById("search-count")

    if not query:
        if bool_elem: bool_elem.innerText = "—"
        if count_elem: count_elem.innerText = "(empty query)"
        if result_pill:
            result_pill.className = "result-pill"
        return

    is_present = query in text
    count = text.count(query)

    if bool_elem:
        bool_elem.innerText = str(is_present)
    if count_elem:
        match_str = "match" if count == 1 else "matches"
        count_elem.innerText = f"({count} {match_str})"

    if result_pill:
        result_pill.className = "result-pill true" if is_present else "result-pill false"

@when("input", "#str-search")
def on_search_input(event):
    check_membership()

@when("click", "#btn-search-check")
def on_search_btn_click(event):
    check_membership()


# ---------------------------------------------------------------------------
# 4. Slicing & Visual Character Tape (text[start:end:step])
# ---------------------------------------------------------------------------
def parse_int_or_default(elem_id, default):
    elem = document.getElementById(elem_id)
    if not elem or not elem.value.strip():
        return default
    try:
        return int(elem.value.strip())
    except Exception:
        return default

def apply_slice(event=None):
    text = get_input_text()
    n = len(text)

    start = parse_int_or_default("slice-start", 0)
    end = parse_int_or_default("slice-end", 15 if n >= 15 else n)
    step = parse_int_or_default("slice-step", 1)

    if step == 0:
        step = 1  # prevent ZeroDivisionError in slice

    # Update code header display
    set_text("slice-disp-start", str(start))
    set_text("slice-disp-end", str(end))
    set_text("slice-disp-step", str(step))

    # Slice calculation
    try:
        sliced_result = text[start:end:step]
    except Exception as e:
        sliced_result = f"Error: {e}"

    res_elem = document.getElementById("slice-result-text")
    if res_elem:
        res_elem.innerText = f'"{sliced_result}"' if sliced_result else '"" (empty string)'

    # Render Visual Tape
    render_character_tape(text, start, end, step)

def render_character_tape(text, start, end, step):
    tape = document.getElementById("char-tape")
    if not tape:
        return

    # Determine which indices are included in the slice
    try:
        s = slice(start, end, step)
        indices_in_slice = set(range(*s.indices(len(text))))
    except Exception:
        indices_in_slice = set()

    max_display = 40
    chars_to_show = text[:max_display]
    n = len(text)

    html_parts = []
    for i, char in enumerate(chars_to_show):
        in_slice_cls = " in-slice" if i in indices_in_slice else ""
        neg_idx = i - n
        char_display = "␣" if char == " " else char
        html_parts.append(
            f'<div class="tape-chip{in_slice_cls}">'
            f'<span class="tape-char">{char_display}</span>'
            f'<span class="tape-idx">{i}</span>'
            f'<span class="tape-neg">{neg_idx}</span>'
            f'</div>'
        )

    if n > max_display:
        html_parts.append(f'<div class="tape-chip"><span class="tape-char">...</span><span class="tape-idx">+{n - max_display}</span></div>')

    tape.innerHTML = "".join(html_parts)

@when("click", "#btn-apply-slice")
def on_apply_slice_click(event):
    apply_slice()

@when("click", "#btn-reset-slice")
def on_reset_slice_click(event):
    set_val("slice-start", "0")
    set_val("slice-end", "15")
    set_val("slice-step", "1")
    apply_slice()


# ---------------------------------------------------------------------------
# 5. String Transformations
# ---------------------------------------------------------------------------
def apply_transform(action):
    text = get_input_text()
    badge = document.getElementById("transform-type-badge")
    out = document.getElementById("transform-output")

    if not out:
        return

    if action == "upper":
        result = text.upper()
        label = ".upper()"
    elif action == "lower":
        result = text.lower()
        label = ".lower()"
    elif action == "title":
        result = text.title()
        label = ".title()"
    elif action == "swapcase":
        result = text.swapcase()
        label = ".swapcase()"
    elif action == "reverse":
        result = text[::-1]
        label = "[::-1] (Reversed)"
    elif action == "snake":
        clean_words = "".join(c if c.isalnum() or c.isspace() else " " for c in text).lower().split()
        result = "_".join(clean_words)
        label = "snake_case"
    else:
        result = text
        label = "Raw"

    if badge:
        badge.innerText = label
    out.innerText = result

@when("click", ".btn-transform")
def on_transform_btn_click(event):
    target = event.currentTarget
    action = target.getAttribute("data-action")
    if action:
        apply_transform(action)


# ---------------------------------------------------------------------------
# 6. Live Python Code Runner (REPL)
# ---------------------------------------------------------------------------
@when("click", "#btn-run-code")
def run_python_code(event):
    code_input = document.getElementById("python-code-input")
    terminal = document.getElementById("terminal-output")
    time_badge = document.getElementById("execution-time")

    if not code_input or not terminal:
        return

    code = code_input.value
    if not code.strip():
        terminal.innerText = "# No code entered to execute."
        terminal.className = "terminal-text"
        return

    output_chunks = []

    def custom_print(*args, **kwargs):
        sep = kwargs.get("sep", " ")
        end = kwargs.get("end", "\n")
        output_chunks.append(sep.join(str(a) for a in args) + end)

    user_globals = {
        "print": custom_print,
        "math": math,
        "time": time,
        "__name__": "__main__",
    }

    has_error = False
    start_time = time.time()
    old_stdout = None
    buffer = None

    if hasattr(sys, "stdout"):
        try:
            buffer = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = buffer
        except Exception:
            old_stdout = None

    try:
        exec(code, user_globals)
    except Exception as e:
        has_error = True
        output_chunks.append(f"\nTraceback (most recent call last):\n{type(e).__name__}: {e}\n")
    finally:
        if old_stdout is not None:
            try:
                if buffer:
                    captured = buffer.getvalue()
                    if captured:
                        output_chunks.append(captured)
                sys.stdout = old_stdout
            except Exception:
                pass

    elapsed = time.time() - start_time
    output = "".join(output_chunks)

    if not output.strip():
        output = "# Code executed successfully with no stdout output."

    terminal.innerText = output
    terminal.className = "terminal-text error" if has_error else "terminal-text"

    if time_badge:
        time_badge.innerText = f"⚡ {elapsed:.3f}s"


# ---------------------------------------------------------------------------
# 7. Types & Numbers Inspector
# ---------------------------------------------------------------------------
def update_type_inspector(event=None):
    elem = document.getElementById("type-input-val")
    val_raw = elem.value.strip() if elem else ""

    if not val_raw:
        return

    # Try evaluating as python literal
    try:
        val = eval(val_raw, {"__builtins__": {}})
    except Exception:
        val = val_raw  # fallback to string literal

    # Type name
    set_text("res-type-name", str(type(val)))

    # int cast
    try:
        set_text("res-int-cast", str(int(val)))
    except Exception as e:
        set_text("res-int-cast", f"TypeError: {e}")

    # float cast
    try:
        set_text("res-float-cast", str(float(val)))
    except Exception as e:
        set_text("res-float-cast", f"TypeError: {e}")

    # str cast
    set_text("res-str-cast", repr(str(val)))

    # bool cast
    bool_val = bool(val)
    bool_elem = document.getElementById("res-bool-cast")
    if bool_elem:
        bool_elem.innerText = str(bool_val)
        bool_elem.className = "type-val bool-true" if bool_val else "type-val bool-false"

@when("click", "#btn-inspect-type")
def on_inspect_type_click(event):
    update_type_inspector()

@when("input", "#type-input-val")
def on_type_input_change(event):
    update_type_inspector()


# ---------------------------------------------------------------------------
# 8. Number Base Representations
# ---------------------------------------------------------------------------
def update_number_bases(event=None):
    num_elem = document.getElementById("num-base-val")
    if not num_elem:
        return
    try:
        n = int(num_elem.value.strip() or 0)
        set_text("base-dec", str(n))
        set_text("base-bin", bin(n))
        set_text("base-hex", hex(n))
        set_text("base-oct", oct(n))
    except Exception:
        set_text("base-dec", "Invalid integer")

@when("input", "#num-base-val")
def on_num_base_input(event):
    update_number_bases()


# ---------------------------------------------------------------------------
# Helper DOM Utilities
# ---------------------------------------------------------------------------
def set_text(elem_id, text):
    el = document.getElementById(elem_id)
    if el:
        el.innerText = text

def set_val(elem_id, val):
    el = document.getElementById(elem_id)
    if el:
        el.value = val

# Boot up the application
init_engine()
