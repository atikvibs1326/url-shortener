# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata



import threading
from datetime import datetime, timezone



lock = threading.Lock()


url_mapping = {}
click_counts = {}
created_at = {}


def add_url(short_code, original_url):
    with lock:
        if short_code in url_mapping:
            return False
        url_mapping[short_code] = original_url
        click_counts[short_code] = 0
        created_at[short_code] = datetime.now(timezone.utc).isoformat()
        return True



def get_url(short_code):
    return url_mapping.get(short_code)


def increment_click(short_code):
    with lock:
        if short_code in click_counts:
            click_counts[short_code] += 1


def get_stats(short_code):
    if short_code in url_mapping:
        return {
            "url": url_mapping[short_code],
            "clicks": click_counts.get(short_code, 0),
            "created_at": created_at.get(short_code)

        }
    return None
