def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to my GitHub repository."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
