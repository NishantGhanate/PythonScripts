let canvas, ctx

// setup config variables and start the program
function init () {
  canvas = document.getElementById('gameCanvas')
  ctx = canvas.getContext('2d')
}

// wait for the HTML to load
document.addEventListener('DOMContentLoaded', init)
function init () {
    // set our config variables
    canvas = document.getElementById('gameCanvas')
    ctx = canvas.getContext('2d')
    createGrid();
  }

  // draws a grid
function createGrid () {
    // draw a line every *step* pixels
    const step = 25
    // our end points
    const width = canvas.width
    const height = canvas.height
    // set our styles
    ctx.save()
    ctx.strokeStyle = 'gray' // line colors
    ctx.fillStyle = 'black' // text color
    // draw vertical from X to Height
    for (let x = 0; x < width; x += step) {
    }
    // draw horizontal from Y to Width
    for (let y = 0; y < height; y += step) {
    }
    // restore the styles from before this function was called
    ctx.restore()
  }
  