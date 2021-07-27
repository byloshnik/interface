function callback(){
  fetch('192.168.7.2:35', {method: 'POST'})
  .then(response => console.log(response))
}

let interval = setInterval(callback, 1000)