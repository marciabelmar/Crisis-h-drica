document.addEventListener('DOMContentLoaded', function () {
    let count = 0;
    const targetCount = 7000;
    const increment = 50; // Incremento del contador
    const interval = 30; // Intervalo en milisegundos

    const countElement = document.getElementById('counter');

    function updateCounter() {
        count += increment;
        if (count >= targetCount) {
            count = targetCount;
            clearInterval(counterInterval);
        }
        countElement.innerText = count.toLocaleString();
    }

    const counterInterval = setInterval(updateCounter, interval);
});



