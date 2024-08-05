//Define action to add shape to canvas
(function () {
    'use strict';
    const defaultShapes = [
      `<svg viewBox="-10 -10 120 120"><polygon points="0 0, 0 100, 100 100, 100 0" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="-8 -8 120 120"><polygon fill="none" stroke-width="5" stroke="black" points="50 0, 85 50, 50 100, 15 50"></polygon></svg>`,
      `<svg viewBox="-10 -10 120 120"><polygon points="25 0, 0 100, 75 100, 100 0" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="-8 -8 120 120"><polygon points="0,100 30,10 70,10 100,100" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="-10 -10 120 120"><path d="M 80,80 V 20 H 20 v 60 z m 20,20 V 0 H 0 v 100 z" stroke-width="5" stroke="#000" fill-rule="evenodd" fill="none"></path></svg>`,
      `<svg viewBox="0 0 100 100"><polygon points="26,86 11.2,40.4 50,12.2 88.8,40.4 74,86 " stroke="#000" stroke-width="5" fill="none"></polygon></svg>`,
      `<svg viewBox="0 0 100 100"><polygon points="30.1,84.5 10.2,50 30.1,15.5 69.9,15.5 89.8,50 69.9,84.5" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="0 0 100 100"><polygon points="34.2,87.4 12.3,65.5 12.3,34.5 34.2,12.6 65.2,12.6 87.1,34.5 87.1,65.5 65.2,87.4" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="0 0 100 100"><polygon points="11.2,70 11.2,40 50,12.2 88.8,40 88.8,70" stroke="#000" stroke-width="5" fill="none"></polygon></svg>`,
      `<svg viewBox="0 0 100 100"><polygon points="10.2,70 10.2,35 30.1,15 69.9,15 89.8,35 89.8,70" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="-10 -10 120 120"><polygon points="50 15, 100 100, 0 100" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="-10 -10 120 120"><polygon points="0 0, 100 100, 0 100" stroke-width="5" stroke="#000" fill="none"></polygon></svg>`,
      `<svg viewBox="-10 -10 120 120"><path d="M 26,85 50,45 74,85 Z m -26,15 50,-85 50,85 z" stroke-width="5" stroke="#000" fill="none"></path></svg>`,
      `<svg viewBox="8 50 100 100"><path d="M 62.68234,131.5107 H 26.75771 V 96.075507 Z M 11.572401,146.76255 V 59.66782 l 87.983665,87.09473 z" stroke-width="5" stroke="#000" fill="none" fill-rule="evenodd"></path></svg>`,
      `<svg viewBox="-2 -2 100 100"><circle cx="50" cy="50" r="40" stroke="#000" stroke-width="5" fill="none"></circle></svg>`,
      `<svg x="0px" y="0px" viewBox="0 0 96 120" xml:space="preserve"><path stroke="#000" stroke-width="5" fill="none" d="M9.113,65.022C11.683,45.575,28.302,30.978,48,30.978c19.696,0,36.316,14.598,38.887,34.045H9.113z"></path></svg>`,
      `<svg viewBox="-15 -15 152 136"><path stroke="#000000" stroke-width="5" d="m0 0l57.952755 0l0 0c32.006428 -1.4055393E-14 57.952755 23.203636 57.952755 51.82677c0 28.623135 -25.946327 51.82677 -57.952755 51.82677l-57.952755 0z" fill="none"></path></svg>`,
      `<svg viewBox="-5 -50 140 140"><path stroke="#000000" stroke-width="5" d="m20.013628 0l84.37401 0l0 0c11.053215 -1.04756605E-14 20.013626 9.282301 20.013626 20.7326c0 11.450296 -8.960411 20.7326 -20.013626 20.7326l-84.37401 0l0 0c-11.053222 0 -20.013628 -9.282303 -20.013628 -20.7326c-5.2380687E-15 -11.450298 8.960406 -20.7326 20.013628 -20.7326z" fill="none"></path></svg>`,
      `<svg viewBox="-8 -8 136 136"><path stroke="#000000" stroke-width="5" d="m0 51.82677l0 0c0 -28.623135 23.203636 -51.82677 51.82677 -51.82677l0 0c13.745312 0 26.927654 5.4603047 36.64706 15.17971c9.719406 9.719404 15.17971 22.901749 15.17971 36.64706l0 0c0 28.623135 -23.203636 51.82677 -51.82677 51.82677l0 0c-28.623135 0 -51.82677 -23.203636 -51.82677 -51.82677zm25.913385 0l0 0c0 14.311565 11.60182 25.913387 25.913385 25.913387c14.311565 0 25.913387 -11.601822 25.913387 -25.913387c0 -14.311565 -11.601822 -25.913385 -25.913387 -25.913385l0 0c-14.311565 0 -25.913385 11.60182 -25.913385 25.913385z" fill="none"></path></svg>`,
      `<svg viewBox="-7 -35 133 105"><path stroke="#000000" stroke-width="5" d="m0 57.952755l0 0c0 -32.006424 25.946333 -57.952755 57.952755 -57.952755c32.006428 0 57.952755 25.946333 57.952755 57.952755l-28.97638 0c0 -16.003212 -12.97316 -28.976377 -28.976376 -28.976377c-16.003212 0 -28.976377 12.9731655 -28.976377 28.976377z" fill="none"></path></svg>`
    ]
    var shapes = function () {
      const _self = this;
      let ShapeList = defaultShapes;
      if (Array.isArray(this.shapes) && this.shapes.length) ShapeList = this.shapes;
      $(`${this.containerSelector} .main-panel`).append(`<div class="toolpanel" id="shapes-panel"><div class="content"><p class="title">Shapes</p></div></div>`);
      ShapeList.forEach(svg => {
        $(`${this.containerSelector} .toolpanel#shapes-panel .content`).append(`<div class="button">${svg}</div>`)
      })
      $(`${this.containerSelector} .toolpanel#shapes-panel .content .button`).click(function () {
        let svg = $(this).html();
        try {
          fabric.loadSVGFromString(
            svg,
            (objects, options) => {
              var obj = fabric.util.groupSVGElements(objects, options)
              obj.strokeUniform = true
              obj.strokeLineJoin = 'miter'
              obj.scaleToWidth(100)
              obj.scaleToHeight(100)
              obj.set({
                left: 0,
                top: 0
              })
              _self.canvas.add(obj).renderAll()
              _self.canvas.trigger('object:modified')
            }
          )
        } catch (_) {
          console.error("can't add shape");
        }
      })
    }
    window.ImageEditor.prototype.initializeShapes = shapes;
  })();