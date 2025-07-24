

import pytest
from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.json["service"] == "URL Shortener API"


def test_shorten_and_redirect_and_stats(client):
    #shortening url
    url = "http://example.com/test"
    res = client.post('/api/shorten', json={"url": url})
    assert res.status_code == 201
    short_code = res.json["short_code"]
    short_url = res.json["short_url"]
    assert short_code
    assert short_url.endswith(short_code)

    # redirecting
    res = client.get(f'/{short_code}', follow_redirects=False)
    assert res.status_code == 302
    assert res.headers['Location'] == url

    #get statuss
    res = client.get(f'/api/stats/{short_code}')
    assert res.status_code == 200
    assert res.json["url"] == url
    assert res.json["clicks"] == 1
    assert "created_at" in res.json


def test_invalid_url(client):
    res = client.post('/api/shorten', json={"url": "ftp://invalid-url"})
    assert res.status_code == 400


def test_not_found(client):
    res = client.get('/nonexistent')
    assert res.status_code == 404
    res = client.get('/api/stats/nonexistent')
    assert res.status_code == 404


def test_missing_url_field(client):
    res = client.post('/api/shorten', json={})
    assert res.status_code == 400
