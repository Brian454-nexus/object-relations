# Script to run example queries

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

if __name__ == "__main__":
    # Example: List all articles by author 'Alice'
    alice = Author.find_by_name("Alice")
    if alice:
        print(f"Articles by {alice.name}:")
        for article in alice.articles:
            print(f"- {article.title}")

    # Example: List all magazines Alice contributed to
    if alice:
        print(f"Magazines {alice.name} contributed to:")
        for mag in alice.magazines:
            print(f"- {mag.name} ({mag.category})")

    # Example: List all contributors to 'Tech Today'
    tech_today = Magazine.find_by_name("Tech Today")
    if tech_today:
        print(f"Contributors to {tech_today.name}:")
        for author in tech_today.contributors:
            print(f"- {author.name}")

    # Example: List all article titles in 'Tech Today'
    if tech_today:
        print(f"Articles in {tech_today.name}:")
        for title in tech_today.article_titles:
            print(f"- {title}")
