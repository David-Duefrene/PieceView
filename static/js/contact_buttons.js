function followButton(url){
  $('button.follow').click(function(e){
    e.preventDefault();
    $.post(url,
      {
        id: $(this).data('id'),
        action: $(this).data('action')
      },
      function(data){
        if (data['status'] == 'follow' || data['status'] == 'unfollow') {
          status = (data['status'] == 'follow') ? 'unfollow' : 'follow';
          // toggle data-action
          $('button.follow').data('action', status);

          // toggle link text
          $('button.follow').text(status);

          // update total followers
          updated_count = (data['status'] == 'follow') ? 1 : -1;
          var previous_followers = parseInt($('span.count .total').text());
          $('span.count .total').text(previous_followers + updated_count);
        }
      }
    );
  });
}
