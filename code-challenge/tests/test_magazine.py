# Tests for Magazine class

import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_db():
    with open('code-challenge/lib/db/schema.sql') as f:
        schema_sql = f.read()
    conn = get_connection()
    conn.executescript(schema_sql)
    conn.commit()
    from lib.db.seed import seed
    seed()
    conn.close()

def test_magazine_save_and_find():
    mag = Magazine("Test Mag", "Test Cat")
    mag.save()
    found = Magazine.find_by_id(mag.id)
    assert found is not None
    assert found.name == "Test Mag"
    assert found.category == "Test Cat"

def test_magazine_articles():
    mag = Magazine.find_by_name("Tech Today")
    articles = mag.articles
    assert len(articles) >= 1
    assert all(a.magazine_id == mag.id for a in articles)

def test_magazine_contributors():
    mag = Magazine.find_by_name("Tech Today")
    contributors = mag.contributors
    assert any(a.name == "Alice" for a in contributors)

def test_magazine_article_titles():
    mag = Magazine.find_by_name("Tech Today")
    titles = mag.article_titles
    assert "AI Revolution" in titles

def test_magazine_not_found():
    assert Magazine.find_by_id(9999) is None
    assert Magazine.find_by_name("Nonexistent") is None
    assert Magazine.find_by_category("Nonexistent") == []

def test_magazine_no_articles():
    mag = Magazine("No Articles Mag", "NoCat")
    mag.save()
    assert mag.articles == []

def test_magazine_no_contributors():
    mag = Magazine("No Contributors Mag", "NoCat")
    mag.save()
    assert mag.contributors == []

def test_magazine_article_titles_empty():
    mag = Magazine("No Titles Mag", "NoCat")
    mag.save()
    assert mag.article_titles == []

def test_magazine_contributing_authors_empty():
    mag = Magazine("No Contrib Auth", "NoCat")
    mag.save()
    assert mag.contributing_authors == []
