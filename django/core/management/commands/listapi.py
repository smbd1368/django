# myapp/management/commands/listapi.py

from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'List all API endpoints in the project'

    def handle(self, *args, **kwargs):
        urls = get_resolver().url_patterns
        self.list_urls(urls)

    def list_urls(self, urls, prefix=''):
        for url in urls:
            if hasattr(url, 'url_patterns'):
                # If it's an include, recurse into it
                self.list_urls(url.url_patterns, prefix + str(url.pattern))
            else:
                # Print the URL pattern
                self.stdout.write(f'{prefix}{url.pattern} -> {url.callback.__name__ if url.callback else "No callback"}')
