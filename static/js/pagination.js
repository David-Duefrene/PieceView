function paginateUsers(url) {
  $('button.paginate').click(function(e){
    e.preventDefault();
    $.post(url, {
        id: $(this).data('id'),
        page_limit: 3,
        page_num: 1
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
