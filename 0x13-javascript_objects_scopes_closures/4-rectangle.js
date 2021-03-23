#!/usr/bin/node
module.exports = {
    Rectangle: function (w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	}
	this.print = function () {
	    for (let i = 0; i < this.height; i++) {
		console.log(('X').repeat(this.width));
	    }
	};
	this.rotate = function () {
	    [this.widht, this.height] = [this.height, this.widht];
	};
	this.double = funtion () {
	    this.widht *= 2;
	    this.height *= 2;
	};
    }
};
