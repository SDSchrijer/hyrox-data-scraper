import requests

def fetch_html(url: str):
    """
    Fetch the HTML content of a given URL.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The raw HTML content of the webpage.

    Raises:
        Exception: If the HTTP request fails or the response status code is not 200 (OK).
    """
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the response status code indicates success (HTTP 200 OK)
    if response.status_code == 200:
        # If successful, return the raw HTML content of the response
        return response.text
    else:
        # If not successful, raise an exception with the status code and URL
        raise Exception(f"Failed to fetch {url}, status code: {response.status_code}")
