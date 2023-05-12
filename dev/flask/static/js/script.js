// JavaScript

const canvas = document.getElementById("sceneimage");
const context = canvas.getContext("2d");

/*
const height = 420;
const width = 640;
*/


const width = canvas.parentElement.clientWidth;
const height =  width * 0.65625;


// resize canvas (CSS does scale it up or down)
context.canvas.width = width;
context.canvas.height = height;


context.strokeStyle = "red";
context.lineWidth = 5;



function getRandomColor(){
    return `hsl(${Math.random()*360},90%,50%)`;
  }


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
        "ax" : start.x / width,
        "ay" : start.y / height,
        "bx" : x / width,
        "by" : y / height,
        "color" : getRandomColor()
    }

    if(rectangle.ax>1 || rectangle.ax<0 || rectangle.ay>1 || rectangle.ay<0 || rectangle.bx>1 || rectangle.bx<0 || rectangle.by>1|| rectangle.by<0){return;}

    rectangles.push(rectangle);
    console.log(rectangle);
    
    context.strokeStyle = rectangle.color;
    context.strokeRect(rectangle.ax * width, rectangle.ay * height, (rectangle.bx-rectangle.ax) * width, (rectangle.by-rectangle.ay) * height);
}
window.addEventListener("mouseup", endRect);


function updateCanvas(){
    var img = new Image;
    img.src = "static/img/scene.jpg";
    img.onload = function() {
        context.drawImage(img, 0, 0, width, width * img.height / img.width)
    }
    
    rectangles.forEach(rectangle => {
        context.strokeStyle = rectangle.color;
        context.strokeRect(rectangle.ax * width, rectangle.ay * height, (rectangle.bx-rectangle.ax) * width, (rectangle.by-rectangle.ay) * height);
    });
    
}

document.addEventListener("DOMContentLoaded", function(){
    updateCanvas();
});
