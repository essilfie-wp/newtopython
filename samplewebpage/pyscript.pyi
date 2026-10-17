"""
Type stub file for PyScript in-browser WebAssembly runtime.
Provides type definitions for the IDE language server so it doesn't show
'Cannot find module pyscript' warnings when editing.
"""

from typing import Any, Callable

def when(event_type: str, selector: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...

document: Any
window: Any
display: Any
HTML: Any
