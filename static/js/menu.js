const iconMenu = document.querySelector('.icon-menu');
const menu = document.querySelector('.menu-navegacion');

console.log(iconMenu)
console.log(menu)

iconMenu.addEventListener('click', () => {
    menu.classList.toggle('spread')
})

window.addEventListener('click', e => {
    if (menu.classList.contains('spread') && e.target != menu &&
        e.target != iconMenu) {

        menu.classList.toggle('spread')
    }
})