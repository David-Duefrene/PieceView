function followButton(url){
  $('button.follow').click(function(e){
    e.preventDefault();
    $.post(url,
      {
        id: $(this).data('id'),
        action: $(this).data('action')
      },
      function(data){
        if (data['status'] == 'follow') {
          // toggle data-action
          $('button.follow').data('action', 'unfollow');

          // toggle link text
          $('button.follow').text('Unfollow');

          // update total followers
          var previous_followers = parseInt(
            $('span.count .total').text());
          $('span.count .total').text(previous_followers + 1);
        }
        else if (data['status'] == 'unfollow') {
          // toggle data-action
          $('button.follow').data('action', 'follow');

          // toggle link text
          $('button.follow').text('Follow');

          // update total followers
          var previous_followers = parseInt(
            $('span.count .total').text());
          $('span.count .total').text(previous_followers - 1);
        }
      }
    );
  });}
