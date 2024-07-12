document.addEventListener('DOMContentLoaded', () => {
    const title = document.getElementById('title');

    setTimeout(() => {
        title.classList.add('show');
    }, 500);

    setTimeout(() => {
        title.classList.add('change-color');
    }, 1500);  
});
