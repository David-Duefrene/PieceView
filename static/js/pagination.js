function process_data(url, action){
  $.post(url, {
      page_limit: $('button.centered-link').attr('data-limit'),
      page_num: $('span.current-page').text(),
      action: action
    },
    function(data){
      if (data['status'] != 'OK') {
        console.log(data);
      }
      for (var i = 0; i < data['followers'].length; i++) {
        $('#Follower'+[i]+' img.card-img-top').attr("src",
          data['followers'][i]['photo']);
        $('#Follower'+[i]+' div.card-footer a.stretched-link').attr("href",
          data['followers'][i]['url']);
        $('#Follower'+[i]+' .card-body .card-title').text(
          data['followers'][i]['name']);
      }
      $('span.current-page').text(data['new_page']);
    }
  )
}

function paginateUsers(url) {
  $('button.page-link').click(function(e){
    e.preventDefault();
    process_data(url, $(this).data('action'))

  })
}
