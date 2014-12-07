<!DOCTYPE html>
<html>
	<head>
		<title>{{blogtitle}} || {{title}}</title>
		<link rel="stylesheet" href="global.css" media="all" />
		<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="feed.xml" />
	</head>
	<body>
		<header>
			<h1>{{blogtitle}}</h1>
		</header>

		<div id="sidelinks">
% for text, link in sidebar:
			<h3><a href="{{link}}" class="sidelink">{{text}}</a></h3>
% end
		</div>
		<div id="mainarea">
