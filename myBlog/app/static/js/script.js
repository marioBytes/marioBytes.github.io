// Mobile Nav Init
let sidenavElem = document.querySelector('.sidenav');
let sidenavInst = new M.Sidenav(sidenavElem, {
    inDuration: 400,
    outDuration: 450
});

// Parallax Init
let parallaxElm = document.querySelector('.parallax');
let parallaxInst = new M.Parallax(parallaxElm, {});

// Modal Init
let modalElem = document.querySelector('.modal');
let modalInst = new M.Modal(modalElem, {});