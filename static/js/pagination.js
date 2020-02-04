function paginateUsers(url) {
  $('a.page-link').click(function(e){
    e.preventDefault();
    $.post(url, {
        page_limit: 3,
        page_num: $('span.current-page').text()
      },
      function(data){
        for (var i = 0; i < data['followers'].length; i++) {
          $('#Follower'+[i]+' img.card-img-top').attr("src",
            data['followers'][i]['photo']);
          $('#Follower'+[i]+' div.card-footer a.stretched-link').attr("href",
            data['followers'][i]['url']);
          $('#Follower'+[i]+' .card-body .card-title').text(
            data['followers'][i]['name']);
        }
      }
    )
  })
}
