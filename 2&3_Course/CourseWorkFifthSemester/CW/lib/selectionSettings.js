//initialize selection setting panel
(function () {
  'use strict';
  const BorderStyleList = [{
    value: {
      strokeDashArray: [],
      strokeLineCap: 'butt'
    },
    label: "-"
  }, {
    value: {
      strokeDashArray: [1, 10],
      strokeLineCap: 'butt'
    },
    label: '|||'
  }, {
    value: {
      strokeDashArray: [1, 10],
      strokeLineCap: 'round'
    },
    label: '...'
  }, {
    value: {
      strokeDashArray: [15, 15],
      strokeLineCap: 'square'
    },
    label: '---(s)'
  }, {
    value: {
      strokeDashArray: [15, 15],
      strokeLineCap: 'round'
    },
    label: '---(r)'
  }, {
    value: {
      strokeDashArray: [25, 25],
      strokeLineCap: 'square'
    },
    label: '- -(s)',
  }, {
    value: {
      strokeDashArray: [25, 25],
      strokeLineCap: 'round'
    },
    label: '- -(r)',
  }, {
    value: {
      strokeDashArray: [1, 8, 16, 8, 1, 20],
      strokeLineCap: 'square'
    },
    label: '-. (s)',
  }, {
    value: {
      strokeDashArray: [1, 8, 16, 8, 1, 20],
      strokeLineCap: 'round'
    },
    label: '-. (r)',
  }]
  var selectionSettings = function () {
    const _self = this;
    $(`${this.containerSelector} .main-panel`).append(`<div class="toolpanel" id="select-panel"><div class="content"><p class="title">Selection Settings</p></div></div>`);
    // font section
    (() => {
      $(`${this.containerSelector} .toolpanel#select-panel .content`).append(`
        <div class="text-section">
          <h4>Style</h4>
          <div class="style">
            <button id="bold"><svg id="Capa_1" x="0px" y="0px" viewBox="-70 -70 450 450" xml:space="preserve"><path d="M218.133,144.853c20.587-14.4,35.2-37.653,35.2-59.52C253.333,37.227,216.107,0,168,0H34.667v298.667h150.187 c44.693,0,79.147-36.267,79.147-80.853C264,185.387,245.547,157.76,218.133,144.853z M98.667,53.333h64c17.707,0,32,14.293,32,32 s-14.293,32-32,32h-64V53.333z M173.333,245.333H98.667v-64h74.667c17.707,0,32,14.293,32,32S191.04,245.333,173.333,245.333z"></path></svg></button>
            <button id="italic"><svg id="Capa_1" x="0px" y="0px" viewBox="-70 -70 450 450" xml:space="preserve"><polygon points="106.667,0 106.667,64 153.92,64 80.747,234.667 21.333,234.667 21.333,298.667 192,298.667 192,234.667 144.747,234.667 217.92,64 277.333,64 277.333,0  "></polygon></svg></button>
            <button id="underline"><svg id="Capa_1" x="0px" y="0px" viewBox="-70 -70 450 450" xml:space="preserve"><path d="M192,298.667c70.72,0,128-57.28,128-128V0h-53.333v170.667c0,41.28-33.387,74.667-74.667,74.667 s-74.667-33.387-74.667-74.667V0H64v170.667C64,241.387,121.28,298.667,192,298.667z"></path><rect x="42.667" y="341.333" width="298.667" height="42.667"></rect></svg></button>
            <button id="linethrough"><svg id="Capa_1" x="0px" y="0px" viewBox="-70 -70 450 450" xml:space="preserve"><polygon points="149.333,160 234.667,160 234.667,96 341.333,96 341.333,32 42.667,32 42.667,96 149.333,96"></polygon><rect x="149.333" y="288" width="85.333" height="64"></rect><rect x="0" y="202.667" width="384" height="42.667"></rect></svg></button>
          </div>
          <div class="family">
            <div class="input-container">
            <label>Font</label>
            <select id="font-family">
              <option value=""></option>
              <option value="'Open Sans', sans-serif">Open Sans</option>
              <option value="'Oswald', sans-serif">Oswald</option>
              <option value="'Playfair Display', serif">Playfair Display</option>
              <option value="'Cormorant Garamond', serif">Cormorant Garamond</option>
              <option value="Impact, Charcoal, sans-serif">Impact</option>
              <option value="'Lucida Console', Monaco, monospace">Lucida Console</option>
              <option value="'Comic Sans MS', 'Comic Sans', cursive, sans-serif">Comic Sans</option>
              <option value="'Dancing Script', cursive">Dancing Script</option>
              <option value="'Indie Flower', cursive">Indie Flower</option>
              <option value="'Amatic SC', cursive">Amatic SC</option>
              <option value="'Permanent Marker', cursive">Permanent Marker</option>
            </select>
            </div>
          </div>
          <div class="sizes">
            <div class="input-container"><label>Font Size</label>
              <div class="custom-number-input">
              <button class="decrease">-</button>
              <input type="number" min="1" value="20" id="fontSize">
              <button class="increase">+</button>
              </div>
            </div>
            <div class="input-container"><label>Line Height</label>
              <div class="custom-number-input">
              <button class="decrease">-</button>
              <input type="number" min="0" max="3" value="1" step="0.1" id="lineHeight">
              <button class="increase">+</button>
              </div>
            </div>
            <div class="input-container"><label>Letter Spacing</label>
              <div class="custom-number-input">
              <button class="decrease">-</button>
              <input type="number" min="0" max="2000" step="100" value="0" id="charSpacing">
              <button class="increase">+</button>
              </div>
            </div>
            </p>
          </div>
          <div class="align">
            <div class="input-container">
            <label>Text Alignment</label>
            <select id="text-align">
              <option value="left">Left</option>
              <option value="center">Center</option>
              <option value="right">Right</option>
              <option value="justify">Justify</option>
            </select>
            </div>
          </div>
          <div class="color">
            <div class="input-container">
            <label>Text Color</label>
            <input id="color-picker" value="black">
            </div>
          </div>
          <hr>
        </div>
      `);
      $(`${this.containerSelector} .toolpanel#select-panel .style button`).click(function () {
        let type = $(this).attr('id');
        switch (type) {
          case 'bold':
            setActiveFontStyle(_self.activeSelection, 'fontWeight', getActiveFontStyle(_self.activeSelection, 'fontWeight') === 'bold' ? '' : 'bold')
            break;
          case 'italic':
            setActiveFontStyle(_self.activeSelection, 'fontStyle', getActiveFontStyle(_self.activeSelection, 'fontStyle') === 'italic' ? '' : 'italic')
            break;
          case 'underline':
            setActiveFontStyle(_self.activeSelection, 'underline', !getActiveFontStyle(_self.activeSelection, 'underline'))
            break;
          case 'linethrough':
            setActiveFontStyle(_self.activeSelection, 'linethrough', !getActiveFontStyle(_self.activeSelection, 'linethrough'))
            break;
          default:
            break;
        }
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified');
      })
      $(`${this.containerSelector} .toolpanel#select-panel .family #font-family`).change(function () {
        let family = $(this).val();
        setActiveFontStyle(_self.activeSelection, 'fontFamily', family)
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified');
      })
      $(`${this.containerSelector} .toolpanel#select-panel .sizes input`).change(function () {
        let value = parseFloat($(this).val());
        let type = $(this).attr('id');
        setActiveFontStyle(_self.activeSelection, type, value);
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified');
      })
      $(`${this.containerSelector} .toolpanel#select-panel .align #text-align`).change(function () {
        let mode = $(this).val();
        setActiveFontStyle(_self.activeSelection, 'textAlign', mode);
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified');
      })
      $(`${this.containerSelector} .toolpanel#select-panel .color #color-picker`).spectrum({
        type: "color",
        showInput: "true",
        allowEmpty: "false"
      });
      $(`${this.containerSelector} .toolpanel#select-panel .color #color-picker`).change(function () {
        let color = $(this).val();
        setActiveFontStyle(_self.activeSelection, 'fill', color)
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified');
      })
    })();
    // end font section

    // border section
    (() => {
      $(`${this.containerSelector} .toolpanel#select-panel .content`).append(`
        <div class="border-section">
          <h4>Border</h4>
          <div class="input-container"><label>Width</label>
            <div class="custom-number-input">
            <button class="decrease">-</button>
            <input type="number" min="1" value="1" id="input-border-width">
            <button class="increase">+</button>
            </div>
          </div>
          <div class="input-container"><label>Style</label><select id="input-border-style">${BorderStyleList.map(item => `<option value='${JSON.stringify(item.value)}'>${item.label}</option>`)}</select></div>
          <div class="input-container"><label>Corner Type</label><select id="input-corner-type"><option value="miter" selected>Square</option><option value="round">Round</option></select></div>
          <div class="input-container"><label>Color</label><input id="color-picker" value="black"></div>
          <hr>
        </div>
      `);
      $(`${this.containerSelector} .toolpanel#select-panel .border-section #color-picker`).spectrum({
        showButtons: false,
        type: "color",
        showInput: "true",
        allowEmpty: "false",
        move: function (color) {
          let hex = 'transparent';
          color && (hex = color.toRgbString()); // #ff0000
          _self.canvas.getActiveObjects().forEach(obj => obj.set('stroke', hex))
          _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
        }
      });
      $(`${this.containerSelector} .toolpanel#select-panel .border-section #input-border-width`).change(function () {
        let width = parseInt($(this).val());
        _self.canvas.getActiveObjects().forEach(obj => obj.set({
          strokeUniform: true,
          strokeWidth: width
        }))
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
      })
      $(`${this.containerSelector} .toolpanel#select-panel .border-section #input-border-style`).change(function () {
        try {
          let style = JSON.parse($(this).val());
          _self.canvas.getActiveObjects().forEach(obj => obj.set({
            strokeUniform: true,
            strokeDashArray: style.strokeDashArray,
            strokeLineCap: style.strokeLineCap
          }))
          _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
        } catch (_) {}
      })
      $(`${this.containerSelector} .toolpanel#select-panel .border-section #input-corner-type`).change(function () {
        let corner = $(this).val();
        _self.canvas.getActiveObjects().forEach(obj => obj.set('strokeLineJoin', corner))
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
      })
    })();
    // end border section

    // fill color section
    (() => {
      $(`${this.containerSelector} .toolpanel#select-panel .content`).append(`
        <div class="fill-section">
          <div class="tab-container">
          <div class="tabs">
            <div class="tab-label" data-value="color-fill">Color Fill</div>
            <div class="tab-label" data-value="gradient-fill">Gradient Fill</div>
          </div>
          <div class="tab-content" data-value="color-fill">
            <input id="color-picker" value='black'/><br>
          </div>
          <div class="tab-content" data-value="gradient-fill">
            <div id="gradient-picker"></div>
            <div class="gradient-orientation-container">
              <div class="input-container">
                <label>Orientation</label>
                <select id="select-orientation">
                  <option value="linear">Linear</option>
                  <option value="radial">Radial</option>
                </select>
              </div>
              <div id="angle-input-container" class="input-container">
                <label>Angle</label>
                <div class="custom-number-input">
                  <button class="decrease">-</button>
                  <input type="number" min="0" max="360" value="0" id="input-angle">
                  <button class="increase">+</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        </div>
      `);
      $(`${this.containerSelector} .toolpanel#select-panel .content .tab-label`).click(function () {
        $(`${_self.containerSelector} .toolpanel#select-panel .content .tab-label`).removeClass('active');
        $(this).addClass('active');
        let target = $(this).data('value');
        $(this).closest('.tab-container').find('.tab-content').hide();
        $(this).closest('.tab-container').find(`.tab-content[data-value=${target}]`).show();
        if (target === 'color-fill') {
          let color = $(`${_self.containerSelector} .toolpanel#select-panel .fill-section #color-picker`).val();
          try {
            _self.canvas.getActiveObjects().forEach(obj => obj.set('fill', color))
            _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
          } catch (_) {
            console.log("can't update background color")
          }
        } else {
          updateGradientFill();
        }
      })
      $(`${_self.containerSelector} .toolpanel#select-panel .content .tab-label[data-value=color-fill]`).click();
      $(`${this.containerSelector} .toolpanel#select-panel .fill-section #color-picker`).spectrum({
        flat: true,
        showPalette: false,
        showButtons: false,
        type: "color",
        showInput: "true",
        allowEmpty: "false",
        move: function (color) {
          let hex = 'transparent';
          color && (hex = color.toRgbString()); // #ff0000
          _self.canvas.getActiveObjects().forEach(obj => obj.set('fill', hex))
          _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
        }
      });
      const gp = new Grapick({
        el: `${this.containerSelector} .toolpanel#select-panel .fill-section #gradient-picker`,
        colorEl: '<input id="colorpicker"/>'
      });
      gp.setColorPicker(handler => {
        const el = handler.getEl().querySelector('#colorpicker');
        $(el).spectrum({
          showPalette: false,
          showButtons: false,
          type: "color",
          color: handler.getColor(),
          showAlpha: true,
          change(color) {
            handler.setColor(color.toRgbString());
          },
          move(color) {
            handler.setColor(color.toRgbString(), 0);
          }
        });
      });
      gp.addHandler(0, 'red');
      gp.addHandler(100, 'blue');
      const updateGradientFill = () => {
        let stops = gp.getHandlers();
        let orientation = $(`${this.containerSelector} .toolpanel#select-panel .content .gradient-orientation-container #select-orientation`).val();
        let angle = parseInt($(`${this.containerSelector} .toolpanel#select-panel .content .gradient-orientation-container #input-angle`).val());

        let gradient = generateFabricGradientFromColorStops(stops, _self.activeSelection.width, _self.activeSelection.height, orientation, angle);
        _self.activeSelection.set('fill', gradient);
        _self.canvas.renderAll()
      }
      gp.on('change', complete => {
        updateGradientFill();
      })
      $(`${this.containerSelector} .toolpanel#select-panel .content .gradient-orientation-container #select-orientation`).change(function () {
        let type = $(this).val();
        console.log('orientation', type)
        if (type === 'radial') {
          $(this).closest('.gradient-orientation-container').find('#angle-input-container').hide();
        } else {
          $(this).closest('.gradient-orientation-container').find('#angle-input-container').show();
        }
        updateGradientFill();
      })
      $(`${this.containerSelector} .toolpanel#select-panel .content .gradient-orientation-container #input-angle`).change(function () {
        updateGradientFill();
      })
    })();
    // end fill color section

    // object options section
    (() => {
      $(`${this.containerSelector} .toolpanel#select-panel .content`).append(`
        <div class="object-options">
          <h4>Object Options</h4>
          <button id="flip-h"><svg width="512" height="512" enable-background="new 0 0 16 16" viewBox="0 0 16 20" xml:space="preserve"><g transform="matrix(0 1.5365 1.5385 0 -5.0769 1.5495)"><rect x="5" y="8" width="1" height="1"></rect><rect x="7" y="8" width="1" height="1"></rect><rect x="9" y="8" width="1" height="1"></rect><rect x="1" y="8" width="1" height="1"></rect><rect x="3" y="8" width="1" height="1"></rect><path d="M 1,2 5.5,6 10,2 Z M 7.37,3 5.5,4.662 3.63,3 Z"></path><polygon points="10 15 5.5 11 1 15"></polygon></g></svg></button>
          <button id="flip-v"><svg width="512" height="512" enable-background="new 0 0 16 16" viewBox="0 0 16 20" xml:space="preserve"><g transform="matrix(1.5365 0 0 1.5385 -.45052 -3.0769)"><rect x="5" y="8" width="1" height="1"></rect><rect x="7" y="8" width="1" height="1"></rect><rect x="9" y="8" width="1" height="1"></rect><rect x="1" y="8" width="1" height="1"></rect><rect x="3" y="8" width="1" height="1"></rect><path d="M 1,2 5.5,6 10,2 Z M 7.37,3 5.5,4.662 3.63,3 Z"></path><polygon points="5.5 11 1 15 10 15"></polygon></g></svg></button>
          <button id="duplicate"><svg id="Capa_1" x="0px" y="0px" viewBox="0 0 512 512" xml:space="preserve"><g><g><g><path d="M42.667,256c0-59.52,35.093-110.827,85.547-134.827V75.2C53.653,101.44,0,172.48,0,256s53.653,154.56,128.213,180.8 v-45.973C77.76,366.827,42.667,315.52,42.667,256z"></path><path d="M320,64c-105.92,0-192,86.08-192,192s86.08,192,192,192s192-86.08,192-192S425.92,64,320,64z M320,405.333 c-82.347,0-149.333-66.987-149.333-149.333S237.653,106.667,320,106.667S469.333,173.653,469.333,256 S402.347,405.333,320,405.333z"></path><polygon points="341.333,170.667 298.667,170.667 298.667,234.667 234.667,234.667 234.667,277.333 298.667,277.333 298.667,341.333 341.333,341.333 341.333,277.333 405.333,277.333 405.333,234.667 341.333,234.667  "></polygon></g></g></g></svg></button>
          <button id="delete"><svg id="Layer_1" x="0px" y="0px" viewBox="0 0 512 512" xml:space="preserve"><g><g><path d="M425.298,51.358h-91.455V16.696c0-9.22-7.475-16.696-16.696-16.696H194.855c-9.22,0-16.696,7.475-16.696,16.696v34.662 H86.704c-9.22,0-16.696,7.475-16.696,16.696v51.357c0,9.22,7.475,16.696,16.696,16.696h5.072l15.26,359.906 c0.378,8.937,7.735,15.988,16.68,15.988h264.568c8.946,0,16.302-7.051,16.68-15.989l15.259-359.906h5.073 c9.22,0,16.696-7.475,16.696-16.696V68.054C441.994,58.832,434.519,51.358,425.298,51.358z M211.551,33.391h88.9v17.967h-88.9 V33.391z M372.283,478.609H139.719l-14.522-342.502h261.606L372.283,478.609z M408.602,102.715c-15.17,0-296.114,0-305.202,0 V84.749h305.202V102.715z"></path></g></g><g><g><path d="M188.835,187.304c-9.22,0-16.696,7.475-16.696,16.696v206.714c0,9.22,7.475,16.696,16.696,16.696 c9.22,0,16.696-7.475,16.696-16.696V204C205.53,194.779,198.055,187.304,188.835,187.304z"></path></g></g><g><g><path d="M255.998,187.304c-9.22,0-16.696,7.475-16.696,16.696v206.714c0,9.22,7.474,16.696,16.696,16.696 c9.22,0,16.696-7.475,16.696-16.696V204C272.693,194.779,265.218,187.304,255.998,187.304z"></path></g></g><g><g><path d="M323.161,187.304c-9.22,0-16.696,7.475-16.696,16.696v206.714c0,9.22,7.475,16.696,16.696,16.696 s16.696-7.475,16.696-16.696V204C339.857,194.779,332.382,187.304,323.161,187.304z"></path></g></g></svg></button>
          <hr>
        </div>
      `);
      $(`${this.containerSelector} .toolpanel#select-panel .object-options #flip-h`).click(() => {
        this.activeSelection.set('flipX', !this.activeSelection.flipX);
        this.canvas.renderAll(), this.canvas.trigger('object:modified');
      })
      $(`${this.containerSelector} .toolpanel#select-panel .object-options #flip-v`).click(() => {
        this.activeSelection.set('flipY', !this.activeSelection.flipY);
        this.canvas.renderAll(), this.canvas.trigger('object:modified');
      })
      $(`${this.containerSelector} .toolpanel#select-panel .object-options #duplicate`).click(() => {
        let clonedObjects = []
        let activeObjects = this.canvas.getActiveObjects()
        activeObjects.forEach(obj => {
          obj.clone(clone => {
            this.canvas.add(clone.set({
              strokeUniform: true,
              left: obj.aCoords.tl.x + 20,
              top: obj.aCoords.tl.y + 20
            }));

            if (activeObjects.length === 1) {
              this.canvas.setActiveObject(clone)
            }
            clonedObjects.push(clone)
          })
        })
        if (clonedObjects.length > 1) {
          let sel = new fabric.ActiveSelection(clonedObjects, {
            canvas: this.canvas,
          });
          this.canvas.setActiveObject(sel)
        }
        this.canvas.requestRenderAll(), this.canvas.trigger('object:modified')
      })
      $(`${this.containerSelector} .toolpanel#select-panel .object-options #delete`).click(() => {
        this.canvas.getActiveObjects().forEach(obj => this.canvas.remove(obj))
        this.canvas.discardActiveObject().requestRenderAll(), this.canvas.trigger('object:modified');
      })
    })();
    // end object options section

    // effect section
    (() => {
      $(`${this.containerSelector} .toolpanel#select-panel .content`).append(`
        <div class="effect-section">
          <h4>Effect</h4>
          <div class="input-container"><label>Opacity</label><input id="opacity" type="range" min="0" max="1" value="1" step="0.01"></div>
          <div class="input-container"><label>Blur</label><input class="effect" id="blur" type="range" min="0" max="100" value="50"></div>
          <div class="input-container"><label>Brightness</label><input class="effect" id="brightness" type="range" min="0" max="100" value="50"></div>
          <div class="input-container"><label>Saturation</label><input class="effect" id="saturation" type="range" min="0" max="100" value="50"></div>
          <h5>Gamma</h5>
          <div class="input-container"><label>Red</label><input class="effect" id="gamma.r" type="range" min="0" max="100" value="50"></div>
          <div class="input-container"><label>Green</label><input class="effect" id="gamma.g" type="range" min="0" max="100" value="50"></div>
          <div class="input-container"><label>Blue</label><input class="effect" id="gamma.b" type="range" min="0" max="100" value="50"></div>
          <hr>
        </div>
      `);
      $(`${this.containerSelector} .toolpanel#select-panel .effect-section #opacity`).change(function () {
        let opacity = parseFloat($(this).val());
        _self.activeSelection.set('opacity', opacity)
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
      })
      $(`${this.containerSelector} .toolpanel#select-panel .effect-section .effect`).change(function () {
        let effect = $(this).attr('id');
        let value = parseFloat($(this).val());
        let currentEffect = getCurrentEffect(_self.activeSelection);
        _self.activeSelection.filters = getUpdatedFilter(currentEffect, effect, value);
        _self.activeSelection.applyFilters();
        _self.canvas.renderAll(), _self.canvas.trigger('object:modified')
      })
    })();
    // end effect section
  }
  window.ImageEditor.prototype.initializeSelectionSettings = selectionSettings;
})()