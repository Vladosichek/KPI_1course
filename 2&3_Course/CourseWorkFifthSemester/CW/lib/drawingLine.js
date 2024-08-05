//Define action to draw line by mouse actions
(function () {
  'use strict';
  var lineDrawing = function (fabricCanvas) {
    let color = '#000000';
    let width = 5;
    let isDrawingLine = false,
      lineToDraw, pointer, pointerPoints
    fabricCanvas.on('mouse:down', (o) => {
      if (!fabricCanvas.isDrawingLineMode) return
      isDrawingLine = true
      pointer = fabricCanvas.getPointer(o.e)
      pointerPoints = [pointer.x, pointer.y, pointer.x, pointer.y]
      lineToDraw = new fabric.Line(pointerPoints, {
        strokeWidth: width,
        stroke: color
      });
      lineToDraw.selectable = false
      lineToDraw.evented = false
      lineToDraw.strokeUniform = true
      fabricCanvas.add(lineToDraw)
    });
    fabricCanvas.on('mouse:move', (o) => {
      if (!isDrawingLine) return
      pointer = fabricCanvas.getPointer(o.e)
      lineToDraw.set({
          x2: pointer.x,
          y2: pointer.y
        })
      fabricCanvas.renderAll()
    });
    fabricCanvas.on('mouse:up', () => {
      if (!isDrawingLine) return
      lineToDraw.setCoords()
      isDrawingLine = false
      fabricCanvas.trigger('object:modified')
    });
  }
  window.ImageEditor.prototype.initializeLineDrawing = lineDrawing;
})()