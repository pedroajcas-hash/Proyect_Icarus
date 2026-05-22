// JavaScript básico para la página web y genérico para todos los archivos

document.addEventListener('DOMContentLoaded', function () {
    const botonesMenu = document.querySelectorAll('.menu_principal_boton');

    botonesMenu.forEach(function (boton) {
        boton.addEventListener('mouseenter', function () {
            boton.classList.add('menu_principal_boton_sobresaliente');
        });

        boton.addEventListener('mouseleave', function () {
            boton.classList.remove('menu_principal_boton_sobresaliente');
        });
    });
});
