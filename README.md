# Badges
[![Coverage Status](https://coveralls.io/repos/github/David-Duefrene/PieceView/badge.svg?branch=master)](https://coveralls.io/github/David-Duefrene/PieceView?branch=master)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gh/David-Duefrene/PieceView/?ref=repository-badge)

# PieceView
  A social media website revolving around pieces of information posted to views. Users will be able to follow other users as well as individual views.
  Users should be able to create a custom view and mark it either public or private to customize the viewing experience.

# Organization
  1. The account application primary purpose is to hold and manage all account related information including:
      * Authentication
      * User profile
      * follow relationships
  2. The Piece application purpose is to hold and manage the content a user posts. Type of contents are:
      * Blog-style, name is a WIP, likely to contain a mix of marked up text (HTML/CSS) as well as other types of "pieces" embedded
      * Strait picture/videos/gifs, will likely use a small "body" as a description along with title, for thing like movie/game trailers and
        to compete with quick reaction and meme content.
      * Code block with syntax highlighting, must be language selectable
      * Possible News piece that condenses the content by 90%+ and offers a "preview" for the article
