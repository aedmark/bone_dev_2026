"""
struts.py

The Structural Primitives Module.

This file provides the low-level struts that bind the deterministic execution layer
to the narrative and data layers.
"""

from typing import Any

from constants import Prisma

# LINGUISTIC & STRUCTURAL UTILITIES

def ux(section: str, key: str, default: Any = "") -> Any:
    """
    Retrieves localized, user-facing strings from the Lore cache.

    This function acts as the Lexical Firewall, ensuring that all narrative text is
    drawn from a centralized, easily modifiable manifest.

    Args:
        section (str): The specific narrative domain (e.g., 'warnings', 'greetings').
        key (str): The precise string identifier within that domain.
        default (Any): The fallback value if the key is missing.

    Returns:
        Any: The requested narrative string, or the default if the lookup fails.
    """
    from core import LoreManifest
    data = LoreManifest.get_instance().get("ux_strings", section)
    return data.get(key, default) if isinstance(data, dict) else default

def ux_format(section: str, key: str, default: str = "", **kwargs) -> str:
    """
    Retrieves and safely interpolates dynamic variables into a UX string.

    Prioritizes system resilience by gracefully degrading to the raw,
    unformatted string rather than triggering an apocalyptic stack trace for a typo.

    Args:
        section (str): The narrative domain.
        key (str): The string identifier.
        default (str): Fallback string.
        **kwargs: The dynamic variables to inject into the string template.

    Returns:
        str: The fully interpolated string, or the raw string if interpolation fails.
    """
    msg = ux(section, key, default) or default
    if not msg:
        return ""
    try:
        # Force string conversion to prevent AttributeError if the UX cache returns a list or dict.
        return str(msg).format(**kwargs)
    except (KeyError, ValueError, IndexError, AttributeError, TypeError) as e:
        # We log the grammatical failure so the developer can fix it without crashing the engine.
        print(f"{Prisma.GRY}[UX] Formatting mismatch ({e}) in {section}.{key}. Falling back to raw string.{Prisma.RST}")
        return str(msg)


def safe_get(obj: Any, key: str, default: Any = None) -> Any:
    """
    Agnostic retriever for nested data structures.
    Handles the routing automatically so the developer can just ask for the data.

    Args:
        obj (Any): The target object (can be a dict or a class instance).
        key (str): The property or key to retrieve.
        default (Any): What to return if the key/attribute does not exist.

    Returns:
        Any: The retrieved value, or the default.
    """
    if obj is None:
        return default
    if isinstance(obj, dict):
        val = obj.get(key, default)
    else:
        val = getattr(obj, key, default)
    return default if val is None else val


def safe_set(obj: Any, key: str, value: Any) -> None:
    """
    Agnostic setter for nested data structures, equipped with structural alarms.
    Acts as a systemic smoke detector, explicitly warning the developer
    that the architecture is rotting.

    Args:
        obj (Any): The target object to modify.
        key (str): The key or attribute name to set.
        value (Any): The new value to assign.
    """
    if obj is None:
        print(f"{Prisma.RED}[STRUCTURAL ROT] safe_set swallowed a write to '{key}'. Target object is None.{Prisma.RST}")
        return
    try:
        if isinstance(obj, dict):
            obj[key] = value
        else:
            setattr(obj, key, value)
    except (TypeError, AttributeError) as e:
        print(f"{Prisma.RED}[STRUCTURAL ROT] safe_set failed on '{key}'. Target is immutable or rejects assignment: {e}{Prisma.RST}")