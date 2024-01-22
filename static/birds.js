document.addEventListener('DOMContentLoaded', (event) => {
    VANTA.BIRDS({
        el: "body",
        backgroundColor: "rgba(0,0,0,0)", // Transparent background for birds
        color1: 0x0,
        color2: 0x244855,
        // Other Vanta.js settings
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 400.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        birdSize: 1.40,
        wingSpan: 20.00,
        separation: 50.00,
        alignment: 20.00,
        cohesion: 20.00,
        quantity: 4.00,
        backgroundAlpha: 0.65
    });

});
