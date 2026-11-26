window.addEventListener('DOMContentLoaded', () => {
    const errorTitle = document.querySelector('.error-title');
    const homeLink = document.querySelector('header .click-here a[href="/"]');

    if (errorTitle) {
        errorTitle.focus();

        errorTitle.addEventListener('keydown', (event) => {
            if (event.key === 'Tab' && !event.shiftKey && homeLink) {
                event.preventDefault();
                homeLink.focus();
            }
        });
    }
});