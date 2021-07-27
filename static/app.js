let interval;
function callback() {
  fetch('/api', { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      document.getElementById("dragon").innerHTML = data;
      console.log(data);
    })
    .catch((e) => { clearInterval(interval) })
}

function jog(axis, distance) {
  fetch(`/jog?axis=${axis}&distance=${distance}`, { method: 'GET' })
    .then(response => response.json())
}

function home(axis) {
  fetch(`/home?axis=${axis}`, { method: 'GET' })
    .then(response => response.json())
}

interval = setInterval(callback, 50)

