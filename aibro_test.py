"""
Aibro.ai Test Module

A simple module to demonstrate basic functionality for the Aibro.ai test.
"""


def greet(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet (default: "World")
        
    Returns:
        A greeting string
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def main():
    """Main entry point for the module."""
    print(greet())
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
