% include('header.tpl', title="Archive")

<h2>ARCHIVE</h2>
% for post in posts:
  <p><a href="{{uri.format(post['link'])}}">{{post['title']}}</a>&nbsp;<span class="date">({{post['date']}})</span></p>
% end

% include('footer.tpl')
