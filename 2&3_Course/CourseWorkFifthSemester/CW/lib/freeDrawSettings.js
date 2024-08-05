//Define action to pen draw by mouse action
(function () {
    'use strict';
    var freeDrawSettings = function () {
      let width = 1;
      let color = 'black';
      const _self = this;
      $(`${this.containerSelector} .main-panel`).append(`<div class="toolpanel" id="draw-panel"><div class="content"><p class="title">Free Draw</p></div></div>`);
      // set dimension section
      $(`${this.containerSelector} .toolpanel#draw-panel .content`).append(`
        <div>
          <div class="input-container">
            <label>Brush Width</label>
            <div class="custom-number-input">
            <button class="decrease">-</button>
            <input type="number" min="1" value="1" id="input-brush-width"/>
            <button class="increase">+</button>
            </div>
          </div>
          <div class="input-container">
            <label>Brush Color</label>
            <input id="color-picker" value='black'/>
          </div>
        </div>
      `);
      let updateBrush = () => {
        try {
          _self.canvas.freeDrawingBrush = new fabric.PencilBrush(_self.canvas)
          _self.canvas.freeDrawingBrush.width = width;
          _self.canvas.freeDrawingBrush.color = color;
        } catch (_) {}
      }
      $(`${this.containerSelector} .toolpanel#draw-panel .content #input-brush-width`).change(function () {
        try {
          width = parseInt($(this).val());
          updateBrush();
        } catch (_) {}
      })
      $(`${this.containerSelector} .toolpanel#draw-panel .content #color-picker`).spectrum({
        type: "color",
        showInput: "true",
        showInitial: "true",
        allowEmpty: "false",
      });
      $(`${this.containerSelector} .toolpanel#draw-panel .content #color-picker`).change(function () {
        try {
          color = $(this).val();
          updateBrush();
        } catch (_) {}
      })
    }
    window.ImageEditor.prototype.initializeFreeDrawSettings = freeDrawSettings;
  })();