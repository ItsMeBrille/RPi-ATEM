// JavaScript

const canvas = document.getElementById("sceneimage");
const context = canvas.getContext("2d");

const height = 420;
const width = 640; // window.innerWidth

// resize canvas (CSS does scale it up or down)
context.canvas.width = window.innerWidth;
context.canvas.height = window.innerWidth * 0.65625;

context.strokeStyle = "red";
context.lineWidth = 5;


function getMousePos(canvas, evt) {
  var rect = canvas.getBoundingClientRect(),
    scaleX = canvas.width / rect.width,
    scaleY = canvas.height / rect.height;

  return {
    x: (evt.clientX - rect.left) * scaleX, y: (evt.clientY - rect.top) * scaleY,
  };
}


let start = {};
let rectangles = [];

function startRect(e){
    start = getMousePos(canvas, e);
}
window.addEventListener("mousedown", startRect);

function endRect(e){
    let { x, y } = getMousePos(canvas, e);

    rectangle = {
        "coordinates" : {
            "x1" : start.x,
            "y1" : start.y,
            "x2" : x - start.x,
            "y2" : y - start.y
        }
    }

    rectangles.push(rectangle);
    context.strokeRect(rectangle.coordinates.x1, rectangle.coordinates.y1, rectangle.coordinates.x2, rectangle.coordinates.y2);
}

window.addEventListener("mouseup", endRect);

function updateCanvas(){
    var img = new Image;
    img.src = "static/img/scene.jpg";
    img.onload = function() {
        context.drawImage(img, 0, 0, 680, 680 * img.height / img.width)
    }
    
    rectangles.forEach(rectangle => {
        context.strokeRect(rectangle.coordinates.x1, rectangle.coordinates.y1, rectangle.coordinates.x2, rectangle.coordinates.y2);
    });
    
}

updateCanvas();