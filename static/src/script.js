document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.ui.form');
    const titleInput = form.querySelector('input[name="title"]');
    const detailInput = form.querySelector('input[name="detail"]');

    form.addEventListener('submit', function(event) {
        let isValid = true;

        titleInput.classList.remove('error');
        detailInput.classList.remove('error');

        if (titleInput.value.trim() === '') {
            isValid = false;
            titleInput.classList.add('error');
            alert('Por favor, ingrese un título para la tarea.');
        }

        if (detailInput.value.trim() === '') {
            isValid = false;
            detailInput.classList.add('error');
            alert('Por favor, ingrese un detalle para la tarea.');
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});
