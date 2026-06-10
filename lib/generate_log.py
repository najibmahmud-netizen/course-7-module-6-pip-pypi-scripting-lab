from datetime import datetime
import requests

def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(entry + "\n")

    print(f"Log written to {filename}")

    return filename

def fetch_data():
    """Fetch data from a public API and return the response."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # Fetch data from API
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print("Fetched Post Title:", post_title)
    
    # Create log with sample data including API result
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"API Post Title: {post_title}"
    ]
    generate_log(log_data)