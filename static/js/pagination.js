function process_followers(url, action){
  $.post(url, {
      page_limit: $('button.follower-page').attr('data-limit'),
      page_num: $('span.follower-current-page').text(),
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
      $('span.follower-current-page').text(data['new_page']);
    }
  )
}

function process_following(url, action){
  $.post(url, {
      page_limit: $('button.following-page').attr('data-limit'),
      page_num: $('span.following-current-page').text(),
      action: action
    },
    function(data){
      if (data['status'] != 'OK') {
        console.log(data);
      }
      for (var i = 0; i < data['followers'].length; i++) {
        $('#Following'+[i]+' img.card-img-top').attr("src",
          data['following'][i]['photo']);
        $('#Following'+[i]+' div.card-footer a.stretched-link').attr("href",
          data['following'][i]['url']);
        $('#Following'+[i]+' .card-body .card-title').text(
          data['following'][i]['name']);
      }
      $('span.following-current-page').text(data['new_page']);
    }
  )
}

function paginateFollowers(url) {
  $('button.followers').click(function(e){
    e.preventDefault();
    process_followers(url, $(this).data('action'))

  })
}

function paginateFollowing(url) {
  $('button.following').click(function(e){
    e.preventDefault();
    process_followers(url, $(this).data('action'))

  })
}
