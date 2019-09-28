var canvas, ctx, p = function(x, y) {
    return { x: x, y: y };
};

// drawing
$(function() {
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext('2d');
    ctx.canvas.width = window.innerWidth;
    ctx.canvas.height = window.innerHeight;

    ctx.lineCap = 'round';
    ctx.lineWidth = 4;

    ctx.strokeStyle = 'rgba(50,30,120,0.5)';
    ctx.beginPath();
    ctx.wavy(p(80, 120), p(350, 120), 8, 12, 4);
    ctx.stroke();

    ctx.strokeStyle = 'rgba(255,60,0,0.8)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.wavy(p(380, 120), p(450, 390), 23, 32, 1);
    ctx.stroke();

    ctx.setLineDash([6, 12]);
    ctx.strokeStyle = 'rgba(10,190,40,0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.wavy(p(80, 180), p(350, 180), 8, 12, 4, true);
    ctx.stroke();


});



CanvasRenderingContext2D.prototype.wavy = function(from, to, frequency, amplitude, step, negative) {
    var cx = 0,
        cy = 0,
        fx = from.x,
        fy = from.y,
        tx = to.x,
        ty = to.y,
        i = 0,
        waveOffsetLength = 0,

        ang = Math.atan2(ty - fy, tx - fx),
        distance = Math.sqrt((fx - tx) * (fx - tx) + (fy - ty) * (fy - ty)),
        a = amplitude * (!negative ? 1 : -1),
        f = Math.PI * frequency;

    for (i; i <= distance; i += step) {
        waveOffsetLength = Math.sin((i / distance) * f) * a;
        cx = from.x + Math.cos(ang) * i + Math.cos(ang - Math.PI / 2) * waveOffsetLength;
        cy = from.y + Math.sin(ang) * i + Math.sin(ang - Math.PI / 2) * waveOffsetLength;
        i > 0 ? this.lineTo(cx, cy) : this.moveTo(cx, cy);
    }
}