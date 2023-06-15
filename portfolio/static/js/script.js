window.addEventListener('scroll', () => {
    const scrollElements = document.querySelectorAll('.scroll-element');
    scrollElements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        if (elementPosition < window.innerHeight - 100) {
            element.classList.add('active');
        }
    });

    const articleElement = document.querySelector('article');
    const articlePosition = articleElement.getBoundingClientRect().top;
    if (articlePosition < window.innerHeight - 100) {
        articleElement.classList.add('active');
    }
});