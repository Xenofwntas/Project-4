document.addEventListener('DOMContentLoaded', function() {
    var elems = document.getElementsByClassName('postEdit');
    for (var i=0;i<elems.length;i+=1){
    elems[i].style.display = 'none';
    }
});

function editPost(post) {
    document.getElementById(`body${post}`).style.display = 'none';
    document.getElementById(`${post}`).style.display = 'block';
    document.getElementById(`editBtn${post}`).style.display = 'none';
}

function canselEdit(post) {
    document.getElementById(`${post}`).style.display = 'none';
    document.getElementById(`editBtn${post}`).style.display = 'block';
    document.getElementById(`input${post}`).value = document.getElementById(`body${post}`).innerHTML
    document.getElementById(`body${post}`).style.display = 'block';
}

function likePost(post) {
    
    fetch(`/like/${post}`,{
        method: 'PUT'
    })
    .then(res => res.json())
    .then(res => {
    console.log(res);
    
      if (res.like) {
        document.getElementById(`likeBtn${post}`).innerHTML = `<b style="color: rgb(229, 255, 0);">Liked</b> <small style="font-size: 11px;">${res.likeNum}</small>`;
      }
      else {
          if (res.likeNum > 0){
        document.getElementById(`likeBtn${post}`).innerHTML = `<b>Like</b> <small style="font-size: 11px;">${res.likeNum}</small>`;
          }
          else{
            document.getElementById(`likeBtn${post}`).innerHTML = '<b>Like</b>';
          }     }
});
event.preventDefault();}

function saveEdit(post) {
    const body = document.getElementById(`input${post}`).value;
    fetch(`/edit/${post}`, {
        method: 'PUT',
        body: JSON.stringify({
          body: body,
          id: post
        })
      })
      .then(res => res.json())
      .then(data => {
        console.log(data);
      });
      
      document.getElementById(`body${post}`).innerHTML = body;
      document.getElementById(`${post}`).style.display = 'none';
      document.getElementById(`editBtn${post}`).style.display = 'block';
      document.getElementById(`body${post}`).style.display = 'block';
      event.preventDefault();
}