<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>the jazzybones blog</title>
    <link>https://jazzybones-www.github.io/blog/index.html</link>
    <atom:link href="https://jazzybones-www.github.io/blog/rss.xml" rel="self" />
    <description>the jazzybones blog</description>
    <language>en-us</language>
    <copyright>copyright 2024, jazzybones</copyright>
    <managingEditor>jazzybones@proton.me</managingEditor>
    <webMaster>jazzybones@proton.me</webMaster>
    <pubDate>
\$ date -R
    </pubDate>
    <generator>jazzybones custom software workers' cooperative</generator>
    <docs>https://www.rssboard.org/rss-specification</docs>
    <ttl>60</ttl>
    <image>
      <url>https://jazzybones-www.github.io/buttons/mine.png</url>
      <title>jazzybones 88x31 button</title>
      <link>https://jazzybones-www.github.io/blog/index.html</link>
    </image>
\$ ./blog/create-rss.sh
  </channel>
</rss>
\jb_dependencies: find blog -mindepth 2 -name '*.md'
