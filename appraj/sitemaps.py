from django.contrib.sitemaps import Sitemap
from appraj.models import movielist
class movielistSitemap(Sitemap):
    changefreq="hourly"
    def items(self):
        return movielist.objects.all()