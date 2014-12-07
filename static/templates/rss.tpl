% from datetime import datetime
<?xml version="1.0" ?>
<rss version="2.0">
<channel>
  <description>{{tagline}}</description>
% for post in posts:
% newtime = datetime.strftime(datetime.strptime(post['date'], '%B %d, %Y'),'%a, %d %b %Y %H:%M:%S GMT')
  <item>
    <description>{{post['tagline']}}</description>
    <guid>http://{{url}}/{{uri.format(post['link'])}}</guid>
    <link>http://{{url}}/{{uri.format(post['link'])}}</link>
    <pubDate>{{newtime}}</pubDate>
    <title>{{post['title']}}</title>
  </item>
% end
  <link>http://{{url}}/</link>
  <title>{{blogtitle}}</title>
</channel>
</rss>
