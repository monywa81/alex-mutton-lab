import requests

def fetch_github_user_data(username):
    """
    Fetches user data from GitHub API and displays it in a user-friendly format.

    :param username: GitHub username to query.
    """
    url = f"https://api.github.com/users/{username}"

    try:
        # Make the API request
        response = requests.get(url)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        if not data:
            print("No data found")
            return

        # Display user data in a user-friendly format
        print(f"User: {data.get('login', 'N/A')}")
        print(f"ID: {data.get('id', 'N/A')}")
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Company: {data.get('company', 'N/A')}")
        print(f"Blog: {data.get('blog', 'N/A')}")
        print(f"Location: {data.get('location', 'N/A')}")
        print(f"Public Repos: {data.get('public_repos', 'N/A')}")
        print(f"Followers: {data.get('followers', 'N/A')}")
        print(f"Following: {data.get('following', 'N/A')}")
        print(f"Profile URL: {data.get('html_url', 'N/A')}")

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    fetch_github_user_data('microsoft')