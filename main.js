const socket = io.connect('http://127.0.0.1:5000')

const btn = document.getElementById('send-msg')
const txt = document.getElementById('msg-text')

socket.on('connect', () => {
  socket.send('User connected')
})

btn.addEventListener('click', () => {
  const text = txt.value
  console.log(text)
})
socket.on('message', (msg) => {
  console.log(msg)
})
