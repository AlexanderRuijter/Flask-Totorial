var canvas = document.getElementById("game")
var context = canvas.getContext("2d")
var playerX = 0
var playerY = 0
var playerSize = 50
function init() {
  update()
  loop()
}
function update() {
  
}
function loop() {

}
function render() {
  context.fillRect(0,0,50,50)
}
window.setInterval(loop1000/60)